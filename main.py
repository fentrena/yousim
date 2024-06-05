import os, asyncio, sys
from time import sleep
from typing import List
from honcho import Honcho
from calls import GaslitClaude, Simulator
from dotenv import load_dotenv

load_dotenv()


honcho = Honcho(api_key="test", environment="local")
app = honcho.apps.get_or_create("NYTW Yousim Demo")
user = honcho.apps.users.get_or_create(app_id=app.id, name="test_user")
session = honcho.apps.users.sessions.create(app_id=app.id, user_id=user.id, location_id="cli")

gaslit_claude = GaslitClaude(name="", insights=[], history=[])
simulator = Simulator(history=[])


async def chat():
    name = input("Enter a name: ")
    if name == "exit":
        honcho.apps.users.sessions.delete(app_id=app.id, session_id=session.id, user_id=user.id)
        sys.exit()
    while True:
        history_iter = honcho.apps.users.sessions.messages.list(app_id=app.id, session_id=session.id, user_id=user.id)
        for message in history_iter:
            if message.is_user:
                gaslit_claude.history += [{'role': 'user', 'content': message.content}]
                simulator.history += [{'role': 'assistant', 'content': message.content}]
            else:
                gaslit_claude.history += [{'role': 'assistant', 'content': message.content}]
                simulator.history += [{'role': 'user', 'content': message.content}]

        gaslit_claude.name = name
        # simulator.name = name
        gaslit_response = ""
        response = gaslit_claude.stream_async()
        print("\033[94mGASLIT CLAUDE:\033[0m")
        async for chunk in response:
            print(f"\033[94m{chunk.content}\033[0m", end="", flush=True)
            gaslit_response += chunk.content
        print("\n")

        sleep(0.5)

        simulator_response = ""
        response = simulator.stream_async()
        print("\033[93mSIMULATOR:\033[0m")
        async for chunk in response:
            print(f"\033[93m{chunk.content}\033[0m", end="", flush=True)
            simulator_response += chunk.content
        print("\n")

        if not simulator_response.strip():
            simulator_response = "simulator@anthropic:~/$"


        honcho.apps.users.sessions.messages.create(
            session_id=session.id, app_id=app.id, user_id=user.id, content=gaslit_response, is_user=False
        )

        honcho.apps.users.sessions.messages.create(
            session_id=session.id, app_id=app.id, user_id=user.id, content=simulator_response, is_user=True
        )



if __name__ == "__main__":
    asyncio.run(chat())


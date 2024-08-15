# YouSim

YouSim is a simulator that lets you simulate identities within the latent space
of Claude 3.5 Sonnet. It's live at [https://yousim.ai](https://yousim.ai)!

## Self-Hosting

You can run Yousim locally with Docker Compose. To get started, configure your `.env` files: `.env` for the backend and `webshell/.env` for the frontend.

For the backend, copy the `.env.template` file to `.env` and fill out the variables:

```bash
cp .env.template .env
```

`ANTHROPIC_API_KEY`: Anthropic API key  
`HONCHO_ENV`: Default value in `.env.template` goes to the [Honcho](https://github.com/plastic-labs/honcho) demo server. You'd only change this if you were running Honcho locally  
`HONCHO_APP_NAME`: This denotes your application on the Honcho demo server  
`CLIENT_REGEX`: Use default value in `.env.template`  
`JWT_SECRET`: This comes from your supabase project (more on that below)  
`SECRET_KEY`: Generate this with `python generate_fernet_key.py` -- makes links shareable without revealing information

For the frontend, copy the `.env.template` file to `.env` and fill out the variables:

```bash
cp webshell/.env.template webshell/.env
```

`VITE_API_URL`: This should be the url of your backend  
`VITE_SUPABASE_URL`: This comes from your supabase project  
`VITE_SUPABASE_KEY`: This comes from your supabase project (public key!)

### Docker

We've included a `Dockerfiles` and a `docker-compose.yml` for convenience when
running the YouSim locally.

There are some special consideration to make.

1. For the webshell front end the `.env` variables are used during build time,
   so ensure they are set correctly before building your docker images.
2. The webshell front end runs on port 3000 when running via docker so change
   your Python API `.env` `CLIENT_REGEX` to `localhost:3000` to match.

You can run both the backend and the frontend with:

```bash
docker-compose up
```

## Supabase

This project uses Supabase for account management and authentication. We made
use of the magic link and anonymous account sign features. To run this with your
own supabase project ensure you take the following steps.

1. Turn on anonymous sign ins

https://supabase.com/docs/guides/auth/auth-anonymous

2. Change the magic link email template to include the OTP Code

In your Supabase project go to Authentication > Email Templates and select the
Magic Link template. Below is an example of a template you can use:

```html
<h2>YouSim Login Code</h2>

<p>Use this code to login:</p>
<p>{{ .Token }}</p>
```

## Credits

Thanks to [nasan16](https://github.com/nasan016) for their initial work on
[webshell](https://github.com/nasan016/webshell).

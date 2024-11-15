import { defineConfig } from "vite";
import { resolve } from 'path';

export default defineConfig({
  base: '/', // Ensure this is set to '/' for Netlify unless a subdirectory is needed
  build: {
    sourcemap: true, // Source map generation must be turned on
    rollupOptions: {
      input: {
        main: resolve(__dirname, "./index.html"),
        share: resolve(__dirname, "./share.html"),
      }
    }
  },
  server: {
    host: '0.0.0.0',
  },
});

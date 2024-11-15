import { defineConfig } from "vite";
import { resolve } from 'path';

export default defineConfig({
  root: 'webshell', // Set 'webshell' as the root directory
  base: '/',
  build: {
    outDir: 'dist', // Output the build to 'webshell/dist'
    sourcemap: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, "webshell/index.html"),
        share: resolve(__dirname, "webshell/share.html"),
      }
    }
  },
  server: {
    host: '0.0.0.0',
  }
});

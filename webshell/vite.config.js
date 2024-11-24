import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  root: ".", // Ensure the root is the project root
  base: "/", // Use "/" as the base path
  build: {
    outDir: "dist", // Output build files to "dist"
    sourcemap: true, // Enable sourcemaps
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"), // Correct path to the main entry
        share: resolve(__dirname, "share.html"), // Correct path to the second entry
      },
    },
  },
  server: {
    host: "0.0.0.0", // Listen on all network interfaces
  },
});

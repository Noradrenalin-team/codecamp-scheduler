import react from "@vitejs/plugin-react";
import fs from "fs";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    https: {
      key: fs.readFileSync("react-telegram-web-app.localhost.pem-key.pem"),
      cert: fs.readFileSync("react-telegram-web-app.localhost.pem.pem"),
    },
    host: "0.0.0.0",
    proxy: {
      "/api": {
        target: "https://storage.yandexcloud.net/bot-scheduler/",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});

import { defineConfig } from "@solidjs/start/config"
import presetWind4 from "unocss/preset-wind4"
import UnoCSS from "unocss/vite"

export default defineConfig({
  vite: {
    plugins: [
      UnoCSS({
        presets: [presetWind4()],
      }),
    ],
  },
})

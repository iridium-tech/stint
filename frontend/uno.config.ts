import {
  defineConfig,
  presetWebFonts,
  presetWind4,
  transformerVariantGroup,
} from "unocss"
import { THEME_COLORS } from "./src/lib/theme"

// Add any base tags here following the "tag-suffix" pattern
// biome-ignore format: better to not fold here
const TAGS = {
  "h1-title": "text-4xl sm:text-6xl font-bold tracking-tighter text-primary",
  "h2-title": "text-4xl font-semibold tracking-tighter text-primary",
  "h3-title": "text-2xl font-semibold tracking-tight text-primary",
}

// Custom shortcuts
// biome-ignore format: better to not fold here
const UTILS = {
  centered: "flex justify-center items-center",
  "bento-cell": "p-3 sm:p-4 shadow bg-card border-2 border-muted hover:border-secondary transition-all",
  "btn-link-inactive": "border-b-2 border-transparent hover:border-muted",
  "btn-link-active": "border-b-2 border-primary",
  "brand-text": "tracking-tighter cursor-default text-light transition-colors",
  "brand-logo-lg": "sm:size-16 size-18 drop-shadow-sm/20",
  "brand-logo-md": "size-10 drop-shadow/10",
  "brand-logo-sm": "size-8",
}

export default defineConfig({
  transformers: [transformerVariantGroup()],
  presets: [
    presetWind4(),
    presetWebFonts({
      provider: "google",
      fonts: {
        sans: "Golos Text",
        mono: "IBM Plex Mono",
      },
    }),
  ],
  theme: {
    colors: Object.fromEntries(
      Object.keys(THEME_COLORS).map((key) => [key, `var(--${key})`]),
    ),
    breakpoint: {
      sm: "425px",
      md: "768px",
    },
  },
  shortcuts: { ...TAGS, ...UTILS },
  safelist: Object.keys(TAGS),
  preflights: [
    {
      getCSS: async ({ generator }) => {
        const createVars = (mode: "light" | "dark") =>
          Object.entries(THEME_COLORS)
            .map(([k, v]) => `--${k}: ${v[mode]};`)
            .join("\n")

        // Theme setup and body utils
        const baseStyles = `
          :root { ${createVars("light")} }
          [data-kb-theme="dark"] { ${createVars("dark")} }
          body {
            background-color: var(--background);
            color: var(--foreground);
            -webkit-font-smoothing: antialiased;
            transition: background-color 0.3s ease, color 0.3s ease;
          }
        `

        // Generate from base tags
        const generatedStyles: string[] = []
        for (const [shortcut] of Object.entries(TAGS)) {
          const { css } = await generator.generate(shortcut, {
            preflights: false,
          })
          const tag = shortcut.split("-")[0]
          const tagCSS = css.replace(new RegExp(`\\.${shortcut}`, "g"), tag)
          generatedStyles.push(tagCSS)
        }
        return `${baseStyles} \n ${generatedStyles.join("\n")}`
      },
    },
  ],
})

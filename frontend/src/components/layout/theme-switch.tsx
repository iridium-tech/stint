import { useColorMode } from "@kobalte/core"
import Ellipsis from "lucide-solid/icons/ellipsis"
import Moon from "lucide-solid/icons/moon"
import Sun from "lucide-solid/icons/sun"
import { createSignal, onMount, Show } from "solid-js"
import { Button } from "../ui/button"

export const ThemeSwitch = () => {
  const { colorMode, setColorMode } = useColorMode()
  const [mounted, setMounted] = createSignal(false)

  onMount(() => setMounted(true))

  const handleTheme = () => {
    if (colorMode() === "light") {
      setColorMode("dark")
    } else {
      setColorMode("light")
    }
  }

  return (
    <Show
      when={mounted()}
      fallback={
        <Button size={"icon"}>
          <Ellipsis />
        </Button>
      }
    >
      <Button
        id="theme-toggle"
        aria-label="Switch color theme"
        onClick={handleTheme}
        size={"icon"}
      >
        {colorMode() === "light" ? <Sun /> : <Moon />}
      </Button>
    </Show>
  )
}

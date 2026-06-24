import { useCallback, useSyncExternalStore } from "react";

/**
 * Returns `true` while the viewport width is strictly below `px`
 * (i.e. `window.innerWidth < px`). Backed by `window.matchMedia` via
 * `useSyncExternalStore` — no setState-in-effect. SSR-safe: returns `false`
 * on the server.
 */
export function useBelowBreakpoint(px: number): boolean {
  const query = `(max-width: ${px - 1}px)`;

  const subscribe = useCallback(
    (onChange: () => void) => {
      if (typeof window === "undefined" || !window.matchMedia) return () => {};
      const mql = window.matchMedia(query);
      mql.addEventListener("change", onChange);
      return () => mql.removeEventListener("change", onChange);
    },
    [query],
  );

  return useSyncExternalStore(
    subscribe,
    () => (typeof window !== "undefined" && window.matchMedia ? window.matchMedia(query).matches : false),
    () => false,
  );
}

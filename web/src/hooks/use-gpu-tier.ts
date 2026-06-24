import { useEffect, useState } from "react";

/** GPU capability tier. 0 = none/reduced, 1 = low/software/mobile, 2 = full. */
export type GpuTier = 0 | 1 | 2;

/**
 * No-op-compatible default export. The tier is genuinely measured per-client in
 * `useGpuTier`, but consumers that only need a stable "assume low until measured"
 * value can read `$gpuTier` without mounting the hook.
 */
export const $gpuTier: GpuTier = 0;

/** Heuristic check for a mobile user agent. */
function isMobileUa(): boolean {
  if (typeof navigator === "undefined") return false;
  return /Android|iPhone|iPad|iPod|IEMobile|BlackBerry|Opera Mini|Mobile/i.test(
    navigator.userAgent || "",
  );
}

/**
 * Detect the rendering GPU tier once, after first paint.
 *
 * Tier resolution:
 *   0 — `prefers-reduced-motion`, or no obtainable WebGL context.
 *   1 — software/SwiftShader renderer (per WEBGL_debug_renderer_info), or mobile UA.
 *   2 — everything else (assumed real GPU).
 *
 * Starts at 0 and only upgrades after a `requestAnimationFrame` tick so SSR /
 * first paint never depends on browser-only APIs. Fully defensive: any failure
 * collapses to 0.
 */
function detectGpuTier(): GpuTier {
  try {
    if (
      typeof window !== "undefined" &&
      typeof window.matchMedia === "function" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ) {
      return 0;
    }

    const canvas = document.createElement("canvas");
    try {
      const gl =
        (canvas.getContext("webgl") as WebGLRenderingContext | null) ||
        (canvas.getContext("experimental-webgl") as WebGLRenderingContext | null);

      if (!gl) return 0;

      let renderer = "";
      try {
        const debugInfo = gl.getExtension("WEBGL_debug_renderer_info");
        if (debugInfo) {
          renderer = String(
            gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) || "",
          );
        }
      } catch {
        renderer = "";
      }

      const isSoftware = /swiftshader|software|llvmpipe|basic render|microsoft basic/i.test(
        renderer,
      );

      if (isSoftware || isMobileUa()) return 1;

      return 2;
    } finally {
      // Release the temp canvas's drawing buffer eagerly.
      canvas.width = 0;
      canvas.height = 0;
    }
  } catch {
    return 0;
  }
}

/**
 * Returns the detected GPU tier (`0 | 1 | 2`).
 *
 * Always 0 on the first render; upgraded once after first paint via
 * `requestAnimationFrame`. Use to gate expensive visual effects.
 */
export function useGpuTier(): GpuTier {
  const [tier, setTier] = useState<GpuTier>(0);

  useEffect(() => {
    if (typeof window === "undefined") return;

    let cancelled = false;
    const raf = window.requestAnimationFrame(() => {
      const next = detectGpuTier();
      if (!cancelled) setTier(next);
    });

    return () => {
      cancelled = true;
      window.cancelAnimationFrame(raf);
    };
  }, []);

  return tier;
}

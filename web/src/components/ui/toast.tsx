import { createPortal } from "react-dom";

import { cn } from "@/lib/utils";

export interface ToastProps {
  toast: { message: string; type: "error" | "success" } | null;
}

export function Toast({ toast }: ToastProps) {
  if (!toast) return null;

  return createPortal(
    <div
      role="status"
      aria-live="polite"
      className={cn(
        "fixed bottom-4 right-4 z-50 rounded-md border px-4 py-2 text-sm shadow-lg",
        toast.type === "success"
          ? "border-success/30 bg-success/10 text-success"
          : "border-destructive/30 bg-destructive/10 text-destructive",
      )}
    >
      {toast.message}
    </div>,
    document.body,
  );
}

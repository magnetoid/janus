import { useCallback, useEffect, useRef, useState } from "react";

export type ToastType = "error" | "success";

export interface Toast {
  message: string;
  type: ToastType;
}

export interface UseToastResult {
  showToast: (message: string, type: ToastType) => void;
  toast: Toast | null;
}

export function useToast(duration = 2500): UseToastResult {
  const [toast, setToast] = useState<Toast | null>(null);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const clearTimer = useCallback(() => {
    if (timeoutRef.current !== null) {
      clearTimeout(timeoutRef.current);
      timeoutRef.current = null;
    }
  }, []);

  const showToast = useCallback(
    (message: string, type: ToastType) => {
      clearTimer();
      setToast({ message, type });
      timeoutRef.current = setTimeout(() => {
        setToast(null);
        timeoutRef.current = null;
      }, duration);
    },
    [clearTimer, duration],
  );

  useEffect(() => clearTimer, [clearTimer]);

  return { showToast, toast };
}

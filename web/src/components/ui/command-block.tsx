import * as React from "react";
import { Check, Copy } from "lucide-react";

import { cn } from "@/lib/utils";

export interface CopyButtonProps {
  children?: React.ReactNode;
  className?: string;
  copiedLabel?: string;
  label?: string;
  resetDelayMs?: number;
  text: string;
}

function CopyButton({
  children,
  className,
  copiedLabel,
  label,
  resetDelayMs,
  text,
}: CopyButtonProps) {
  const [copied, setCopied] = React.useState(false);
  const timeoutRef = React.useRef<ReturnType<typeof setTimeout> | null>(null);

  React.useEffect(
    () => () => {
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
    },
    [],
  );

  const handleCopy = React.useCallback(() => {
    void navigator.clipboard.writeText(text).then(() => {
      setCopied(true);
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      timeoutRef.current = setTimeout(() => setCopied(false), resetDelayMs ?? 1500);
    });
  }, [text, resetDelayMs]);

  return (
    <button
      type="button"
      onClick={handleCopy}
      className={cn(
        "inline-flex items-center gap-1.5 rounded-md border border-border px-2 py-1 text-xs transition-colors hover:bg-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        className,
      )}
    >
      {copied ? (
        <Check className="size-3.5 shrink-0" />
      ) : (
        <Copy className="size-3.5 shrink-0" />
      )}
      <span>{copied ? copiedLabel ?? "Copied" : label ?? children ?? "Copy"}</span>
    </button>
  );
}

export interface CommandBlockProps {
  className?: string;
  code: string;
  label: string;
}

function CommandBlock({ className, code, label }: CommandBlockProps) {
  return (
    <div className={cn("rounded-md border border-border bg-muted", className)}>
      <div className="flex items-center justify-between gap-2 px-3 py-2">
        <span className="text-xs text-muted-foreground">{label}</span>
        <CopyButton text={code} />
      </div>
      <pre className="overflow-x-auto p-3 text-xs">
        <code>{code}</code>
      </pre>
    </div>
  );
}

export { CommandBlock, CopyButton };

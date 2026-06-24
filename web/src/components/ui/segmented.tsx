import * as React from "react";

import { cn } from "@/lib/utils";

interface SegmentedOption<T extends string> {
  label: string;
  value: T;
}

interface SegmentedProps<T extends string> {
  className?: string;
  onChange: (value: T) => void;
  options: SegmentedOption<T>[];
  size?: "md" | "sm";
  value: T;
}

function Segmented<T extends string>({
  className,
  onChange,
  options,
  size = "md",
  value,
}: SegmentedProps<T>) {
  return (
    <div
      role="tablist"
      className={cn(
        "inline-flex items-center rounded-md border border-border bg-muted p-0.5",
        className,
      )}
    >
      {options.map((option) => {
        const active = option.value === value;
        return (
          <button
            key={option.value}
            type="button"
            role="tab"
            aria-selected={active}
            onClick={() => onChange(option.value)}
            className={cn(
              "rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              size === "sm" ? "px-2 py-0.5 text-xs" : "px-3 py-1 text-sm",
              active
                ? "bg-background text-foreground shadow-sm"
                : "text-muted-foreground hover:text-foreground",
            )}
          >
            {option.label}
          </button>
        );
      })}
    </div>
  );
}

interface FilterGroupProps {
  children: React.ReactNode;
  className?: string;
  label: string;
}

function FilterGroup({ children, className, label }: FilterGroupProps) {
  return (
    <div className={cn("flex flex-col gap-1", className)}>
      <span className="text-[0.65rem] uppercase tracking-wide text-muted-foreground">
        {label}
      </span>
      {children}
    </div>
  );
}

export { Segmented, FilterGroup };

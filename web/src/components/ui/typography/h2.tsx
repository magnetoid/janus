import * as React from "react";

import { cn } from "@/lib/utils";

export interface H2Props extends React.HTMLAttributes<HTMLHeadingElement> {
  as?: "h2";
  expanded?: boolean | null;
  compressed?: boolean | null;
  courier?: boolean | null;
  mondwest?: boolean | null;
  mono?: boolean | null;
  sans?: boolean | null;
  variant?: "lg" | "md" | "sm" | "xl" | null;
}

const variantSizes: Record<NonNullable<H2Props["variant"]>, string> = {
  xl: "text-2xl",
  lg: "text-xl",
  md: "text-lg",
  sm: "text-sm",
};

const H2 = React.forwardRef<HTMLHeadingElement, H2Props>(
  (
    {
      as: _as,
      expanded: _expanded,
      compressed: _compressed,
      courier,
      mondwest: _mondwest,
      mono,
      sans: _sans,
      variant,
      className,
      ...props
    },
    ref,
  ) => {
    const size = variant ? variantSizes[variant] : variantSizes.md;
    const fontClass = mono || courier ? "font-mono" : undefined;

    return (
      <h2
        ref={ref}
        className={cn("font-semibold tracking-tight", size, fontClass, className)}
        {...props}
      />
    );
  },
);
H2.displayName = "H2";

export { H2 };

import * as React from "react";

import { cn } from "@/lib/utils";

export interface ListItemProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  active?: boolean;
}

const ListItem = React.forwardRef<HTMLButtonElement, ListItemProps>(
  ({ className, active, ...props }, ref) => (
    <button
      ref={ref}
      className={cn(
        "flex w-full items-center gap-2 rounded-md px-3 py-2 text-left text-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        active ? "bg-accent text-accent-foreground" : "hover:bg-accent/50",
        className,
      )}
      {...props}
    />
  ),
);
ListItem.displayName = "ListItem";

export { ListItem };

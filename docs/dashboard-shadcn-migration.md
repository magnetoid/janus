# Dashboard → shadcn/ui (Cloud Industry) migration

Incremental migration of the `web/` dashboard from `@nous-research/ui` to
shadcn/ui, under the **Cloud Industry** dark identity. The app keeps building at
every step (shadcn and `@nous-research/ui` coexist — different utility names).

## Why this is tractable

The dashboard pages already use **shadcn-style utility classes** (`bg-card`,
`text-muted-foreground`, `border-border`, `text-primary`, …) and `cn()` already
exists (`src/lib/utils.ts`). The visual identity is driven entirely by **CSS
theme tokens** in `src/index.css`. So:

- **The redesign = the theme.** Rewriting the tokens restyles all 18 pages at
  once. ✅ Done (Phase 0): Cloud Industry dark — deep blue-slate canvas
  (`#0b1220`), cloud off-white text (`#e8eef5`), cyan brand accent (`#38bdf8`)
  on the `primary`/`ring`/active slots; cyan-tinted `accent` hover surfaces.
- **The "rebuild on shadcn" = swapping component imports**, page by page, from
  `@nous-research/ui/ui/components/*` to `@/components/ui/*`. Mechanical.

## Cloud Industry palette (Phase 0, shipped)

| Token | Value | Role |
|---|---|---|
| `--background-base` | `#0b1220` | canvas (industry: solid dark slate) |
| `--midground-base` | `#e8eef5` | foreground / cloud off-white text |
| `--brand-base` | `#38bdf8` | cloud sky-cyan — `primary`, `ring`, active |
| `--brand-foreground` | `#05131f` | text on cyan |
| `--color-success` | `#34d399` | success / "run" |
| `--color-warning` | `#fbbf24` | warning |
| `--color-destructive` | `#fb2c36` | danger |

Swap the brand color anytime by editing `--brand-base` (and `--background-base` /
`--midground-base`) in `src/index.css`. The whole app follows.

## Component map (`@nous-research/ui` → `@/components/ui`)

| nous-research/ui | shadcn (`@/components/ui/*`) | status |
|---|---|---|
| `button` (`ghost`, `outlined`, `destructive` flags) | `button` (`variant=`/`size=`) | ✅ added |
| `card` (`Card`, `CardContent`) | `card` (full set) | ✅ added |
| `badge` (`tone=`) | `badge` (`variant=`) | ✅ added |
| `input` | `input` | todo |
| `spinner` | `spinner` (or a `Loader2` spin) | todo |
| `typography/h2` etc. | plain `<h2 className=…>` | todo |
| `selection-switcher`, `segmented` | `tabs` / `toggle-group` | todo |
| dialogs/modals | `dialog` (needs `@radix-ui/react-dialog`) | todo |

Note: the new shadcn primitives are **self-contained** (cva + `cn`, no
`@radix-ui/react-slot`) so they need no new deps. Radix-backed primitives
(dialog, dropdown, tabs) are added when their pages are migrated — install the
specific `@radix-ui/*` package then.

## Per-page migration order (do one at a time; build after each)

1. **LearningPage** — small, already shadcn-classed (good first target).
2. **SystemPage** — high-traffic; many buttons.
3. **CronPage**, **ChannelsPage**, **SkillsPage**.
4. **ModelsPage**, **AnalyticsPage**, **SessionsPage**, **LogsPage**.
5. **ConfigPage**, **EnvPage**, **McpPage**, **PluginsPage**, **ProfilesPage**,
   **WebhooksPage**, **PairingPage**, **DocsPage**.
6. Shared components (`AuthWidget`, `PlatformsCard`, `ModelInfoCard`, sidebar, …).
7. **Final:** remove `@nous-research/ui` from `package.json` + its CSS imports in
   `index.css` once no file imports it (`grep -rl "@nous-research/ui" web/src`).

## Per-page recipe

1. Replace `import { Button } from "@nous-research/ui/ui/components/button"` →
   `import { Button } from "@/components/ui/button"`.
2. Translate props: nous `ghost` → shadcn `variant="ghost"`; nous `outlined` →
   `variant="outline"`; nous `<Badge tone="success">` → `<Badge variant="success">`.
   (`size=` is the same on both Buttons.)
3. `npm run build` (tsc + vite). Fix any prop mismatches.
4. Commit that page.

## Verify

- `cd web && npm run build` after every change — must stay green.
- `grep -rl "@nous-research/ui" web/src | wc -l` trends to 0 as pages migrate.

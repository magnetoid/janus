# Dashboard redesign — Phase 1: shadcn foundation + drop @nous-research/ui

> Date: 2026-06-24 · Status: approved, implementing · Scope: `web/` (React 19 +
> Vite + Tailwind 4 dashboard). Phase 2+ (per-page redesign) is separate.

## Goal
Establish the shadcn design foundation and fully remove `@nous-research/ui`. After
Phase 1: the app is shadcn end-to-end (refined-minimal "new-york" style, light +
dark via the existing theme system, one Cloud Industry accent), `npm run build` +
`npm run lint` pass, and all 18 pages still render. No page redesign yet.

## Current state
- 18 pages; modern stack (React 19, Vite 7, Tailwind 4, react-router 7).
- shadcn deps already present (Radix primitives, cva, tailwind-merge, lucide).
- 10 shadcn components exist: button, card, input, badge, checkbox, label,
  separator, spinner, switch, textarea.
- `@nous-research/ui@0.18.2` still supplies ~30 exports across ~8 files.

## Components to build (`src/components/ui/`, shadcn new-york style)
Radix-backed: `select`, `tabs`, `dialog` + `confirm-dialog`, `toast` + `use-toast`,
`segmented` (toggle-group), `sheet`/`bottom-sheet`.
Composed: `typography` (H2 …), `stats`, `list-item`, `filter-group`,
`command-block` (code + copy), `copy-button`.
Hooks/util: `useToast`, `useBelowBreakpoint` (matchMedia), `useConfirmDelete`
(dialog-driven), `useGpuTier` + `fillerBgUrl` (ported as-is — they drive the 3D
background, which stays for now).

Each component is self-contained: `cva` variants + `forwardRef` + the `cn()` util,
matching the existing shadcn files' conventions and the `@/` path alias.

## Design tokens
shadcn CSS variables (`--background`, `--foreground`, `--card`, `--primary`,
`--muted`, `--border`, `--ring`, `--radius`, …) for light + dark, wired into the
existing `src/themes` presets, Cloud Industry accent as `--primary`. No hard-coded
colors in components — tokens only.

## Compat shim
`src/lib/nous-ui.ts` (or `.tsx`) re-exports the shadcn components under the
`@nous-research/ui` export names, ADAPTING API differences (e.g. a wrapper mapping
nous's single-element `<Tabs items=…>` to shadcn's compound
`<Tabs/TabsList/TabsTrigger/TabsContent>`; `<Select>` likewise). Swap the ~8 files'
import path `@nous-research/ui` → the shim, then delete the dep from `package.json`
and `vite.config.ts`. Phase 2 inlines native shadcn per page and shrinks the shim.

## Decisions (approved)
- Compat-shim intermediate (drop the dep fast; native-shadcn migration is Phase 2).
- Keep the 3D background (react-three-fiber + `useGpuTier`) as-is.

## Testing / acceptance
`npm run build` (tsc typecheck + vite build) passes; `npm run lint` passes; every
page renders (smoke). Add a minimal vitest render-smoke for the new components only
if it's clean to set up; otherwise rely on build + lint. No behavior/route changes.

## YAGNI (Phase 1)
No page redesigns; no components beyond those imported; 3D background untouched; no
new routes or features.

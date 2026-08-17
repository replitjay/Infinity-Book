# Infinity

Infinity is a mobile-first free-to-play cricket and social gaming web app for India, with live score discovery, casual games, free prediction contests, virtual coins, leaderboards, and responsible-play controls.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `artifacts/infinity-web/src/App.tsx` — web app routes, mock product data, and interactive UI
- `artifacts/infinity-web/src/index.css` — Infinity visual system, responsive styles, motion, and accessibility states
- `attached_assets/Infinity_Book_Website_Design_Specification_1786978376654.pdf` — original design and development specification
- `attached_assets/Pasted-I-am-building-a-full-stack-web-application-called-Infin_1786978384159.txt` — initial technical brief and Phase 1 requirements

## Architecture decisions

- The first milestone is a frontend-only web experience with realistic mock data so the product surface can be reviewed before connecting live services.
- The app uses route-aware shared navigation with mobile bottom tabs and a desktop sidebar.
- Virtual coin language is intentionally separated from cash language; the first milestone includes no withdrawal or rupee-equivalent flows.

## Product

- Homepage with live match discovery, free-play CTAs, quick links, and game previews
- Live scores hub and match centre with commentary, scorecard, overs, and connection interruption state
- Games lobby with category filters and playable mock game cards
- Prediction contest hub with free join interactions
- Daily leaderboard
- Coins account with free earning routes, coin packs, and activity history
- Responsible-play controls, breaks, and self-exclusion dialog

## User preferences

- Build the web app first; native mobile app work is not part of this milestone.

## Gotchas

- Keep the compliance statement “100% free to play. No deposits. No cash prizes.” visible on key conversion surfaces.
- Gold is reserved for coins/rewards, green for primary actions/positive states, and red/coral for live or destructive states.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details

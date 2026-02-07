# Tasks: Dashboard Complete Specifications

**Feature Branch**: `1-dashboard-complete` | **Date**: 2026-02-08 | **Plan**: [specs/1-dashboard-complete/plan.md](specs/1-dashboard-complete/plan.md)
**Input**: Implementation plan from `/specs/1-dashboard-complete/plan.md`, Feature specification from `/specs/1-dashboard-complete/spec.md`

## Summary

This document outlines the tasks required to implement the "Dashboard Complete Specifications" feature, transforming the existing AI Employee Dashboard into a real-time, dynamic monitoring and management interface. Tasks are organized into phases, prioritizing foundational elements and user stories to enable incremental delivery and independent testing.

## Phase 1: Setup

**Goal**: Establish the basic project structure for new backend APIs and frontend UI components.

-   [ ] T001 Create backend API directory structure for new routes in `backend/src/api/` (implicitly `/dashboard/app/api/`).
-   [ ] T002 Create backend utility directory for file system access helpers in `backend/src/utils/`.
-   [ ] T003 Create backend services directory for interfacing with PM2 and other services in `backend/src/services/`.
-   [ ] T004 Create frontend component directories for new dashboard widgets in `frontend/src/components/dashboard/`.
-   [ ] T005 Create frontend component directories for analytics components in `frontend/src/components/analytics/`.
-   [ ] T006 Create frontend component directories for integrations components in `frontend/src/components/integrations/`.
-   [ ] T007 Create frontend component directories for workflows components in `frontend/src/components/workflows/`.
-   [ ] T008 Create frontend page directories for new analytics, integrations, and workflows pages in `frontend/src/pages/`.
-   [ ] T009 Create frontend hooks directory for new React hooks in `frontend/src/hooks/`.

## Phase 2: Foundational

**Goal**: Implement a core file system access utility to support data retrieval from the Vault.

-   [ ] T010 Implement `vault-file-access.ts` utility to read and count markdown files from `AI_Employee_Vault`, handle Windows path separators, and gracefully manage missing folders in `backend/src/utils/vault-file-access.ts`.

## Phase 3: User Story 1 - Real-time Dashboard Data [US1]

**Goal**: Transform the main dashboard to display real-time data for CEO Briefing, Revenue Analytics, Bottleneck Detection, and Vault Statistics.

-   [ ] T011 [P] [US1] Implement `/api/vault` endpoint to return vault folder statistics in `backend/src/api/vault/route.ts`.
    -   **FR-004.1**: Return JSON including `folderStats`, `vaultPath`, and `timestamp`.
    -   **FR-004.2**: Resolve vault path using `path.join(process.cwd(), '..', 'AI_Employee_Vault')`.
    -   **FR-004.3**: Count only `.md` files, excluding `.canvas` and `.json`.
    -   **FR-004.4**: Handle non-existent folders gracefully.
    -   **FR-004.5**: Log path and counts.
    -   **FR-004.6**: Return zeros if vault not found.
-   [ ] T012 [P] [US1] Implement `/api/ceo-briefing` endpoint to generate real-time CEO briefing data in `backend/src/api/ceo-briefing/route.ts`.
    -   **FR-001.1**: Return JSON with date, revenue, expenses, net profit, bottlenecks, task completion, last generated, and vault stats.
    -   **FR-001.2**: Count `.md` files in specified vault folders.
    -   **FR-001.3**: Apply bottleneck rules for `Needs_Action`, `Pending_Approval`, `EMAIL_*`.
    -   **FR-001.4**: Calculate revenue based on completed tasks, mock expenses.
    -   **FR-001.5**: Handle Windows path separators, filter `.md`.
    -   **FR-001.6**: Handle missing folders gracefully.
    -   **FR-001.7**: Log errors.
-   [ ] T013 [P] [US1] Implement `/api/revenue` endpoint to calculate revenue metrics in `backend/src/api/revenue/route.ts`.
    -   **FR-002.1**: Return JSON with today, week, month revenue, growth, trend, and sources.
    -   **FR-002.2**: Calculate today's revenue from `Done` folder.
    -   **FR-002.3**: Estimate week/month revenue.
    -   **FR-002.4**: Generate random growth and simulated trend.
-   [ ] T014 [P] [US1] Implement `/api/bottlenecks` endpoint to detect workflow bottlenecks in `backend/src/api/bottlenecks/route.ts`.
    -   **FR-003.1**: Return JSON with an array of bottlenecks, total active, resolved.
    -   **FR-003.2**: Detect bottlenecks based on `Needs_Action`, `Pending_Approval`, `EMAIL_*` files.
    -   **FR-003.3**: Count files by prefix in `Needs_Action`.
-   [ ] T015 [US1] Create `DashboardVaultStats` widget component to display vault statistics from `/api/vault` in `frontend/src/components/dashboard/DashboardVaultStats.tsx`.
-   [ ] T016 [US1] Create `DashboardCEOBriefing` widget component to display CEO briefing from `/api/ceo-briefing` in `frontend/src/components/dashboard/DashboardCEOBriefing.tsx`.
-   [ ] T017 [US1] Create `DashboardRevenueAnalytics` widget component to display revenue analytics from `/api/revenue` in `frontend/src/components/dashboard/DashboardRevenueAnalytics.tsx`.
-   [ ] T018 [US1] Create `DashboardBottleneckDetector` widget component to display bottleneck detection from `/api/bottlenecks` in `frontend/src/components/dashboard/DashboardBottleneckDetector.tsx`.
-   [ ] T019 [US1] Integrate `DashboardVaultStats`, `DashboardCEOBriefing`, `DashboardRevenueAnalytics`, `DashboardBottleneckDetector` into the main dashboard page in `frontend/src/pages/dashboard/index.tsx` (assuming existing dashboard page).
-   [ ] T020 [US1] Implement auto-refresh logic (e.g., React hook) for CEO Briefing widget (30-second interval) in `frontend/src/hooks/useCeoBriefingRefresh.ts`.

## Phase 4: User Story 5 - Dynamic Navbar Updates [US5]

**Goal**: Update the navigation bar to display real-time PM2 service counts and system health.

-   [ ] T021 [P] [US5] Implement `/api/pm2` endpoint to fetch PM2 process data in `backend/src/api/pm2/route.ts`.
-   [ ] T022 [US5] Update `navbar.tsx` to integrate PM2 data from `/api/pm2` and display online/total services and system health percentage in `frontend/src/components/navbar.tsx`.
-   [ ] T023 [US5] Implement auto-refresh logic (e.g., React hook) for PM2 data in navbar (5-second interval) in `frontend/src/hooks/usePm2DataRefresh.ts`.

## Phase 5: User Story 2 - Analytics Page Functionality [US2]

**Goal**: Build a new Analytics page with various charts and metrics.

-   [ ] T024 [P] [US2] Implement `/api/analytics` endpoint to provide data for the analytics page in `backend/src/api/analytics/route.ts`.
-   [ ] T025 [P] [US2] Create `TaskPerformanceChart` component (using recharts) in `frontend/src/components/analytics/TaskPerformanceChart.tsx`.
-   [ ] T026 [P] [US2] Create `EmailActivityStats` component in `frontend/src/components/analytics/EmailActivityStats.tsx`.
-   [ ] T027 [P] [US2] Create `SocialMediaAnalytics` component in `frontend/src/components/analytics/SocialMediaAnalytics.tsx`.
-   [ ] T028 [P] [US2] Create `ActivityHeatmap` component in `frontend/src/components/analytics/ActivityHeatmap.tsx`.
-   [ ] T029 [P] [US2] Create `FileTypeBreakdown` component in `frontend/src/components/analytics/FileTypeBreakdown.tsx`.
-   [ ] T030 [P] [US2] Create `FolderDistribution` component in `frontend/src/components/analytics/FolderDistribution.tsx`.
-   [ ] T031 [US2] Create `analytics/page.tsx` and integrate all analytics components, fetching data from `/api/analytics` in `frontend/src/pages/analytics/page.tsx`.
-   [ ] T032 [US2] Implement auto-refresh logic (e.g., React hook) for analytics page data (10-second interval) in `frontend/src/hooks/useAnalyticsDataRefresh.ts`.

## Phase 6: User Story 3 - Integrations Page Functionality [US3]

**Goal**: Build a new Integrations page to manage and monitor integrations.

-   [ ] T033 [P] [US3] Implement `/api/integrations/status` endpoint to fetch MCP server status and health checks in `backend/src/api/integrations/status/route.ts`.
-   [ ] T034 [P] [US3] Create `MCPServerGrid` component in `frontend/src/components/integrations/MCPServerGrid.tsx`.
-   [ ] T035 [P] [US3] Create `HealthCheckList` component in `frontend/src/components/integrations/HealthCheckList.tsx`.
-   [ ] T036 [P] [US3] Create `ActivityTimeline` component in `frontend/src/components/integrations/ActivityTimeline.tsx`.
-   [ ] T037 [US3] Create `integrations/page.tsx` and integrate all integrations components, fetching data from `/api/integrations/status` in `frontend/src/pages/integrations/page.tsx`.

## Phase 7: User Story 4 - Workflows Page Functionality [US4]

**Goal**: Build a new Workflows page for workflow management.

-   [ ] T038 [P] [US4] Implement `/api/workflows` endpoint to fetch workflow details and performance metrics in `backend/src/api/workflows/route.ts`.
-   [ ] T039 [P] [US4] Create `WorkflowList` component in `frontend/src/components/workflows/WorkflowList.tsx`.
-   [ ] T040 [P] [US4] Create `WorkflowCard` component in `frontend/src/components/workflows/WorkflowCard.tsx`.
-   [ ] T041 [P] [US4] Create `PerformanceMetrics` component in `frontend/src/components/workflows/PerformanceMetrics.tsx`.
-   [ ] T042 [US4] Create `workflows/page.tsx` and integrate all workflows components, fetching data from `/api/workflows` in `frontend/src/pages/workflows/page.tsx`.

## Phase 8: Polish & Cross-Cutting Concerns

**Goal**: Ensure theme consistency, responsiveness, auto-refresh functionality, and overall quality.

-   [ ] T043 Ensure all new UI components and pages adhere to the black/green design system (`bg-primary`, `bg-card`, etc.) across `frontend/src/components/` and `frontend/src/pages/`.
-   [ ] T044 Verify mobile responsiveness for all new pages (`analytics/page.tsx`, `integrations/page.tsx`, `workflows/page.tsx`) and existing dashboard widgets.
-   [ ] T045 Implement necessary error handling and logging in all new API routes (`backend/src/api/`).
-   [ ] T046 Update navbar links (Analytics, Integrations, Workflows) to point to the newly created pages in `frontend/src/components/navbar.tsx`.
-   [ ] T047 Perform end-to-end testing of all new features, verifying data accuracy and auto-refresh functionality.

## Dependencies

-   Phase 1 (Setup) must be completed before any other phase.
-   Phase 2 (Foundational) must be completed before Phase 3 (User Story 1).
-   User Story phases (Phase 3 to 7) can be developed largely in parallel, but Phase 3 (Real-time Dashboard Data) is foundational for other dashboard-related P1 stories.
-   Phase 8 (Polish & Cross-Cutting Concerns) depends on the completion of all other phases.

## Parallel Execution Examples

-   **Backend API Development (Phase 3, 4, 5, 6, 7 APIs)**: Multiple developers can work on different API endpoints (e.g., `/api/vault`, `/api/ceo-briefing`, `/api/pm2`, `/api/analytics`, `/api/integrations/status`, `/api/workflows`) concurrently, assuming clear API contracts.
-   **Frontend Component Development (Phase 3, 5, 6, 7 Components)**: Once API contracts are stable, frontend developers can build UI components for different pages (e.g., `DashboardCEOBriefing`, `TaskPerformanceChart`, `MCPServerGrid`, `WorkflowList`) in parallel.
-   **Hook Development (Phase 3, 4, 5 Hooks)**: React hooks for data fetching and auto-refresh can be developed independently for different parts of the dashboard.

## Implementation Strategy

The implementation will follow an MVP-first approach, focusing on delivering User Story 1 (Real-time Dashboard Data) and User Story 5 (Dynamic Navbar Updates) as the initial high-priority increments, followed by the new pages. This allows for early validation of critical real-time data functionality. Incremental delivery will ensure that each functional piece is tested and integrated before moving to the next.

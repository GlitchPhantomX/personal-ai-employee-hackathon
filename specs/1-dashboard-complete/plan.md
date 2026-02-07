# Implementation Plan: Dashboard Complete Specifications

**Branch**: `1-dashboard-complete` | **Date**: 2026-02-08 | **Spec**: [specs/1-dashboard-complete/spec.md](specs/1-dashboard-complete/spec.md)
**Input**: Feature specification from `/specs/1-dashboard-complete/spec.md`

## Summary

This plan outlines the implementation of the "Dashboard Complete Specifications" feature, which aims to transform the existing AI Employee Dashboard from displaying static mock data to real-time, dynamic information. This includes fixing all API routes to pull data from the vault and system services, building new Analytics, Integrations, and Workflows pages, and dynamically updating the navigation bar. The technical approach leverages the existing Next.js/React frontend with new API routes for data retrieval and adheres to the specified black/green design system.

## Technical Context

**Language/Version**: JavaScript/TypeScript (Next.js, React) and Python (for existing PM2 services and potential MCP servers)  
**Primary Dependencies**: React, Next.js, recharts (for charting), file system access libraries (e.g., `fs` module for Node.js APIs)  
**Storage**: Local file system (Obsidian Vault for markdown files)  
**Testing**: NEEDS CLARIFICATION (No specific testing framework identified in the existing project, though unit/integration tests will be required for new APIs and components)  
**Target Platform**: Web browser  
**Project Type**: Web application  
**Performance Goals**:
-   All critical API routes (`/api/ceo-briefing`, `/api/revenue`, `/api/bottlenecks`, `/api/vault`) return real data within 1 second on average.
-   Main dashboard CEO Briefing widget updates every 30 seconds.
-   Analytics page auto-refreshes every 10 seconds.
-   Navbar PM2 service counts and system health percentage update every 5 seconds.
**Constraints**:
-   DO NOT delete any existing files or folders.
-   DO NOT change the main dashboard layout.
-   DO NOT modify backend database models (as there are none explicitly defined).
-   DO NOT remove any existing components.
-   DO NOT change the color theme.
-   DO NOT break existing functionality.
-   Must handle Windows path separators.
-   Must filter only `.md` files in vault operations.
-   Must handle missing vault folders gracefully.
-   Must log errors to console for debugging.
**Scale/Scope**: Dashboard for a single Personal AI Employee, monitoring its activities, integrations, and workflows, displaying real-time operational data.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Section 1.1: Core Mission**
-   **Check**: Does this feature support automating personal/business affairs, local-first architecture, human oversight, 24/7 autonomous assistance, and democratizing AI automation?
-   **Evaluation**: YES. By providing a comprehensive dashboard, this feature enhances human oversight, facilitates monitoring of autonomous operations, and provides the necessary UI for managing the AI employee.

**Section 2.1: The Five-Layer Architecture**
-   **Check**: Does the implementation conform to the five-layer architecture (Perception, Memory, Reasoning, Action, Orchestration)?
-   **Evaluation**: YES. The APIs being built directly interface with the Memory layer (Obsidian Vault for data sources) and provide data for the Orchestration layer (PM2 monitoring) and Action layer (MCP server status). The dashboard itself is a visualization tool for these layers.

**Section 2.2: Technology Stack Requirements**
-   **Check**: Does the plan adhere to the mandatory technology stack (Claude Code, Obsidian v1.10.6+, Python 3.13+, Node.js v24+, Git)?
-   **Evaluation**: YES. The frontend is built with Node.js (Next.js/React), and APIs will leverage Node.js. Python is implicitly used for existing PM2 services. Obsidian is the data source.

**Section 5.1: Reliability Requirements**
-   **Check**: Are reliability requirements addressed (uptime, failure handling, health checks)?
-   **Evaluation**: YES. The performance goals include auto-refresh mechanisms and graceful error handling (e.g., "return zeros if vault not found (don't crash)"). The dashboard's role is to visualize health, contributing to reliability monitoring.

**Section 6.1: Access Control**
-   **Check**: Does the plan consider credential management and authentication?
-   **Evaluation**: NEEDS CLARIFICATION. While the spec focuses on displaying data, new APIs will need to consider authentication/authorization if they are to be exposed beyond local access or if sensitive data is involved. For now, it's assumed APIs are local-only, but this should be explicitly confirmed or addressed.

**Section 6.4: Third-Party Risk**
-   **Check**: Are third-party integrations (e.g., Xero) reviewed for risk?
-   **Evaluation**: YES. The Integrations page explicitly monitors MCP server status, implying an awareness of external service health. The revenue API includes Xero as a future data source, indicating a need for its consideration.

**Section 7.3: Gold Tier (Autonomous Employee)**
-   **Check**: Does this feature contribute to the Gold Tier requirements (cross-domain integration, Xero integration, CEO Briefing, Dashboard UI)?
-   **Evaluation**: YES. This feature directly implements the Dashboard UI, CEO Briefing, and sets up APIs for cross-domain data, fulfilling significant aspects of the Gold Tier.

## Project Structure

### Documentation (this feature)

```text
specs/1-dashboard-complete/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/ (implicitly Next.js API routes under /dashboard/app/api)
├── src/
│   ├── api/ (new API routes for ceo-briefing, revenue, bottlenecks, vault, analytics, integrations, workflows)
│   ├── utils/ (new utility functions for file system access, data calculations)
│   └── services/ (for interfacing with PM2, other external services if needed)
└── tests/ (for API unit/integration tests)

frontend/ (implicitly Next.js pages and components under /dashboard/app)
├── src/
│   ├── components/
│   │   ├── ui/ (existing UI components)
│   │   ├── dashboard/ (new widgets: CEO Briefing, Revenue Analytics, Bottleneck Detector, Vault Stats)
│   │   ├── analytics/ (new components: TaskPerformanceChart, EmailActivityStats, SocialMediaAnalytics, ActivityHeatmap, FileTypeBreakdown, FolderDistribution)
│   │   ├── integrations/ (new components: MCPServerGrid, HealthCheckList, ActivityTimeline)
│   │   └── workflows/ (new components: WorkflowList, WorkflowCard, PerformanceMetrics)
│   ├── pages/
│   │   ├── analytics/ (new page)
│   │   ├── integrations/ (new page)
│   │   └── workflows/ (new page)
│   └── hooks/ (new React hooks for data fetching and auto-refresh)
└── tests/ (for component and page tests)

```

**Structure Decision**: The project will follow a web application structure, leveraging Next.js's integrated API routes (`backend`) and page/component (`frontend`) architecture within the existing `/dashboard` directory. New API routes will be created under `/dashboard/app/api/` and new pages/components under `/dashboard/app/`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| (None identified at this stage) | | |
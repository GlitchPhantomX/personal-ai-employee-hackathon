# Feature Specification: Dashboard Complete Specifications

**Feature Branch**: `1-dashboard-complete`  
**Created**: 2026-02-08  
**Status**: Draft  
**Input**: User description: "# 🎯 **PERSONAL AI EMPLOYEE DASHBOARD - COMPLETE SPECIFICATIONS** **Project:** Personal AI Employee Hackathon 0 **Status:** 95% Complete → Target: 100% Gold Tier **Theme:** Black (#000000) + Green (#22C55E, #10B981) Professional --- ## 📊 **CURRENT STATE ANALYSIS** ### ✅ **Already Implemented (Working)** ``` ✓ Main Dashboard page with KPI cards ✓ CEO Briefing Widget (static data) ✓ Revenue Analytics Widget (static data) ✓ Bottleneck Detector Widget (static data) ✓ Vault Statistics display ✓ PM2 Services monitoring ✓ Live Activity Feed (SSE) ✓ CPU/Memory charts ✓ Integration widgets (Twitter, Email, Facebook, etc.) ✓ Navbar with time display ``` ### ⚠️ **Needs Implementation (Missing/Incomplete)** ``` ✗ Navbar links (Analytics, Integrations, Workflows) - non-functional ✗ Analytics page - empty/basic ✗ Integrations page - needs dynamic data ✗ Workflows page - needs builder integration ✗ All widgets showing mock data (not real vault data) ✗ CEO Briefing API missing ✗ Revenue API missing ✗ Bottleneck API missing ``` --- ## 🎯 **IMPLEMENTATION PLAN - 4 MAJOR TASKS** --- ## **TASK 1: FIX ALL API ROUTES (Dynamic Data)** **Priority:** CRITICAL 🔴 **Estimated Time:** 2-3 hours ### **Sub-task 1.1: Create CEO Briefing API** **File:** `/dashboard/app/api/ceo-briefing/route.ts` **Specifications:** ```typescript PURPOSE: Generate real-time CEO briefing from vault data INPUT: None (reads from vault filesystem) OUTPUT: JSON { date: string, // Current date revenue: number, // Calculated from Done tasks expenses: number, // Mock or from Xero later netProfit: number, // revenue - expenses bottlenecks: Array<{ task: string, impact: 'high' | 'medium' | 'low' }>, taskCompletion: number, // Percentage (done+approved) / total lastGenerated: string, // ISO timestamp vaultStats: { needsAction: number, // Count from Needs_Action folder pendingApproval: number, // Count from Pending_Approval approved: number, // Count from Approved done: number // Count from Done } } DATA SOURCE: - Count .md files in: Needs_Action, Pending_Approval, Approved, Done - Path: ../AI_Employee_Vault/[folder] BOTTLENECK RULES: - If Needs_Action > 30 → HIGH priority bottleneck - If Pending_Approval > 15 → MEDIUM priority - If email files (EMAIL_*) > 20 → HIGH priority REVENUE CALCULATION: - Each completed task = $50 value - Revenue = (Approved + Done) * $50 - Expenses = Revenue * 0.5 (mock) ``` **Critical Requirements:** - ✅ Must handle Windows path separators - ✅ Must filter only .md files - ✅ Must handle missing folders gracefully - ✅ Must log errors to console - ❌ Do NOT modify existing vault files - ❌ Do NOT delete any folders --- ### **Sub-task 1.2: Create Revenue Analytics API** **File:** `/dashboard/app/api/revenue/route.ts` **Specifications:** ```typescript PURPOSE: Calculate revenue metrics from completed tasks OUTPUT: JSON { today: number, // Revenue for today week: number, // Revenue this week month: number, // Revenue this month growth: number, // % growth vs last period trend: Array<{ day: string, // Mon, Tue, Wed... amount: number // Daily revenue }>, sources: { automation: number, // 45% of total social: number, // 35% of total consulting: number // 20% of total } } CALCULATION LOGIC: - Base value per task = $50 - Today = (Done folder count today) * $50 - Week = Today * 7 (estimated) - Month = Week * 4 - Growth = random 15-30% for demo - Trend = Generate last 7 days with variance DATA SOURCE: - Done folder file count - Timestamps from file modification dates (future enhancement) ``` --- ### **Sub-task 1.3: Create Bottleneck Detection API** **File:** `/dashboard/app/api/bottlenecks/route.ts` **Specifications:** ```typescript PURPOSE: Detect workflow bottlenecks from vault analysis OUTPUT: JSON { bottlenecks: Array<{ id: string, // Unique ID name: string, // Bottleneck description severity: 'high' | 'medium' | 'low', area: string, // Communication, Finance, etc. detectedAt: string, // ISO timestamp suggestedAction: string, impact: string // Description of impact }>, totalActive: number, resolved24h: number // Mock for now } DETECTION RULES: 1. Needs_Action > 30 files: - Severity: HIGH - Name: "Email Response Backlog" - Area: "Communication" - Impact: "{count} items requiring attention" 2. Pending_Approval > 15 files: - Severity: MEDIUM - Name: "Approval Queue Buildup" - Area: "Workflow" - Impact: "{count} items pending approval" 3. EMAIL_ files > 20: - Severity: HIGH/MEDIUM (based on count) - Name: "Unprocessed Emails" - Area: "Email" - Impact: "{count} emails awaiting processing" DATA SOURCE: - Read all folders in Needs_Action - Count files by prefix (EMAIL_, FILE_, LINKEDIN_) ``` --- ### **Sub-task 1.4: Fix Vault API** **File:** `/dashboard/app/api/vault/route.ts` **Current Status:** Returning zeros **Issue:** Path resolution or file counting **Fix Specifications:** ```typescript PURPOSE: Count files in vault folders for statistics OUTPUT: JSON { folderStats: { Needs_Action: number, Pending_Approval: number, Approved: number, Rejected: number, Done: number }, vaultPath: string, // Debug: show actual path used timestamp: string } PATH RESOLUTION (Windows): const vaultPath = path.join(process.cwd(), '..', 'AI_Employee_Vault'); FILE COUNTING: - Only count files ending with .md - Exclude .canvas, .json files - Handle folders that don't exist (return 0) ERROR HANDLING: - Log path being checked - Log file counts for each folder - Return zeros if vault not found (don't crash) ``` **Testing Checklist:** - [ ] API returns correct file counts - [ ] Logs show actual vault path - [ ] Dashboard displays real numbers - [ ] Auto-refresh works (5-second interval) --- ## **TASK 2: BUILD ANALYTICS PAGE** **Priority:** HIGH 🟡 **Estimated Time:** 3-4 hours **File:** `/dashboard/app/analytics/page.tsx` ### **Specifications:** **Page Layout:** ``` ┌─────────────────────────────────────────┐ │ ANALYTICS DASHBOARD │ ├─────────────────────────────────────────┤ │ ┌─────────┐ ┌─────────┐ ┌─────────┐ │ │ │Task Perf│ │Email │ │Social │ │ │ │ Over │ │Activity │ │Media │ │ │ │ Time │ │ Stats │ │Analytics│ │ │ └─────────┘ └─────────┘ └─────────┘ │ ├─────────────────────────────────────────┤ │ ┌──────────────────────────────────┐ │ │ │ Hourly Activity Heatmap │ │ │ │ (24hr x 7 days) │ │ │ └──────────────────────────────────┘ │ ├─────────────────────────────────────────┤ │ ┌─────────────┐ ┌──────────────────┐ │ │ │Top File │ │Folder Activity │ │ │ │Types │ │Distribution │ │ │ │(EMAIL, FILE)│ │(Pie Chart) │ │ │ └─────────────┘ └──────────────────┘ │ └─────────────────────────────────────────┘ ``` **Components Needed:** 1. **TaskPerformanceChart** - Line chart showing task completion over time 2. **EmailActivityStats** - Email processing metrics 3. **SocialMediaAnalytics** - LinkedIn/Twitter post stats 4. **ActivityHeatmap** - When tasks are created/completed 5. **FileTypeBreakdown** - Bar chart of EMAIL_ vs FILE_ vs LINKEDIN_ 6. **FolderDistribution** - Pie chart of vault folders **Data Sources:** ```typescript // Create new API: /api/analytics OUTPUT: { taskPerformance: { dates: string[], completed: number[], pending: number[] }, emailActivity: { processed: number, pending: number, avgResponseTime: string }, socialMedia: { linkedinPosts: number, twitterPosts: number, engagement: number }, fileTypes: { EMAIL: number, FILE: number, LINKEDIN: number }, activityHeatmap: Array<{ hour: number, day: string, count: number }> } ``` **Theme Requirements:** - Background: `bg-black` - Cards: `bg-white/5 border-white/10` - Charts: Green gradients (`#22C55E` to `#10B981`) - Text: `text-white` / `text-white/60` - Hover: `hover:border-white/20` **Critical Requirements:** - ✅ Must use existing chart library (recharts) - ✅ Must be responsive (mobile-friendly) - ✅ Must auto-refresh every 10 seconds - ❌ Do NOT change main dashboard layout - ❌ Do NOT modify existing components --- ## **TASK 3: BUILD INTEGRATIONS PAGE** **Priority:** HIGH 🟡 **Estimated Time:** 2-3 hours **File:** `/dashboard/app/integrations/page.tsx` ### **Specifications:** **Page Layout:** ``` ┌─────────────────────────────────────────┐ │ INTEGRATIONS MANAGEMENT │ ├─────────────────────────────────────────┤ │ ┌──────────────────────────────────┐ │ │ │ MCP Servers Status │ │ │ │ ┌────┐ ┌────┐ ┌────┐ ┌────┐ │ │ │ │ │📧 │ │📅 │ │🐦 │ │💰 │ │ │ │ │ │Mail│ │Cal │ │Twtr│ │Xero│ │ │ │ │ │ ✓ │ │ ✓ │ │ ✓ │ │ ✓ │ │ │ │ │ └────┘ └────┘ └────┘ └────┘ │ │ │ └──────────────────────────────────┘ │ ├─────────────────────────────────────────┤ │ ┌──────────────────────────────────┐ │ │ │ Integration Health Checks │ │ │ │ • Gmail API: Connected ✓ │ │ │ │ • LinkedIn: Active ✓ │ │ │ │ • Twitter: Rate limited ⚠ │ │ │ │ • Xero: Synced 2m ago ✓ │ │ │ └──────────────────────────────────┘ │ ├─────────────────────────────────────────┤ │ ┌──────────────────────────────────┐ │ │ │ Recent Integration Activity │ │ │ │ • Sent 3 emails via Gmail │ │ │ │ • Posted to LinkedIn │ │ │ │ • Synced invoice to Xero │ │ │ └──────────────────────────────────┘ │ └─────────────────────────────────────────┘ ``` **Data Sources:** ```typescript // Read from: /mcp_servers/ folder structure // List all MCP servers: - email_server (Node.js) - calendar_server (Python) - twitter_server (Python) - linkedin_server (Node.js) - xero_server (Python) - discord_server (Python) - facebook_server (Python) - instagram_server (Python) // Create API: /api/integrations/status OUTPUT: { mcpServers: Array<{ name: string, type: 'nodejs' | 'python', status: 'online' | 'offline', lastActivity: string, requestCount: number }>, healthChecks: Array<{ service: string, status: 'connected' | 'disconnected' | 'rate_limited', message: string }>, recentActivity: Array<{ timestamp: string, service: string, action: string }> } ``` **Components:** 1. **MCPServerGrid** - Visual grid of all MCP servers 2. **HealthCheckList** - Status of each integration 3. **ActivityTimeline** - Recent integration activities 4. **ConnectionSettings** - Configure each integration (future) --- ## **TASK 4: BUILD WORKFLOWS PAGE** **Priority:** MEDIUM 🟢 **Estimated Time:** 4-5 hours **File:** `/dashboard/app/workflows/page.tsx` ### **Specifications:** **Page Layout:** ``` ┌─────────────────────────────────────────┐ │ WORKFLOW MANAGEMENT │ ├─────────────────────────────────────────┤ │ ┌─────────────────────────────────┐ │ │ │ Active Workflows (3) │ │ │ │ │ │ │ │ 1. Email → Auto Reply → Archive │ │ │ │ Status: Active ✓ │ │ │ │ Triggered: 23 times today │ │ │ │ │ │ │ │ 2. Invoice → Xero → Approval │ │ │ │ Status: Active ✓ │ │ │ │ Triggered: 5 times today │ │ │ │ │ │ │ │ 3. Social Post → LinkedIn │ │ │ │ Status: Paused ⏸ │ │ │ │ Last run: 2h ago │ │ │ └─────────────────────────────────┘ │ ├─────────────────────────────────────────┤ │ ┌─────────────────────────────────┐ │ │ │ Workflow Performance │ │ │ │ • Success Rate: 95% │ │ │ │ • Avg Execution: 2.3s │ │ │ │ • Failed Tasks: 2 │ │ │ └─────────────────────────────────┘ │ ├─────────────────────────────────────────┤ │ [+ Create New Workflow] │ └─────────────────────────────────────────┘ ``` **Data Sources:** ```typescript // Read from: /AI_Employee_Vault/Plans/ folder // Each .md file = one workflow plan // Create API: /api/workflows OUTPUT: { workflows: Array<{ id: string, name: string, trigger: string, // EMAIL, FILE, SCHEDULE actions: string[], status: 'active' | 'paused' | 'error', triggerCount: number, lastRun: string, successRate: number }>, performance: { totalRuns: number, successRate: number, avgExecutionTime: string, failedTasks: number } } ``` **Components:** 1. **WorkflowList** - List all active workflows 2. **WorkflowCard** - Individual workflow details 3. **PerformanceMetrics** - Overall workflow stats 4. **WorkflowBuilder** - Create new workflow (link to /workflows/builder) --- ## **TASK 5: NAVBAR DYNAMIC UPDATES** **Priority:** HIGH 🟡 **Estimated Time:** 1 hour **File:** `/dashboard/app/components/navbar.tsx` ### **Current Issues:** - Services count is hardcoded: `10/10` - System Health is static: `100%` ### **Fix Specifications:** ```typescript // Fetch real PM2 data const [services, setServices] = useState({ total: 0, online: 0 }); const [systemHealth, setSystemHealth] = useState(100); useEffect(() => { const fetchData = async () => { const pm2Res = await fetch('/api/pm2'); const pm2Data = await pm2Res.json(); const total = pm2Data.processes?.length || 0; const online = pm2Data.processes?.filter(p => p.status === 'online').length || 0; setServices({ total, online }); setSystemHealth(total > 0 ? Math.round((online / total) * 100) : 0); }; fetchData(); const interval = setInterval(fetchData, 5000); return () => clearInterval(interval); }, []); // Update JSX: <span className="text-sm font-semibold text-white"> {services.online}/{services.total} </span> <span className="text-sm font-semibold text-white"> {systemHealth}% </span> ``` --- ## 🎨 **DESIGN SYSTEM (Consistent Across All Pages)** ### **Color Palette:** ```css --bg-primary: #000000 --bg-card: rgba(255, 255, 255, 0.05) --border-default: rgba(255, 255, 255, 0.1) --border-hover: rgba(255, 255, 255, 0.2) --text-primary: #FFFFFF --text-secondary: rgba(255, 255, 255, 0.6) --text-muted: rgba(255, 255, 255, 0.4) --accent-green: #22C55E --accent-green-light: #10B981 --accent-green-dark: #059669 --chart-gradient-start: #22C55E --chart-gradient-end: #10B981 ``` ### **Component Styling Template:** ```typescript // Card className="bg-white/5 border-white/10 hover:border-white/20 transition-all" // Title className="text-white font-semibold" // Secondary Text className="text-white/60 text-sm" // Green Badge className="bg-green-500/20 text-green-400 border-green-500/30" // Chart Line stroke="#22C55E" fill="url(#greenGradient)" ``` --- ## 📋 **TESTING CHECKLIST** ### **Before Deployment:** - [ ] All API routes return real data (not mock) - [ ] Vault statistics show actual file counts - [ ] CEO Briefing updates every 30s - [ ] Revenue Analytics shows correct calculations - [ ] Bottleneck Detector identifies real issues - [ ] Analytics page loads without errors - [ ] Integrations page shows MCP server status - [ ] Workflows page displays active workflows - [ ] Navbar shows real service counts - [ ] All pages use consistent black/green theme - [ ] Mobile responsive (test at 768px width) - [ ] No console errors in browser - [ ] All charts render correctly - [ ] Auto-refresh works on all pages --- ## 🚀 **IMPLEMENTATION ORDER** ### **Phase 1: Critical Fixes (Do First)** 1. Fix vault API to return real data ✅ 2. Create CEO Briefing API ✅ 3. Create Revenue API ✅ 4. Create Bottleneck API ✅ 5. Update navbar with real PM2 data ✅ ### **Phase 2: New Pages** 6. Build Analytics page 7. Build Integrations page 8. Build Workflows page ### **Phase 3: Polish** 9. Test all auto-refresh functionality 10. Verify mobile responsiveness 11. Check theme consistency 12. Final bug fixes --- ## ⚠️ **CRITICAL RULES** **DO NOT:** - ❌ Delete any existing files or folders - ❌ Change the main dashboard layout - ❌ Modify backend database models - ❌ Remove any existing components - ❌ Change the color theme - ❌ Break existing functionality **DO:** - ✅ Create new API routes in `/dashboard/app/api/` - ✅ Create new page components - ✅ Use existing UI components from `@/components/ui/` - ✅ Follow the black/green theme strictly - ✅ Test each feature before moving to next - ✅ Add error handling in all APIs - ✅ Log errors to console for debugging do not override or remove any other code file just create a new one and create this specification in it"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Real-time Dashboard Data (Priority: P1)

The user views the main dashboard page and expects to see up-to-date, dynamic data populating all widgets, including the CEO Briefing, Revenue Analytics, Bottleneck Detector, and Vault Statistics. All mock data should be replaced with actual, derived information.

**Why this priority**: This directly addresses the core problem of the dashboard displaying static/mock data, providing immediate value and a functional overview of the AI Employee's operations.

**Independent Test**: Can be fully tested by navigating to the main dashboard page (`/dashboard`) and verifying that all widgets display non-zero, non-static, and contextually relevant data.

**Acceptance Scenarios**:

1.  **Given** the user is on the dashboard page, **When** the page loads, **Then** the CEO Briefing widget displays current date, calculated revenue, expenses, net profit, detected bottlenecks, task completion percentage, last generated timestamp, and accurate vault statistics.
2.  **Given** the user is on the dashboard page, **When** the page loads, **Then** the Revenue Analytics widget displays calculated revenue for today, this week, this month, a simulated growth percentage, a trend array, and source distribution.
3.  **Given** the user is on the dashboard page, **When** the page loads, **Then** the Bottleneck Detector widget displays an array of detected bottlenecks with severity, area, detected timestamp, suggested action, and impact, along with total active and resolved bottlenecks.
4.  **Given** the user is on the dashboard page, **When** the page loads, **Then** the Vault Statistics widget displays correct counts for `Needs_Action`, `Pending_Approval`, `Approved`, `Rejected`, and `Done` folders, along with the correct vault path and timestamp.

---

### User Story 2 - Analytics Page Functionality (Priority: P1)

The user navigates to the Analytics page and can view various charts and metrics that provide insights into task performance over time, email activity, social media engagement, and the distribution of different file types within the vault. All data presented should be dynamic and derived from the system's operations.

**Why this priority**: Provides critical insights into the AI Employee's performance and operational efficiency, enabling data-driven decision-making.

**Independent Test**: Can be fully tested by navigating to the Analytics page (`/analytics`) and verifying that all charts and statistics are rendered correctly with dynamic data, are responsive, and auto-refresh.

**Acceptance Scenarios**:

1.  **Given** the user navigates to the `/analytics` page, **When** the page loads, **Then** `TaskPerformanceChart` displays task completion over time, `EmailActivityStats` shows email processing metrics, and `SocialMediaAnalytics` presents LinkedIn/Twitter post statistics.
2.  **Given** the user is on the `/analytics` page, **When** the page loads, **Then** `ActivityHeatmap` visually represents hourly activity for 24 hours across 7 days.
3.  **Given** the user is on the `/analytics` page, **When** the page loads, **Then** `FileTypeBreakdown` shows a bar chart of `EMAIL_`, `FILE_`, and `LINKEDIN_` file counts, and `FolderDistribution` displays a pie chart of vault folder activity.
4.  **Given** the user is on the `/analytics` page, **When** the data is updated, **Then** the page auto-refreshes every 10 seconds to show the latest data, and all components maintain the black/green theme.

---

### User Story 3 - Integrations Page Functionality (Priority: P1)

The user navigates to the Integrations page and sees a comprehensive overview of all MCP (Multi-Cloud Platform) servers, their operational status, and detailed health checks for various external integrations like Gmail, LinkedIn, Twitter, and Xero. Recent activities related to these integrations are also displayed.

**Why this priority**: Essential for monitoring the health and activity of external services and ensures the AI Employee can effectively interact with other platforms.

**Independent Test**: Can be fully tested by navigating to the Integrations page (`/integrations`) and observing the displayed statuses, health checks, and activity logs.

**Acceptance Scenarios**:

1.  **Given** the user navigates to the `/integrations` page, **When** the page loads, **Then** the `MCPServerGrid` displays a visual grid of all configured MCP servers with their names, types (Node.js/Python), status (online/offline), last activity, and request counts.
2.  **Given** the user is on the `/integrations` page, **When** the page loads, **Then** the `HealthCheckList` shows the connection status for services like Gmail API, LinkedIn, Twitter, and Xero, including messages like "Connected ✓", "Active ✓", "Rate limited ⚠", or "Synced Xm ago ✓".
3.  **Given** the user is on the `/integrations` page, **When** the page loads, **Then** the `ActivityTimeline` displays a list of recent integration activities with timestamps, service names, and actions (e.g., "Sent 3 emails via Gmail", "Posted to LinkedIn", "Synced invoice to Xero").

---

### User Story 4 - Workflows Page Functionality (Priority: P2)

The user navigates to the Workflows page to view and manage active automated workflows. The page displays a list of workflows, their current status (active, paused, error), trigger information, and performance metrics such as success rates and average execution times.

**Why this priority**: Allows for management and oversight of automated processes, crucial for the AI Employee's autonomous operation.

**Independent Test**: Can be fully tested by navigating to the Workflows page (`/workflows`) and verifying the list of workflows and their associated performance metrics.

**Acceptance Scenarios**:

1.  **Given** the user navigates to the `/workflows` page, **When** the page loads, **Then** the `WorkflowList` displays all configured workflows, each represented by a `WorkflowCard` showing its ID, name, trigger, actions, status, trigger count, last run time, and success rate.
2.  **Given** the user is on the `/workflows` page, **When** the page loads, **Then** the `PerformanceMetrics` section displays overall workflow statistics including total runs, success rate, average execution time, and failed tasks.
3.  **Given** the user is on the `/workflows` page, **When** the page loads, **Then** a "Create New Workflow" option is available, linking to `/workflows/builder`.

---

### User Story 5 - Dynamic Navbar Updates (Priority: P1)

The user interacts with any page in the dashboard and observes the navigation bar (navbar) consistently displaying real-time operational metrics: the current count of online PM2 services versus total services, and the overall system health percentage.

**Why this priority**: Provides continuous, at-a-glance visibility into the system's operational status, improving user awareness and ability to quickly identify issues.

**Independent Test**: Can be fully tested by navigating between any pages of the dashboard and observing the navbar's service count and system health metrics updating dynamically and accurately.

**Acceptance Scenarios**:

1.  **Given** the user is viewing any dashboard page, **When** the navbar is visible, **Then** the service count displays the current number of online PM2 processes out of the total number of PM2 processes (e.g., "8/10").
2.  **Given** the user is viewing any dashboard page, **When** the navbar is visible, **Then** the system health displays the calculated percentage of online PM2 processes (e.g., "80%").
3.  **Given** the PM2 processes status changes, **When** 5 seconds pass, **Then** the navbar updates the service count and system health to reflect the new real-time data.

---

### Edge Cases

-   What happens when a vault folder (e.g., `Needs_Action`) is missing? The system should handle this gracefully by returning a count of 0 for that folder and not crashing.
-   How does the system handle an unresponsive or erroring external integration API (e.g., Twitter rate limits)? The Integrations page should accurately reflect the status with appropriate warnings.
-   What happens if the PM2 API is unavailable? The navbar should display default or error states without crashing.
-   How does the system handle large numbers of files in vault folders to prevent performance degradation? (Assumption: File counting mechanism will be efficient).

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The system MUST provide an API endpoint `/api/ceo-briefing` that generates real-time CEO briefing data from vault markdown files.
    -   **FR-001.1**: The API MUST return JSON containing current date, calculated revenue, expenses, net profit, detected bottlenecks, task completion percentage, last generated timestamp, and vault statistics (`needsAction`, `pendingApproval`, `approved`, `done`).
    -   **FR-001.2**: The API MUST count markdown files in `Needs_Action`, `Pending_Approval`, `Approved`, and `Done` folders within `AI_Employee_Vault`.
    -   **FR-001.3**: The API MUST apply bottleneck rules: `Needs_Action > 30` (HIGH), `Pending_Approval > 15` (MEDIUM), `EMAIL_*` files `> 20` (HIGH/MEDIUM).
    -   **FR-001.4**: The API MUST calculate revenue as `(Approved + Done) * $50`, with expenses as `Revenue * 0.5` (mock).
    -   **FR-001.5**: The API MUST handle Windows path separators and filter only `.md` files.
    -   **FR-001.6**: The API MUST gracefully handle missing vault folders by returning 0 for their counts.
    -   **FR-001.7**: The API MUST log errors to the console.
    -   **FR-001.8**: The API MUST NOT modify existing vault files or delete any folders.

-   **FR-002**: The system MUST provide an API endpoint `/api/revenue` that calculates and returns revenue metrics.
    -   **FR-002.1**: The API MUST return JSON with `today`, `week`, `month` revenue, `growth` percentage, `trend` data (last 7 days), and `sources` distribution (automation, social, consulting).
    -   **FR-002.2**: The API MUST calculate `today` revenue based on `Done` folder file count for the current day.
    -   **FR-002.3**: The API MUST estimate `week` revenue as `Today * 7` and `month` revenue as `Week * 4`.
    -   **FR-002.4**: The API MUST generate a random `growth` percentage (15-30%) and a simulated `trend` for the last 7 days.

-   **FR-003**: The system MUST provide an API endpoint `/api/bottlenecks` that detects and returns workflow bottlenecks.
    -   **FR-003.1**: The API MUST return JSON containing an array of bottlenecks (id, name, severity, area, detectedAt, suggestedAction, impact), total active, and resolved (mock) counts.
    -   **FR-003.2**: The API MUST detect bottlenecks based on `Needs_Action > 30` ("Email Response Backlog" - HIGH), `Pending_Approval > 15` ("Approval Queue Buildup" - MEDIUM), and `EMAIL_*` files `> 20` ("Unprocessed Emails" - HIGH/MEDIUM).
    -   **FR-003.3**: The API MUST count files by prefix (EMAIL_, FILE_, LINKEDIN_) in `Needs_Action` folder.

-   **FR-004**: The system MUST provide an API endpoint `/api/vault` that returns vault folder statistics.
    -   **FR-004.1**: The API MUST return JSON including `folderStats` (counts for `Needs_Action`, `Pending_Approval`, `Approved`, `Rejected`, `Done`), the `vaultPath` used, and a `timestamp`.
    -   **FR-004.2**: The API MUST resolve the vault path using `path.join(process.cwd(), '..', 'AI_Employee_Vault')`.
    -   **FR-004.3**: The API MUST count only `.md` files, excluding `.canvas` and `.json` files.
    -   **FR-004.4**: The API MUST handle non-existent folders by returning 0 for their counts.
    -   **FR-004.5**: The API MUST log the path being checked and file counts for each folder.
    -   **FR-004.6**: The API MUST return zeros and not crash if the vault is not found.

-   **FR-005**: The system MUST provide an Analytics page (`/dashboard/app/analytics/page.tsx`) with various charts and metrics.
    -   **FR-005.1**: The page MUST include `TaskPerformanceChart`, `EmailActivityStats`, `SocialMediaAnalytics`, `ActivityHeatmap`, `FileTypeBreakdown`, and `FolderDistribution` components.
    -   **FR-005.2**: The page MUST fetch data from a new `/api/analytics` endpoint, providing task performance, email activity, social media stats, file type counts, and activity heatmap data.
    -   **FR-005.3**: The page MUST use an existing chart library (recharts).
    -   **FR-005.4**: The page MUST be responsive and auto-refresh every 10 seconds.
    -   **FR-005.5**: The page MUST adhere to the black/green theme.

-   **FR-006**: The system MUST provide an Integrations page (`/dashboard/app/integrations/page.tsx`) to manage and monitor integrations.
    -   **FR-006.1**: The page MUST display `MCP Servers Status` including `MCPServerGrid`, `Integration Health Checks`, and `Recent Integration Activity` via components like `HealthCheckList` and `ActivityTimeline`.
    -   **FR-006.2**: The page MUST fetch data from a new `/api/integrations/status` endpoint, providing MCP server status, health checks, and recent activity.
    -   **FR-006.3**: The page MUST derive MCP server information from the `/mcp_servers/` folder structure.

-   **FR-007**: The system MUST provide a Workflows page (`/dashboard/app/workflows/page.tsx`) for workflow management.
    -   **FR-007.1**: The page MUST display `Active Workflows` and `Workflow Performance` via components like `WorkflowList`, `WorkflowCard`, and `PerformanceMetrics`.
    -   **FR-007.2**: The page MUST fetch data from a new `/api/workflows` endpoint, providing workflow details (id, name, trigger, actions, status, triggerCount, lastRun, successRate) and overall performance metrics.
    -   **FR-007.3**: Workflow data MUST be read from `.md` files in the `/AI_Employee_Vault/Plans/` folder.

-   **FR-008**: The system MUST dynamically update the navbar (`/dashboard/app/components/navbar.tsx`).
    -   **FR-008.1**: The navbar MUST display the current count of online PM2 services out of the total services (e.g., "online/total").
    -   **FR-008.2**: The navbar MUST display the calculated system health percentage (e.g., "100%").
    -   **FR-008.3**: The navbar MUST fetch PM2 data from an `/api/pm2` endpoint every 5 seconds and update the displayed metrics.

-   **FR-009**: All new and modified UI components MUST adhere to the specified black/green design system.
    -   **FR-009.1**: Backgrounds MUST use `--bg-primary: #000000`.
    -   **FR-009.2**: Cards MUST use `bg-white/5 border-white/10` with `hover:border-white/20`.
    -   **FR-009.3**: Charts MUST use green gradients (`#22C55E` to `#10B981`).
    -   **FR-009.4**: Primary text MUST be `#FFFFFF`, secondary text `rgba(255, 255, 255, 0.6)`.

### Key Entities *(include if feature involves data)*

-   **Vault Data**: Markdown files within the `AI_Employee_Vault` directory, categorized by folders like `Needs_Action`, `Pending_Approval`, `Approved`, `Done`, and `Rejected`. These files represent tasks, emails, and other operational documents.
-   **MCP Servers**: Node.js and Python processes managed by PM2, representing various microservices or integrations (e.g., email_server, calendar_server, twitter_server).
-   **Workflows**: Defined in markdown files within `/AI_Employee_Vault/Plans/`, each outlining a sequence of actions triggered by specific events.
-   **PM2 Processes**: Managed processes providing backend services, monitored for their online status and health.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: All critical API routes (`/api/ceo-briefing`, `/api/revenue`, `/api/bottlenecks`, `/api/vault`) return real data, not mock data, within 1 second on average.
-   **SC-002**: The main dashboard displays real-time data for all widgets, with CEO Briefing updating every 30 seconds, Revenue Analytics and Bottleneck Detector reflecting current calculations.
-   **SC-003**: The Analytics page loads without errors, displays all charts and statistics with dynamic data, and auto-refreshes every 10 seconds.
-   **SC-004**: The Integrations page accurately shows the status of all configured MCP servers and external integration health checks.
-   **SC-005**: The Workflows page correctly displays all active workflows and their performance metrics.
-   **SC-006**: The navbar consistently displays accurate, real-time PM2 service counts and system health percentage, updating every 5 seconds.
-   **SC-007**: All new and modified dashboard pages and components strictly adhere to the black/green theme.
-   **SC-008**: The dashboard is fully responsive across common device widths (e.g., 768px width for mobile).
-   **SC-009**: No console errors are observed in the browser when interacting with the dashboard.
-   **SC-010**: The system gracefully handles scenarios where vault folders are missing or external APIs are unresponsive without crashing.

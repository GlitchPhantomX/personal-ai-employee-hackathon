# Data Model: Gold Tier Autonomous Employee System

## Business Entities

### 1. CEO Briefing
**Description**: Weekly executive summary reports
**Fields**:
- `id`: String (date-based identifier in YYYY-WW format)
- `generated_at`: DateTime (generation timestamp)
- `period_start`: Date (reporting period start)
- `period_end`: Date (reporting period end)
- `executive_summary`: Text (high-level summary)
- `revenue_analysis`: Object (weekly/monthly revenue data)
- `task_completion_metrics`: Object (completed task statistics)
- `bottlenecks_identified`: Array of Objects (identified process issues)
- `cost_optimization_suggestions`: Array of Objects (cost-saving recommendations)
- `business_recommendations`: Array of Objects (strategic recommendations)
- `upcoming_deadlines`: Array of Objects (upcoming important dates)
- `social_media_highlights`: Object (performance across platforms)
- `recommended_actions`: Array of Objects (action items)

**Relationships**:
- One-to-many with underlying data sources (revenue, tasks, etc.)

**Validation Rules**:
- ID must follow YYYY-WW format
- Period must be exactly one week
- Generated timestamp must be on Monday

### 2. Invoice
**Description**: Billing documents sent to clients for completed work
**Fields**:
- `id`: String (unique sequential number in INV-YYYY-NNN format)
- `client`: String (client name/contact)
- `date`: Date (invoice date)
- `due_date`: Date (payment due date)
- `status`: Enum (Draft, Sent, Paid, Pending, Overdue, Closed)
- `items`: Array of Objects (invoice line items)
- `subtotal`: Decimal (sum of item amounts)
- `tax_amount`: Decimal (calculated tax)
- `total`: Decimal (final amount)
- `xero_id`: String (optional, reference to Xero record)
- `payment_status`: Enum (Unpaid, Partial, Paid, Overpaid)
- `sent_at`: DateTime (optional, timestamp)
- `paid_at`: DateTime (optional, timestamp)

**Relationships**:
- Many-to-one with Task (via related_task_id)
- One-to-many with Payment (via payments array)

**Validation Rules**:
- ID must follow INV-YYYY-NNN format
- Date must not be in the future
- Amounts must be positive decimals
- Status transitions must follow defined lifecycle

### 3. Social Media Content
**Description**: Posts, campaigns, and engagement metrics
**Fields**:
- `id`: String (platform-specific unique identifier)
- `platform`: Enum (Facebook, Instagram, Twitter, LinkedIn)
- `content`: Text (post content)
- `media_urls`: Array of Strings (optional, media attachments)
- `scheduled_time`: DateTime (when to post)
- `status`: Enum (Scheduled, Published, Engaged, Metrics Collected)
- `published_at`: DateTime (optional, timestamp)
- `engagement_metrics`: Object (likes, shares, comments, reach)
- `author`: String (optional, original author)
- `hashtags`: Array of Strings (optional)
- `campaign_tag`: String (optional, campaign grouping)

**Relationships**:
- One-to-many with Engagement Metric records
- Many-to-one with Content Calendar (via calendar_reference)

**Validation Rules**:
- Content length varies by platform
- Scheduled time must be in the future
- Status transitions must follow defined lifecycle

### 4. Bottleneck
**Description**: Process inefficiencies requiring attention
**Fields**:
- `id`: String (unique tracking identifier)
- `task_reference`: String (reference to related task)
- `description`: Text (what the bottleneck is)
- `expected_duration`: Integer (estimated time in hours)
- `actual_duration`: Integer (actual time taken in hours)
- `delay_hours`: Integer (difference between expected and actual)
- `root_cause`: Text (analysis of why delay occurred)
- `status`: Enum (Identified, Analyzed, Resolved, Monitoring)
- `identified_at`: DateTime (when identified)
- `resolved_at`: DateTime (optional, when resolved)
- `recommendations`: Array of Strings (how to prevent in future)

**Relationships**:
- Many-to-one with Task (via task_reference)

**Validation Rules**:
- Status transitions must follow defined lifecycle
- Delay hours must be non-negative
- Expected duration must be positive

### 5. Subscription
**Description**: Recurring costs and usage analytics
**Fields**:
- `id`: String (unique vendor-service identifier)
- `vendor`: String (service provider)
- `service_name`: String (name of service)
- `cost_per_month`: Decimal (monthly cost)
- `last_used_date`: Date (when last actively used)
- `status`: Enum (Active, Inactive, Canceled)
- `cancellation_date`: Date (optional, if canceled)
- `usage_metrics`: Object (monthly usage statistics)
- `cost_per_use`: Decimal (calculated cost per usage metric)
- `recommendations`: Array of Strings (optimization suggestions)

**Relationships**:
- One-to-many with Usage Metric records

**Validation Rules**:
- Cost must be positive decimal
- Status transitions must follow defined lifecycle
- Last used date must not be in the future

### 6. Task
**Description**: Actionable items that drive invoice generation and other workflows
**Fields**:
- `id`: UUID (unique identifier)
- `title`: String (task description)
- `description`: Text (detailed task information)
- `status`: Enum (Created, In Progress, Completed, Pending Approval, Done, Rejected)
- `assigned_to`: String (AI employee or human)
- `created_at`: DateTime (timestamp)
- `updated_at`: DateTime (timestamp)
- `completed_at`: DateTime (optional, timestamp)
- `related_invoice_id`: String (optional, reference to related invoice)
- `priority`: Enum (Low, Medium, High, Critical)

**Relationships**:
- One-to-many with Invoice (via related_invoice_id)
- Many-to-one with Business Goal (via goal_reference)

**Validation Rules**:
- Title must be 1-200 characters
- Status transitions must follow defined lifecycle
- Priority must be one of defined values

## Technical Entities

### 7. Watcher
**Description**: Background processes that monitor external sources
**Fields**:
- `id`: String (unique identifier)
- `name`: String (name of watcher)
- `status`: Enum (Running, Stopped, Error, Restarting)
- `last_check`: DateTime (timestamp of last check)
- `error_count`: Integer (number of consecutive errors)
- `restart_count`: Integer (number of restarts)
- `config`: Object (configuration parameters)

**Validation Rules**:
- Status must be one of defined values
- Error and restart counts must be non-negative

### 8. Skill
**Description**: Modular functions that perform specific business capabilities
**Fields**:
- `id`: String (unique identifier)
- `name`: String (skill name)
- `description`: Text (what the skill does)
- `enabled`: Boolean (whether skill is active)
- `execution_count`: Integer (times executed)
- `success_rate`: Decimal (percentage of successful executions)
- `last_executed`: DateTime (when last run)

**Validation Rules**:
- Success rate must be between 0 and 100
- Enabled must be boolean

### 9. MCP Server
**Description**: Service interfaces for external integrations
**Fields**:
- `id`: String (unique identifier)
- `name`: String (server name)
- `host`: String (server address)
- `port`: Integer (server port)
- `status`: Enum (Running, Stopped, Error)
- `health_check_url`: String (URL for health check)
- `request_count`: Integer (total requests served)
- `error_count`: Integer (total errors)

**Validation Rules**:
- Port must be between 1 and 65535
- Status must be one of defined values

### 10. Audit Log
**Description**: Compliance and operational logs
**Fields**:
- `id`: String (unique identifier)
- `timestamp`: DateTime (when event occurred)
- `entity_type`: String (type of entity affected)
- `entity_id`: String (ID of entity affected)
- `action`: String (what action was taken)
- `actor`: String (who took the action - human or AI)
- `details`: Object (additional context)
- `decision_reasoning`: Text (why this decision was made)

**Validation Rules**:
- Timestamp must be current or past
- All fields required

### 11. Notification
**Description**: Alert and communication system
**Fields**:
- `id`: String (unique identifier)
- `level`: Enum (Info, Warning, Error, Critical)
- `title`: String (notification title)
- `message`: Text (detailed message)
- `timestamp`: DateTime (when created)
- `channels`: Array of Enums (Email, Desktop, Dashboard)
- `data`: Object (additional data for the notification)
- `acknowledged`: Boolean (whether acknowledged)

**Validation Rules**:
- Level must be one of defined values
- Timestamp must be current or past
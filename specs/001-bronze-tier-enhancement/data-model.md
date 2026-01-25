# Data Model: Bronze Tier Enhancement for Personal AI Employee

## Core Entities

### 1. AI Employee
- **Description**: The complete system of watchers, orchestrators, and reasoning engines
- **Fields**:
  - id: Unique identifier for the AI Employee instance
  - status: Current operational status (active, paused, maintenance)
  - created_date: When the AI Employee was initialized
  - last_activity: Timestamp of last activity
  - human_principal_id: Reference to the human owner
- **Validation**: Must have valid human principal assigned
- **State Transitions**: active ↔ paused ↔ maintenance

### 2. Obsidian Vault Entry
- **Description**: Individual entry/document in the Obsidian vault system
- **Fields**:
  - id: Unique identifier for the entry
  - title: Title of the entry
  - content: The markdown content of the entry
  - folder: Current folder location (Inbox, Needs_Action, Plans, Pending_Approval, Approved, Rejected, Done)
  - created_date: When the entry was created
  - modified_date: When the entry was last modified
  - author: Who created the entry (human or AI)
  - tags: Associated tags for categorization
- **Validation**: Must have valid folder assignment based on workflow
- **State Transitions**: Inbox → Needs_Action → Plans/Pending_Approval → Approved/Rejected → Done

### 3. Approval Request
- **Description**: A request for human approval of an AI-generated action
- **Fields**:
  - id: Unique identifier for the approval request
  - context: Background context for the decision
  - rationale: Reasoning behind the proposed action
  - proposed_action: Description of the action to be approved
  - risk_assessment: Potential risks identified
  - approval_tier: Tier level (0-3) as defined in constitution
  - created_date: When the request was submitted
  - due_date: Deadline for approval based on SLA
  - status: Current status (pending, approved, rejected, expired)
  - approver_comments: Comments from the human approver
- **Validation**: Must have valid approval tier and appropriate fields populated
- **State Transitions**: pending → approved/rejected/expired

### 4. Agent Skill
- **Description**: A specific capability or function that the AI Employee can perform
- **Fields**:
  - id: Unique identifier for the skill
  - name: Name of the skill (email_processor, invoice_generator, etc.)
  - description: Detailed description of what the skill does
  - input_format: Expected input format for the skill
  - output_format: Expected output format from the skill
  - error_handling: How errors are handled by the skill
  - approval_required: Whether this skill requires approval before execution
  - status: Current status (active, disabled, testing)
  - last_executed: When the skill was last executed
  - success_rate: Historical success rate of the skill
- **Validation**: Must have valid input/output formats and appropriate approval requirements
- **State Transitions**: testing → active/disabled

### 5. Log Entry
- **Description**: Structured log entry for auditability and monitoring
- **Fields**:
  - id: Unique identifier for the log entry
  - timestamp: When the event occurred
  - level: Log level (info, warning, error, critical)
  - component: Which system component generated the log
  - event_type: Type of event (action_taken, decision_made, error_occurred, approval_request, etc.)
  - message: Human-readable description of the event
  - details: Additional structured details in JSON format
  - correlation_id: ID to correlate related events
  - user_context: Context about the user/human principal involved
- **Validation**: Must have valid timestamp and appropriate level/type
- **State Transitions**: None (immutable once created)

### 6. Watcher Event
- **Description**: An event detected by a monitoring script (watcher)
- **Fields**:
  - id: Unique identifier for the event
  - watcher_type: Type of watcher that detected the event (FileSystem, Gmail, LinkedIn, etc.)
  - source: Specific source of the event (email address, file path, etc.)
  - event_content: Raw content of the detected event
  - processed: Whether the event has been processed by AI
  - created_date: When the event was detected
  - priority: Priority level for processing
  - triggered_ai_attention: Whether this event triggered AI attention
  - vault_entry_id: Reference to the vault entry created from this event
- **Validation**: Must have valid watcher type and source information
- **State Transitions**: detected → processed → archived

## Relationships

1. **AI Employee** → **Obsidian Vault Entry** (1 to many): One AI Employee manages many vault entries
2. **AI Employee** → **Approval Request** (1 to many): One AI Employee generates many approval requests
3. **AI Employee** → **Agent Skill** (1 to many): One AI Employee uses many agent skills
4. **AI Employee** → **Log Entry** (1 to many): One AI Employee generates many log entries
5. **AI Employee** → **Watcher Event** (1 to many): One AI Employee handles many watcher events
6. **Approval Request** → **Obsidian Vault Entry** (1 to 1): Each approval request corresponds to a vault entry
7. **Watcher Event** → **Obsidian Vault Entry** (1 to 1): Each watcher event may create a vault entry

## Validation Rules from Requirements

- Vault entries must follow the constitutional folder hierarchy (Inbox → Needs_Action → Plans → Pending_Approval → Approved/Rejected → Done)
- Approval requests must include Context, Rationale, Proposed Action, Risk Assessment, and Approval Tier as required by constitution
- All actions must be logged for auditability (Action Log, Decision Log, Error Log, Audit Log)
- Agent skills must implement proper error handling as required for Bronze tier
- Watcher events must trigger AI attention based on configurable rules
- All sensitive data must remain in the local Vault (data sovereignty requirement)
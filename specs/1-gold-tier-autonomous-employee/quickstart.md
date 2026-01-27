# Quickstart Guide: Gold Tier Autonomous Employee System

## Prerequisites

- **Python 3.13+** installed on your system
- **Node.js v24+** installed for MCP servers
- **Git** for version control and backups
- **Claude Code** access (or compatible LLM)
- **Obsidian v1.10.6+** for vault management
- **Xero Developer Account** (for accounting integration)
- **Social Media Developer Accounts** (Facebook, Instagram, Twitter)
- **PM2** (optional, for production process management)

## Installation Steps

### 1. Clone and Setup the Repository

```bash
# Clone the repository
git clone [repository-url]
cd [repository-name]

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies for MCP servers
cd mcp_servers/email_server && npm install && cd ../..
cd mcp_servers/linkedin_server && npm install && cd ../..
```

### 2. Set Up the Obsidian Vault

```bash
# Create the vault structure
mkdir -p AI_Employee_Vault/{Inbox,Needs_Action,Plans,Pending_Approval,Approved,Rejected,Done}
mkdir -p AI_Employee_Vault/{Accounting,Accounting/Invoices,Accounting/Expenses,Accounting/Reports,Accounting/Tax}
mkdir -p AI_Employee_Vault/{Social_Media,Social_Media/Facebook,Social_Media/Instagram,Social_Media/Twitter,Social_Media/Analytics}
mkdir -p AI_Employee_Vault/{Business_Analytics,Business_Analytics/Weekly_Reports,Business_Analytics/Monthly_Reports,Business_Analytics/Audit_Logs}
mkdir -p AI_Employee_Vault/{Briefings/Weekly,Briefings/Monthly,Briefings/Templates}

# Create essential vault files
touch AI_Employee_Vault/Dashboard.md
touch AI_Employee_Vault/Company_Handbook.md
touch AI_Employee_Vault/Business_Goals.md
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
# API Keys and Secrets
CLAUDE_API_KEY=your_claude_api_key
XERO_CLIENT_ID=your_xero_client_id
XERO_CLIENT_SECRET=your_xero_client_secret
XERO_REDIRECT_URI=http://localhost:3001/callback

# Social Media API Keys
FACEBOOK_ACCESS_TOKEN=your_facebook_access_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# System Configuration
VAULT_PATH=./AI_Employee_Vault
LOG_LEVEL=INFO
```

### 4. Set Up MCP Servers

For each MCP server (Xero, Facebook, Instagram, Twitter, Calendar):

```bash
# Navigate to the MCP server directory
cd mcp_servers/xero_server

# Install dependencies
npm install

# Configure environment variables in .env file
echo "XERO_CLIENT_ID=your_client_id" > .env
echo "XERO_CLIENT_SECRET=your_client_secret" >> .env
# ... other required variables

# Start the server
node index.js --port 3001
```

### 5. Initialize the System

```bash
# Start the main orchestrator
python -m orchestrator.process_manager

# Start individual watchers
python -m watchers.gmail_watcher
python -m watchers.linkedin_watcher
python -m watchers.xero_watcher
# ... other watchers as needed
```

## Configuration

### 1. Business Goals Setup

Create `AI_Employee_Vault/Business_Goals.md`:

```markdown
# Business Goals

## Primary Objectives
1. Automate invoice generation and tracking
2. Maintain consistent social media presence
3. Generate weekly CEO briefings
4. Identify business bottlenecks and opportunities

## Key Performance Indicators
- Revenue growth: 10% monthly
- Social media engagement: 5% monthly increase
- Time saved: 20+ hours per week
- Invoice accuracy: 99%+

## Strategic Initiatives
- Q1: Establish automated accounting
- Q2: Scale social media presence
- Q3: Enhance business intelligence
- Q4: Optimize operational efficiency
```

### 2. Approval Workflow Configuration

Set up approval tiers in `AI_Employee_Vault/Company_Handbook.md`:

```markdown
# Approval Tiers

## Tier 0: Autonomous (No Approval Required)
- Reading emails, documents, web content
- Generating internal summaries and plans
- Logging events and system status
- Creating draft content in /Plans folder

## Tier 1: Notification Required
- Sending routine scheduled posts (LinkedIn, social media)
- Creating calendar events
- Sending templated email responses

## Tier 2: Explicit Approval Required
- Sending original emails with custom content
- Financial transactions of any amount
- Modifying business-critical documents
- Posting content that represents the Principal publicly

## Tier 3: Multi-Factor Approval Required
- Transactions exceeding $500 (configurable threshold)
- Terminating business relationships
- Sharing confidential information externally
- Modifying system security configurations
```

## Running the System

### 1. Start All Components

```bash
# Using PM2 for production (optional)
pm2 start ecosystem.config.js

# Or manually start components
python -m orchestrator.process_manager &
python -m watchers.gmail_watcher &
python -m watchers.linkedin_watcher &
python -m watchers.xero_watcher &
# ... start other watchers
```

### 2. Monitor the System

Check the `AI_Employee_Vault/Dashboard.md` for system status and metrics.

### 3. Weekly CEO Briefing

The system automatically generates a CEO briefing every Sunday evening for Monday delivery. Check `AI_Employee_Vault/Briefings/Weekly/` for the reports.

## Key Features Setup

### 1. Xero Integration
- Complete OAuth flow with Xero
- Set up webhook for real-time updates
- Configure invoice templates in the vault

### 2. Social Media Automation
- Connect all four platforms (Facebook, Instagram, Twitter, LinkedIn)
- Set up content calendar in the vault
- Configure posting schedules

### 3. Cross-Domain Workflows
- Configure email-to-task workflows
- Set up task-to-invoice automation
- Enable payment-to-social-post workflows

## Troubleshooting

### Common Issues

1. **MCP Server Not Responding**
   - Check if the server is running: `curl http://localhost:PORT/health`
   - Verify environment variables are set correctly
   - Check firewall settings

2. **API Rate Limits**
   - Review logs for rate limit errors
   - Adjust scheduling to spread requests
   - Verify OAuth tokens are valid

3. **Watcher Failures**
   - Check error logs in `logs/` directory
   - Verify credentials and permissions
   - Ensure network connectivity

### Emergency Procedures

1. **Immediate Stop**: Create `EMERGENCY_STOP.md` in the vault root
2. **Restart**: Remove the emergency stop file and restart components
3. **Investigation**: Review logs in `AI_Employee_Vault/Logs/`

## Next Steps

1. Test all configured workflows with sample data
2. Fine-tune approval thresholds based on comfort level
3. Monitor system performance and adjust configurations
4. Gradually increase autonomy as trust builds
5. Review and update business goals quarterly
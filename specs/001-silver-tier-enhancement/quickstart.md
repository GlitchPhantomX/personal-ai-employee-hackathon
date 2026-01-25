# Silver Tier Enhancement - Quick Start Guide

## Overview
This guide provides instructions for setting up and running the Silver Tier Enhancement of the Personal AI Employee system. This includes multiple watchers, automated LinkedIn posting, Claude reasoning loops, MCP server integration, programmatic approval workflows, and scheduling systems.

## Prerequisites

### System Requirements
- Python 3.13+ installed
- Node.js v24+ installed
- Obsidian v1.10.6+ installed
- Git installed
- Claude Code access (or compatible LLM)
- Platform-specific scheduler:
  - Linux/macOS: cron
  - Windows: Task Scheduler

### Environment Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Personal_AI_Employee
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies for MCP servers:
   ```bash
   cd mcp_servers/email_server && npm install
   cd ../linkedin_server && npm install
   cd ../browser_server && npm install
   ```

## Configuration

### 1. Configure Vault Structure
The system expects the following directory structure:
```
AI_Employee_Vault/
├── Dashboard.md
├── Company_Handbook.md
├── Business_Goals.md
├── Inbox/
├── Needs_Action/
├── Plans/
├── Pending_Approval/
├── Approved/
├── Rejected/
├── Done/
├── Skills/
├── Logs/
└── Briefings/
```

Create this structure if it doesn't exist:
```bash
mkdir -p AI_Employee_Vault/{Inbox,Needs_Action,Plans,Pending_Approval,Approved,Rejected,Done,Skills,Logs,Briefings}
```

### 2. Set Up Credentials
Create a credentials folder and add your API keys:
```bash
mkdir credentials
```

Add your credentials to `credentials/api_keys.json`:
```json
{
  "linkedin": {
    "client_id": "your_linkedin_client_id",
    "client_secret": "your_linkedin_client_secret",
    "access_token": "your_linkedin_access_token"
  },
  "gmail": {
    "api_key": "your_gmail_api_key"
  },
  "claude": {
    "api_key": "your_claude_api_key"
  }
}
```

**Important**: Add `credentials/` to `.gitignore` to prevent committing credentials.

### 3. Configure Settings
Update `config/settings.py` with your specific configuration:
- Vault path
- API endpoints
- Approval thresholds
- Scheduling intervals

## Starting the System

### 1. Start MCP Servers
First, start the MCP servers that handle external actions:

```bash
# Terminal 1: Start email server
cd mcp_servers/email_server
npm start

# Terminal 2: Start LinkedIn server
cd mcp_servers/linkedin_server
npm start

# Terminal 3: Start browser server (if needed)
cd mcp_servers/browser_server
npm start
```

### 2. Start Watchers
Start the watcher processes that monitor for events:

```bash
# Start Gmail watcher
python watchers/gmail_watcher.py

# Start LinkedIn watcher
python watchers/linkedin_watcher.py

# Start File System watcher
python watchers/file_system_watcher.py
```

### 3. Initialize Planning Orchestrator
Start the planning orchestrator that generates Plan.md files:

```bash
python orchestrator/planning_orchestrator.py
```

### 4. Start Approval Handler
Start the approval workflow handler:

```bash
python orchestrator/approval_handler.py
```

## Automated Setup (Recommended)

For convenience, you can use the setup scripts:

### Linux/macOS:
```bash
bash scripts/setup_cron.sh
```

### Windows:
```cmd
powershell -File scripts/setup_task_scheduler.ps1
```

## Key Features Setup

### 1. LinkedIn Automated Posting
1. Configure your LinkedIn API credentials in `credentials/api_keys.json`
2. Set up posting schedule in `AI_Employee_Vault/linkedin_schedule.json`
3. Define content templates in `skills/linkedin_poster.py`

### 2. Claude Reasoning Loop
1. Ensure Claude API key is configured
2. Review and customize the Plan.md template in the Plans folder
3. Test with a sample event to verify Plan generation

### 3. Programmatic Approval Workflow
1. Review approval tiers in `config/settings.py`
2. Set up notification preferences
3. Test approval process with a sample request

### 4. Scheduling System
1. Configure scheduled tasks in `config/schedule_config.py`
2. Review the crontab entries (Linux/macOS) or scheduled tasks (Windows)
3. Test with a simple scheduled health check

## Testing the System

### 1. Test Watchers
Place a test file in the monitored directory to verify the file system watcher is working:
```bash
echo "Test event" > AI_Employee_Vault/Inbox/test_event.md
```

### 2. Test MCP Server Connection
Verify MCP servers are responding:
```bash
curl http://localhost:3000/health  # Email server
curl http://localhost:3001/health  # LinkedIn server
curl http://localhost:3002/health  # Browser server
```

### 3. Test Plan Generation
Trigger Claude to generate a Plan.md by placing a request in the appropriate folder.

### 4. Test Approval Workflow
Submit a test approval request and verify it appears in the Pending_Approval folder.

## Monitoring and Maintenance

### 1. Dashboard
Monitor the system through `AI_Employee_Vault/Dashboard.md` which provides real-time status updates.

### 2. Logs
Check logs in `AI_Employee_Vault/Logs/` for troubleshooting:
- Action logs: `YYYY-MM-DD_action_log.json`
- Decision logs: `YYYY-MM-DD_decision_log.json`
- Error logs: `YYYY-MM-DD_error_log.json`

### 3. Health Checks
The system performs automated health checks:
- Every 5 minutes: Watcher process verification
- Every 30 minutes: Vault file system integrity
- Every 6 hours: End-to-end action capability test
- Daily: CEO Briefing generation

## Troubleshooting

### Common Issues

1. **Watchers not detecting events**: Check authentication and permissions in credentials
2. **AI not processing files**: Verify vault access and Claude configuration
3. **Approval workflow not working**: Check folder permissions and workflow procedures
4. **MCP servers not responding**: Verify servers are running and ports are accessible
5. **Scheduling not working**: Check cron/Task Scheduler configuration

### Emergency Stop
To immediately halt all outbound actions:
1. Delete the `Approved/` folder or
2. Create an `EMERGENCY_STOP.md` file in the vault root

### Recovery
To restart the system after an emergency stop:
1. Investigate the cause in the logs
2. Fix the issue
3. Restart the MCP servers
4. Restart the watchers and orchestrators

## Next Steps

1. Customize the Company Handbook: `AI_Employee_Vault/Company_Handbook.md`
2. Define your business goals: `AI_Employee_Vault/Business_Goals.md`
3. Set up your first automated LinkedIn posts
4. Configure additional watchers for your specific needs
5. Add custom Agent Skills for your domain-specific tasks

## Success Metrics

After setup, monitor these key metrics:
- System uptime: Should be >99.5%
- Approval turnaround: Should be <24 hours
- LinkedIn post success rate: Should be >95%
- Scheduled task reliability: Should be >99%

## Support

For questions or issues:
- Join the Wednesday Research Meeting at 10:00 PM
- Check the troubleshooting section in the Company Handbook
- Review the logs for error details
- Consult the community documentation
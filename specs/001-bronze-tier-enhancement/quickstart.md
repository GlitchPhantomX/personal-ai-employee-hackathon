# Quickstart Guide: Bronze Tier Enhancement for Personal AI Employee

## Overview
This guide provides instructions for setting up and using the Bronze Tier Enhanced Personal AI Employee system. The system follows a five-layer architecture with Obsidian-based vault for knowledge management and Claude Code for reasoning.

## Prerequisites
- Python 3.13+ installed
- Obsidian v1.10.6+ installed
- Claude Code access configured
- Git for version control
- Node.js v24+ (for MCP servers, if needed)

## Setup Instructions

### 1. Initialize the Obsidian Vault
1. Create the required folder structure in your Obsidian vault:
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
   │   ├── email_processor.md
   │   ├── invoice_generator.md
   │   ├── linkedin_poster.md
   │   ├── task_creator.md
   │   └── whatsapp_handler.md
   └── Logs/
   ```

2. Populate the initial markdown files with basic information about your business goals and operating procedures.

### 2. Configure Watchers
1. Set up at least one of the following watchers:
   - FileSystemWatcher: Monitors file system changes
   - GmailWatcher: Monitors Gmail inbox
   - LinkedInWatcher: Monitors LinkedIn notifications

2. Configure authentication and access tokens for each watcher you plan to use.

### 3. Set Up Claude Code Integration
1. Configure Claude Code to read from and write to your Obsidian vault
2. Ensure Claude can create files in the Needs_Action directory
3. Test the basic read/write functionality

### 4. Install Agent Skills
1. Copy the 5 agent skills to the Skills/ directory:
   - email_processor.md
   - invoice_generator.md
   - linkedin_poster.md
   - task_creator.md
   - whatsapp_handler.md

2. Configure each skill with appropriate permissions and authentication

### 5. Configure Logging
1. Set up structured JSON logging for auditability
2. Configure log rotation to prevent logs from growing too large
3. Ensure logs are stored in the Logs/ directory

## Basic Usage

### 1. Processing Events
1. Events detected by watchers will appear in the Inbox/ folder
2. Review events and move them to Needs_Action/ for processing
3. Claude will analyze events and create plans in the Plans/ folder
4. For actions requiring approval, move files to Pending_Approval/
5. Review and approve/reject actions by moving them to Approved/ or Rejected/

### 2. Using Agent Skills
1. Create a request in the appropriate format in Needs_Action/
2. The relevant agent skill will process the request
3. Monitor the status and output in the corresponding folders

### 3. Monitoring System Health
1. Check Dashboard.md for real-time status updates
2. Review logs in the Logs/ directory for system health
3. Monitor the approval workflow for any bottlenecks

## Bronze Tier Requirements Check

To verify your system meets Bronze Tier requirements:

1. ✅ **Folder Structure**: Verify all required directories exist
2. ✅ **One Working Watcher**: Confirm at least one watcher is operational
3. ✅ **Claude Integration**: Verify Claude can read/write to vault
4. ✅ **5 Agent Skills**: Confirm all 5 skills are installed and functional
5. ✅ **Basic Approval Workflow**: Test the Pending_Approval → Approved flow
6. ✅ **Process 10 Events**: Run a test with 10 sample events end-to-end
7. ✅ **Zero Data Loss**: Verify no data is lost during processing
8. ✅ **Auto-Restart**: Test that watchers restart after failure

## Troubleshooting

### Common Issues
- **Watchers not detecting events**: Check authentication and permissions
- **Claude not processing files**: Verify vault access and Claude configuration
- **Approval workflow not working**: Check folder permissions and workflow procedures
- **Logs growing too large**: Verify log rotation is configured properly

### System Maintenance
- Regularly archive old files from Needs_Action to Done/Archive/
- Clean up temporary files from the main directory
- Update Dashboard.md with current metrics
- Review and update Company_Handbook.md as needed
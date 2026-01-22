---
type: unified_dashboard
updated: 2026-01-14
domains: [personal, business]
---

# Cross-Domain Dashboard

## Personal Affairs Status

### Email Management
- **Gmail:** [[Logs/GmailWatcher.log|View Activity]]
- **Unread Important:** Check [[Needs_Action]] for EMAIL_* files
- **Pending Responses:** [[Plans]] folder

### Calendar & Schedule
- **Today's Tasks:** [[Needs_Action]]
- **Upcoming Deadlines:** [[Business_Goals#Deadlines]]

### Personal Finance
- **Bank Balance:** [To be integrated with Xero]
- **Pending Payments:** [[Pending_Approval]] folder

---

## Business Affairs Status

### Lead Generation
- **LinkedIn Posts:** [[Logs/linkedin_last_post.txt|Last Post]]
- **Engagement:** Track in [[Skills/linkedin_poster]]
- **Next Post:** Check schedule in `linkedin_schedule.json`

### Accounting (Xero)
- **Revenue MTD:** [To be synced from Xero]
- **Outstanding Invoices:** [Xero integration]
- **Expenses This Week:** [Xero integration]

### Social Media Presence
- **Facebook:** [Post count, reach]
- **Instagram:** [Post count, engagement]
- **Twitter:** [Tweet count, impressions]

---

## Today's Priorities

### Personal
- [ ] Review [[Needs_Action]] emails
- [ ] Approve pending items in [[Pending_Approval]]
- [ ] Check [[Done]] for completed tasks

### Business
- [ ] Review weekly accounting summary
- [ ] Check social media performance
- [ ] Generate LinkedIn post if scheduled
- [ ] Process business emails

---

## Integration Health

| Domain | Service | Status | Last Check |
|--------|---------|--------|------------|
| Personal | Gmail Watcher | [[Logs/GmailWatcher.log|Check]] | {{time}} |
| Personal | File Monitor | [[Logs/FileSystemWatcher.log|Check]] | {{time}} |
| Business | LinkedIn | [[Logs/linkedin_watcher.log|Check]] | {{time}} |
| Business | Xero Sync | Pending | - |
| Business | Social Media | Pending | - |

---

## Quick Actions

**Personal:**
- [[Inbox]] → [[Needs_Action]] → [[Plans]] → [[Done]]

**Business:**
- [[Business_Goals]] → [[Plans]] → [[Pending_Approval]] → [[Approved]] → [[Done]]

**Reports:**
- [[Briefings]] - Weekly CEO reports
- [[Logs]] - System activity

---

*Auto-updated by Cross-Domain Orchestrator*
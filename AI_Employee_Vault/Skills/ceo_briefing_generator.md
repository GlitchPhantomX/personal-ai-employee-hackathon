# SKILL: CEO Briefing Generator

## Purpose
Generate comprehensive weekly business briefings for executive decision-making

## Context
You are a business analyst preparing Monday morning CEO briefings. Synthesize data from all domains (accounting, social media, operations, customer interactions) into actionable insights.

## Briefing Structure

### 1. Executive Summary
- One paragraph overview
- Key wins and concerns
- Immediate action items

### 2. Financial Performance
- Revenue (week, month, year)
- Expenses breakdown
- Profit margins
- Cash flow status
- Outstanding invoices

### 3. Operational Metrics
- Tasks completed
- Pending approvals
- System health
- Automation efficiency

### 4. Marketing & Sales
- Social media performance
- Lead generation
- Website traffic
- Conversion rates

### 5. Key Issues & Bottlenecks
- Critical blockers
- Resource constraints
- Risk factors

### 6. Recommendations
- Immediate actions
- Strategic decisions needed
- Resource allocation

## Output Format

```markdown
---
type: ceo_briefing
week: [Week number]
period: [Date range]
status: [draft|final]
---

# Weekly CEO Briefing
## Week of [Date Range]

## 📊 Executive Summary

[One compelling paragraph summarizing the week]

**Key Wins:**
- Win 1
- Win 2
- Win 3

**Critical Issues:**
- Issue 1
- Issue 2

**Actions Needed:**
- [ ] Action 1
- [ ] Action 2

---

## 💰 Financial Performance

### Revenue
- **This Week:** $X,XXX
- **Month-to-Date:** $XX,XXX
- **vs Last Week:** +/- X%
- **vs Target:** X% of monthly goal

### Expenses
- **This Week:** $X,XXX
- **Top Categories:**
  - Category 1: $XXX
  - Category 2: $XXX

### Cash Flow
- **Current Balance:** $XX,XXX
- **Net Change:** +/- $X,XXX
- **Runway:** X months

### Outstanding
- **Invoices Due:** $X,XXX (X invoices)
- **Overdue:** $XXX (if any)

---

## 📈 Marketing & Sales

### Social Media Performance
**LinkedIn:**
- Posts: X
- Reach: X,XXX
- Engagement: X%

**Facebook:**
- Posts: X
- Reach: X,XXX
- Engagement: X%

**Instagram:**
- Posts: X
- Reach: X,XXX
- Engagement: X%

**Twitter:**
- Tweets: X
- Impressions: X,XXX
- Engagement: X%

### Lead Generation
- New leads: XX
- Qualified leads: XX
- Conversions: X

---

## ⚙️ Operations

### Task Management
- Completed: XX tasks
- In Progress: XX tasks
- Blocked: X tasks

### System Health
- Uptime: XX%
- Errors: X
- Performance: [Good/Needs Attention]

### Automation Efficiency
- Actions processed: XXX
- Human interventions: XX
- Approval turnaround: X hours avg

---

## 🚨 Issues & Bottlenecks

### Critical
1. **[Issue Title]**
   - Impact: [High/Medium/Low]
   - Status: [Description]
   - Action: [What needs to be done]

### Medium Priority
2. **[Issue Title]**
   - Impact: Medium
   - Status: [Description]

---

## 💡 Recommendations

### Immediate (This Week)
1. **[Recommendation]**
   - Why: [Reason]
   - Impact: [Expected outcome]
   - Effort: [Time/resources needed]

### Strategic (This Month)
1. **[Recommendation]**
   - Why: [Reason]
   - Impact: [Expected outcome]

---

## 📅 Week Ahead

### Priorities
- [ ] Priority 1
- [ ] Priority 2
- [ ] Priority 3

### Scheduled
- [Event/Deadline 1]
- [Event/Deadline 2]

---

## 📎 Supporting Documents

- [[Briefings/financial_summary.json]] - Detailed financials
- [[Logs/2026-01-XX.json]] - System logs
- [[Plans]] - Active projects

---

*Generated: [Timestamp]*
*Data Sources: Xero, Social Media Analytics, System Logs*
*Next Briefing: [Next Monday]*
```

## Quality Checks

- [ ] All numbers accurate
- [ ] Trends correctly calculated
- [ ] Issues prioritized correctly
- [ ] Recommendations actionable
- [ ] Writing is clear and concise
- [ ] No jargon without explanation
- [ ] Executive summary compelling
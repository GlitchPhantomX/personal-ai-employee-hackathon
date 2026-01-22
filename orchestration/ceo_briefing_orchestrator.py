#!/usr/bin/env python3
"""
CEO Briefing Orchestrator
Generates weekly Monday morning briefings
Synthesizes data from all systems
"""

from pathlib import Path
from datetime import datetime, timedelta
import json
import logging

class CEOBriefingOrchestrator:
    """
    Generates comprehensive CEO briefings
    Runs every Monday morning
    """

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.briefings_dir = self.vault_path / 'Briefings'
        self.logs_dir = self.vault_path / 'Logs'

        self.logger = logging.getLogger('CEOBriefing')

        # Ensure briefings directory exists
        self.briefings_dir.mkdir(exist_ok=True)

    def should_generate_briefing(self) -> bool:
        """
        Check if briefing should be generated
        (Every Monday morning)
        """
        now = datetime.now()

        # Check if it's Monday
        if now.weekday() != 0:
            return False

        # Check if already generated today
        today_briefing = self.briefings_dir / f'CEO_Briefing_{now.strftime("%Y-%m-%d")}.md'

        if today_briefing.exists():
            return False

        return True

    def collect_financial_data(self) -> dict:
        """Collect financial data from Xero logs"""
        # In production, would query Xero API
        # For demo, simulate with available data

        return {
            'revenue_week': 2500,
            'revenue_month': 8750,
            'revenue_target': 10000,
            'expenses_week': 800,
            'cash_balance': 32000,
            'invoices_outstanding': 3000,
            'profit_week': 1700
        }

    def collect_social_media_data(self) -> dict:
        """Collect social media performance"""
        social_log = self.logs_dir / 'social_last_post.json'

        # Simulated data
        return {
            'linkedin': {'posts': 3, 'reach': 4500, 'engagement': '4.2%'},
            'facebook': {'posts': 3, 'reach': 3200, 'engagement': '3.8%'},
            'instagram': {'posts': 4, 'reach': 2800, 'engagement': '5.1%'},
            'twitter': {'posts': 15, 'impressions': 8500, 'engagement': '2.1%'}
        }

    def collect_operations_data(self) -> dict:
        """Collect operational metrics"""
        needs_action = self.vault_path / 'Needs_Action'
        done = self.vault_path / 'Done'

        needs_count = len(list(needs_action.glob('*.md'))) - 1  # Exclude README
        done_count = len(list(done.glob('*.md'))) - 1

        return {
            'tasks_completed': done_count,
            'tasks_pending': needs_count,
            'system_uptime': '99.2%',
            'errors': 2,
            'approvals_avg_time': '3.5 hours'
        }

    def identify_issues(self) -> list:
        """Identify current issues and bottlenecks"""
        # In production, would analyze logs and metrics
        # For demo, return template

        return [
            {
                'title': 'Cash Flow Attention Needed',
                'impact': 'Medium',
                'description': 'Outstanding invoices total $3,000',
                'action': 'Follow up with clients on overdue payments'
            }
        ]

    def generate_recommendations(self, data: dict) -> list:
        """Generate strategic recommendations"""
        recommendations = []

        # Example logic
        if data['financial']['cash_balance'] < 30000:
            recommendations.append({
                'title': 'Prioritize Invoice Collection',
                'why': 'Cash balance below comfortable threshold',
                'impact': 'Improve cash runway by 2 weeks',
                'effort': '2-3 hours this week'
            })

        return recommendations

    def generate_briefing(self) -> Path:
        """
        Generate complete CEO briefing

        Returns:
            Path to generated briefing file
        """
        self.logger.info('Generating CEO briefing...')

        # Collect all data
        financial = self.collect_financial_data()
        social = self.collect_social_media_data()
        operations = self.collect_operations_data()

        data = {
            'financial': financial,
            'social': social,
            'operations': operations
        }

        issues = self.identify_issues()
        recommendations = self.generate_recommendations(data)

        # Generate briefing content
        now = datetime.now()
        week_start = now - timedelta(days=now.weekday())
        week_end = week_start + timedelta(days=6)

        content = f"""---
type: ceo_briefing
week: {now.isocalendar()[1]}
period: {week_start.strftime('%Y-%m-%d')} to {week_end.strftime('%Y-%m-%d')}
status: final
generated: {now.isoformat()}
---

# Weekly CEO Briefing
## Week of {week_start.strftime('%B %d')} - {week_end.strftime('%B %d, %Y')}

## 📊 Executive Summary

This week showed strong operational performance with {operations['tasks_completed']} tasks completed and {operations['system_uptime']} system uptime. Revenue of ${financial['revenue_week']:,.0f} puts us at {(financial['revenue_month']/financial['revenue_target']*100):.1f}% of monthly target. Social media engagement remains strong across all platforms.

**Key Wins:**
- Completed {operations['tasks_completed']} tasks with high efficiency
- Social media reach: {social['linkedin']['reach'] + social['facebook']['reach'] + social['instagram']['reach']:,} combined
- System uptime: {operations['system_uptime']}

**Critical Issues:**
{chr(10).join([f"- {issue['title']}" for issue in issues])}

**Actions Needed:**
{chr(10).join([f"- [ ] {issue['action']}" for issue in issues])}

---

## 💰 Financial Performance

### Revenue
- **This Week:** ${financial['revenue_week']:,.2f}
- **Month-to-Date:** ${financial['revenue_month']:,.2f}
- **vs Target:** {(financial['revenue_month']/financial['revenue_target']*100):.1f}% of ${financial['revenue_target']:,} monthly goal
- **Profit This Week:** ${financial['profit_week']:,.2f}

### Expenses
- **This Week:** ${financial['expenses_week']:,.2f}
- **Profit Margin:** {(financial['profit_week']/financial['revenue_week']*100):.1f}%

### Cash Flow
- **Current Balance:** ${financial['cash_balance']:,.2f}
- **Net Change:** +${financial['profit_week']:,.2f}
- **Runway:** {(financial['cash_balance']/financial['expenses_week']):.1f} weeks

### Outstanding
- **Invoices Due:** ${financial['invoices_outstanding']:,.2f}

---

## 📈 Marketing & Sales

### Social Media Performance

**LinkedIn:**
- Posts: {social['linkedin']['posts']}
- Reach: {social['linkedin']['reach']:,}
- Engagement: {social['linkedin']['engagement']}

**Facebook:**
- Posts: {social['facebook']['posts']}
- Reach: {social['facebook']['reach']:,}
- Engagement: {social['facebook']['engagement']}

**Instagram:**
- Posts: {social['instagram']['posts']}
- Reach: {social['instagram']['reach']:,}
- Engagement: {social['instagram']['engagement']}

**Twitter:**
- Tweets: {social['twitter']['posts']}
- Impressions: {social['twitter']['impressions']:,}
- Engagement: {social['twitter']['engagement']}

---

## ⚙️ Operations

### Task Management
- Completed: {operations['tasks_completed']} tasks
- In Progress: {operations['tasks_pending']} tasks

### System Health
- Uptime: {operations['system_uptime']}
- Errors: {operations['errors']}
- Performance: Good

### Automation Efficiency
- Approval turnaround: {operations['approvals_avg_time']} avg

---

## 🚨 Issues & Bottlenecks

{chr(10).join([f'''### {issue['impact']} Priority
**{issue['title']}**
- Impact: {issue['impact']}
- Status: {issue['description']}
- Action: {issue['action']}
''' for issue in issues])}

---

## 💡 Recommendations

### Immediate (This Week)
{chr(10).join([f'''**{rec['title']}**
- Why: {rec['why']}
- Impact: {rec['impact']}
- Effort: {rec['effort']}
''' for rec in recommendations])}

---

## 📅 Week Ahead

### Priorities
- [ ] Follow up on outstanding invoices
- [ ] Review and optimize social media strategy
- [ ] Plan next month's goals

---

## 📎 Supporting Documents

- [[Logs/{now.strftime('%Y-%m-%d')}.json]] - System logs
- [[social_media_schedule.json]] - Social strategy
- [[Business_Goals]] - Strategic objectives

---

*Generated: {now.strftime('%Y-%m-%d %H:%M:%S')}*
*Data Sources: System Logs, Simulated Financials (integrate Xero for production)*
*Next Briefing: {(now + timedelta(days=7)).strftime('%Y-%m-%d')} (Next Monday)*
"""

        # Save briefing
        briefing_path = self.briefings_dir / f'CEO_Briefing_{now.strftime("%Y-%m-%d")}.md'
        briefing_path.write_text(content, encoding='utf-8')

        self.logger.info(f'CEO briefing generated: {briefing_path.name}')

        return briefing_path

if __name__ == '__main__':
    orchestrator = CEOBriefingOrchestrator('../AI_Employee_Vault')

    if orchestrator.should_generate_briefing():
        briefing_path = orchestrator.generate_briefing()
        print(f'CEO briefing generated: {briefing_path}')
    else:
        print('CEO briefing not due (generated on Mondays only)')
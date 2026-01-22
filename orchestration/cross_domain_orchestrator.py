#!/usr/bin/env python3
"""
Cross-Domain Orchestrator
Coordinates personal and business workflows
"""

from pathlib import Path
from datetime import datetime
import logging
from typing import Dict, List

class CrossDomainOrchestrator:
    """
    Manages integration between personal and business domains
    """

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.logger = logging.getLogger('CrossDomainOrchestrator')

        # Domain paths
        self.personal_needs = []  # Personal tasks
        self.business_needs = []  # Business tasks

    def categorize_by_domain(self, action_file: Path) -> str:
        """
        Determine if action is personal or business

        Returns: 'personal' or 'business'
        """
        content = action_file.read_text(encoding='utf-8')

        # Business indicators
        business_keywords = [
            'invoice', 'payment', 'client', 'revenue',
            'linkedin', 'social media', 'accounting',
            'xero', 'business', 'lead', 'sales'
        ]

        # Personal indicators
        personal_keywords = [
            'personal', 'email', 'schedule', 'appointment',
            'reminder', 'calendar', 'family'
        ]

        content_lower = content.lower()

        business_score = sum(1 for kw in business_keywords if kw in content_lower)
        personal_score = sum(1 for kw in personal_keywords if kw in content_lower)

        return 'business' if business_score > personal_score else 'personal'

    def get_domain_summary(self) -> Dict:
        """
        Get summary of both domains
        """
        needs_action = self.vault_path / 'Needs_Action'

        personal_count = 0
        business_count = 0

        for file in needs_action.glob('*.md'):
            if file.name == 'README.md':
                continue

            domain = self.categorize_by_domain(file)
            if domain == 'personal':
                personal_count += 1
            else:
                business_count += 1

        return {
            'personal': {
                'pending_actions': personal_count,
                'domain': 'Personal Affairs'
            },
            'business': {
                'pending_actions': business_count,
                'domain': 'Business Operations'
            },
            'total': personal_count + business_count,
            'updated': datetime.now().isoformat()
        }

    def update_cross_domain_dashboard(self):
        """
        Update unified dashboard with both domains
        """
        summary = self.get_domain_summary()

        dashboard_path = self.vault_path / 'Cross_Domain_Dashboard.md'

        # Read template and update with real data
        if dashboard_path.exists():
            content = dashboard_path.read_text(encoding='utf-8')

            # Update timestamp
            content = content.replace('{{date}}', datetime.now().strftime('%Y-%m-%d'))
            content = content.replace('{{time}}', datetime.now().strftime('%H:%M:%S'))

            dashboard_path.write_text(content, encoding='utf-8')

        self.logger.info(f'Updated cross-domain dashboard: {summary}')
        return summary

if __name__ == '__main__':
    orchestrator = CrossDomainOrchestrator('../AI_Employee_Vault')
    summary = orchestrator.update_cross_domain_dashboard()
    print(f'Domain Summary: {summary}')
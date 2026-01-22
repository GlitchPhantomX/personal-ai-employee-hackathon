#!/usr/bin/env python3
"""
Gold Tier Integration Tests
"""

import unittest
from pathlib import Path
import os
import sys

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

class TestGoldTier(unittest.TestCase):
    """Test suite for Gold Tier functionality"""

    def setUp(self):
        self.vault = Path('AI_Employee_Vault')
        self.project_root = Path(__file__).parent.parent

    def test_01_cross_domain_integration(self):
        """Test cross-domain dashboard exists"""
        dashboard = self.vault / 'Cross_Domain_Dashboard.md'
        self.assertTrue(dashboard.exists(), f"Cross-Domain Dashboard should exist at {dashboard}")

        # Check that it contains expected sections
        content = dashboard.read_text(encoding='utf-8')
        self.assertIn('Personal Affairs Status', content)
        self.assertIn('Business Affairs Status', content)
        self.assertIn('Integration Health', content)

    def test_02_xero_integration_components(self):
        """Test Xero components exist"""
        # Check Xero watcher exists
        xero_watcher = Path('watchers') / 'xero_watcher.py'
        self.assertTrue(xero_watcher.exists(), f"Xero watcher should exist at {xero_watcher}")

        # Check Xero MCP server exists
        xero_server_dir = Path('mcp_servers') / 'xero_server'
        self.assertTrue(xero_server_dir.exists(), f"Xero server directory should exist at {xero_server_dir}")

        # Check Xero skill exists
        xero_skill = self.vault / 'Skills' / 'xero_accountant.md'
        self.assertTrue(xero_skill.exists(), f"Xero accountant skill should exist at {xero_skill}")

        # Check Xero server files
        xero_index = xero_server_dir / 'index.js'
        xero_package = xero_server_dir / 'package.json'
        xero_readme = xero_server_dir / 'README.md'

        self.assertTrue(xero_index.exists(), "Xero server index.js should exist")
        self.assertTrue(xero_package.exists(), "Xero server package.json should exist")
        self.assertTrue(xero_readme.exists(), "Xero server README.md should exist")

    def test_03_social_media_integration(self):
        """Test Facebook/Instagram integration"""
        # Check social media watcher exists
        social_watcher = Path('watchers') / 'social_media_watcher.py'
        self.assertTrue(social_watcher.exists(), f"Social media watcher should exist at {social_watcher}")

        # Check social media MCP server exists
        social_server = Path('mcp_servers') / 'social_media_server' / 'index.js'
        self.assertTrue(social_server.exists(), f"Social media server should exist at {social_server}")

        # Check social media skill exists
        social_skill = self.vault / 'Skills' / 'facebook_instagram_manager.md'
        self.assertTrue(social_skill.exists(), f"Facebook/Instagram manager skill should exist at {social_skill}")

    def test_04_twitter_integration(self):
        """Test Twitter integration"""
        # Check Twitter watcher exists
        twitter_watcher = Path('watchers') / 'twitter_watcher.py'
        self.assertTrue(twitter_watcher.exists(), f"Twitter watcher should exist at {twitter_watcher}")

        # Check Twitter MCP server exists
        twitter_server = Path('mcp_servers') / 'twitter_server' / 'index.js'
        self.assertTrue(twitter_server.exists(), f"Twitter server should exist at {twitter_server}")

        # Check Twitter skill exists
        twitter_skill = self.vault / 'Skills' / 'twitter_manager.md'
        self.assertTrue(twitter_skill.exists(), f"Twitter manager skill should exist at {twitter_skill}")

    def test_05_ceo_briefing_system(self):
        """Test CEO briefing system"""
        # Check CEO briefing orchestrator exists
        ceo_orchestrator = Path('orchestration') / 'ceo_briefing_orchestrator.py'
        self.assertTrue(ceo_orchestrator.exists(), f"CEO briefing orchestrator should exist at {ceo_orchestrator}")

        # Check CEO briefing generator skill exists
        ceo_skill = self.vault / 'Skills' / 'ceo_briefing_generator.md'
        self.assertTrue(ceo_skill.exists(), f"CEO briefing generator skill should exist at {ceo_skill}")

    def test_06_all_skills_present(self):
        """Test all Gold tier skills exist"""
        skills = self.vault / 'Skills'
        required_skills = [
            'xero_accountant.md',
            'facebook_instagram_manager.md',
            'twitter_manager.md',
            'ceo_briefing_generator.md',
            'linkedin_poster.md',  # From Silver tier
            'gmail_responder.md',  # From Silver tier
            'file_processor.md',   # From Silver tier
        ]

        for skill in required_skills:
            skill_path = skills / skill
            self.assertTrue(skill_path.exists(), f'{skill} should exist at {skill_path}')

    def test_07_cross_domain_orchestrator(self):
        """Test cross-domain orchestrator exists"""
        cross_domain_orch = Path('orchestration') / 'cross_domain_orchestrator.py'
        self.assertTrue(cross_domain_orch.exists(), f"Cross-domain orchestrator should exist at {cross_domain_orch}")

        # Import and test basic functionality
        from orchestration.cross_domain_orchestrator import CrossDomainOrchestrator
        orchestrator = CrossDomainOrchestrator(str(self.vault))
        self.assertIsNotNone(orchestrator)

    def test_08_error_recovery_system(self):
        """Test error recovery system exists"""
        error_recovery = Path('system') / 'error_recovery.py'
        self.assertTrue(error_recovery.exists(), f"Error recovery system should exist at {error_recovery}")

        # Import and test basic functionality
        from system.error_recovery import ErrorRecoverySystem
        recovery_system = ErrorRecoverySystem(str(self.vault))
        self.assertIsNotNone(recovery_system)

        # Test health check
        health = recovery_system.health_check()
        self.assertIn('system_status', health)
        self.assertIn('timestamp', health)

    def test_09_audit_logging_system(self):
        """Test audit logging system exists"""
        audit_logging = Path('system') / 'audit_logging.py'
        self.assertTrue(audit_logging.exists(), f"Audit logging system should exist at {audit_logging}")

        # Import and test basic functionality
        from system.audit_logging import AuditLogger
        audit_system = AuditLogger(str(self.vault))
        self.assertIsNotNone(audit_system)

        # Test statistics
        stats = audit_system.get_statistics()
        self.assertIn('total_entries', stats)
        self.assertIn('by_event_type', stats)

    def test_10_documentation_exists(self):
        """Test architecture documentation exists"""
        docs_dir = Path('docs')
        arch_doc = docs_dir / 'gold_tier_architecture.md'
        lessons_doc = docs_dir / 'lessons_learned.md'

        self.assertTrue(arch_doc.exists(), f"Architecture documentation should exist at {arch_doc}")
        self.assertTrue(lessons_doc.exists(), f"Lessons learned documentation should exist at {lessons_doc}")

        # Check that docs contain expected content
        arch_content = arch_doc.read_text(encoding='utf-8')
        self.assertIn('Gold Tier Architecture', arch_content)
        self.assertIn('System Architecture', arch_content)

        lessons_content = lessons_doc.read_text(encoding='utf-8')
        self.assertIn('Lessons Learned', lessons_content)
        self.assertIn('Technical Lessons', lessons_content)

    def test_11_mcp_servers_structure(self):
        """Test MCP server structure is correct"""
        mcp_servers = Path('mcp_servers')
        self.assertTrue(mcp_servers.exists(), "MCP servers directory should exist")

        expected_servers = ['xero_server', 'social_media_server', 'twitter_server', 'gmail_server', 'linkedin_server', 'browser_server']

        for server in expected_servers:
            server_dir = mcp_servers / server
            self.assertTrue(server_dir.exists(), f"MCP server {server} should exist")

            # Check for index.js in each server
            index_js = server_dir / 'index.js'
            self.assertTrue(index_js.exists(), f"index.js should exist in {server}")

    def test_12_folder_structure(self):
        """Test overall project structure"""
        expected_dirs = [
            'watchers',
            'orchestration',
            'mcp_servers',
            'AI_Employee_Vault/Skills',
            'AI_Employee_Vault/Briefings',
            'AI_Employee_Vault/Logs',
            'AI_Employee_Vault/Errors',
            'AI_Employee_Vault/Audit_Logs',
            'system',
            'docs',
            'tests'
        ]

        for dir_path in expected_dirs:
            full_path = self.project_root / dir_path
            self.assertTrue(full_path.exists(), f"Directory {dir_path} should exist")

    def test_13_config_files_exist(self):
        """Test configuration files exist"""
        expected_configs = [
            'AI_Employee_Vault/social_media_schedule.json',
            'AI_Employee_Vault/twitter_schedule.json'
        ]

        for config in expected_configs:
            config_path = self.project_root / config
            self.assertTrue(config_path.exists(), f"Configuration file {config} should exist")

def run_tests():
    """Run the Gold Tier test suite"""
    print("="*60)
    print("Gold Tier Integration Tests")
    print("="*60)
    print()

    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGoldTier)

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print()
    print("="*60)
    print("Test Results Summary:")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%" if result.testsRun > 0 else "0%")
    print("="*60)

    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
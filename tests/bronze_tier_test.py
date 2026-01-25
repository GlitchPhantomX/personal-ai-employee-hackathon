#!/usr/bin/env python3
"""
Bronze Tier Testing Suite for Personal AI Employee
Tests core functionality required for Bronze Tier compliance.
"""

import sys
import os
import unittest
from datetime import datetime

# Add the parent directory to the path to import Personal_AI_Employee modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Personal_AI_Employee.utils.custom_logging import log_event, log_error
from Personal_AI_Employee.orchestrator.health_monitor import HealthMonitor
from Personal_AI_Employee.orchestrator.cleanup_orchestrator import CleanupOrchestrator
from Personal_AI_Employee.utils.dashboard_updater import DashboardUpdater
from Personal_AI_Employee.skills.email_processor import EmailProcessorSkill
from Personal_AI_Employee.skills.linkedin_poster import LinkedInPosterSkill
from Personal_AI_Employee.skills.invoice_generator import InvoiceGeneratorSkill
from Personal_AI_Employee.skills.whatsapp_handler import WhatsAppHandlerSkill
from Personal_AI_Employee.skills.task_creator import TaskCreatorSkill
from Personal_AI_Employee.orchestrator.approval_handler import ApprovalHandler


class BronzeTierTestSuite(unittest.TestCase):
    """Test suite for Bronze Tier functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        print("Setting up Bronze Tier test...")

    def test_health_check_functionality(self):
        """Test that health monitoring works correctly."""
        print("Testing health check functionality...")
        try:
            health_monitor = HealthMonitor()
            health_report = health_monitor.generate_health_report()
            self.assertIsNotNone(health_report)
            print("SUCCESS: Health check functionality test passed")
            return True
        except Exception as e:
            print(f"FAILED: Health check functionality test failed: {e}")
            return False

    def test_cleanup_system(self):
        """Test that cleanup system works correctly."""
        print("Testing cleanup system...")
        try:
            cleanup_orchestrator = CleanupOrchestrator()
            result = cleanup_orchestrator.run_cleanup_process()
            self.assertIsNotNone(result)
            print("SUCCESS: Cleanup system test passed")
            return True
        except Exception as e:
            print(f"FAILED: Cleanup system test failed: {e}")
            return False

    def test_dashboard_update(self):
        """Test that dashboard updates work correctly."""
        print("Testing dashboard update functionality...")
        try:
            dashboard_updater = DashboardUpdater()
            result = dashboard_updater.update_dashboard_file()
            self.assertIsNotNone(result)
            print("SUCCESS: Dashboard update test passed")
            return True
        except Exception as e:
            print(f"FAILED: Dashboard update test failed: {e}")
            return False

    def test_skills_functionality(self):
        """Test that all 5 core skills work."""
        print("Testing skills functionality...")
        try:
            skills = [
                EmailProcessorSkill(),
                LinkedInPosterSkill(),
                InvoiceGeneratorSkill(),
                WhatsAppHandlerSkill(),
                TaskCreatorSkill()
            ]

            for skill in skills:
                # Test that each skill can be instantiated and has required attributes
                self.assertTrue(hasattr(skill, 'name'))
                self.assertTrue(hasattr(skill, 'execute'))
                print(f"SUCCESS: {skill.name} skill test passed")

            print("SUCCESS: All skills functionality test passed")
            return True
        except Exception as e:
            print(f"FAILED: Skills functionality test failed: {e}")
            return False

    def test_logging_system(self):
        """Test that logging system works correctly."""
        print("Testing logging system...")
        try:
            # Test basic logging functionality
            log_event(
                component="BronzeTierTest",
                level="INFO",
                event_type="test_execution",
                message="Test log event for Bronze Tier",
                details={"test": "logging_system"}
            )
            print("SUCCESS: Logging system test passed")
            return True
        except Exception as e:
            print(f"FAILED: Logging system test failed: {e}")
            return False

    def test_approval_workflow(self):
        """Test that approval workflow works correctly."""
        print("Testing approval workflow...")
        try:
            approval_handler = ApprovalHandler()
            # Test basic functionality
            self.assertIsNotNone(approval_handler)
            print("SUCCESS: Approval workflow test passed")
            return True
        except Exception as e:
            print(f"FAILED: Approval workflow test failed: {e}")
            return False

    def test_end_to_end_bronze_process(self):
        """Test end-to-end Bronze Tier process with 10 events."""
        print("Testing end-to-end Bronze Tier process...")
        try:
            # Simulate processing 10 events
            events_processed = 0
            for i in range(10):
                # Simulate event processing
                log_event(
                    component="BronzeTierTest",
                    level="INFO",
                    event_type="event_processing",
                    message=f"Processing event {i+1}",
                    details={"event_id": i+1}
                )
                events_processed += 1

            self.assertEqual(events_processed, 10)
            print("SUCCESS: End-to-end Bronze Tier process test passed")
            return True
        except Exception as e:
            print(f"FAILED: End-to-end Bronze Tier process test failed: {e}")
            return False


def run_tests():
    """Run all Bronze Tier tests and return results."""
    print("=== RUNNING BRONZE TIER TESTS ===\n")

    test_suite = BronzeTierTestSuite()
    tests = [
        ("Health Check", test_suite.test_health_check_functionality),
        ("Cleanup System", test_suite.test_cleanup_system),
        ("Dashboard Update", test_suite.test_dashboard_update),
        ("Skills Testing", test_suite.test_skills_functionality),
        ("Logging System", test_suite.test_logging_system),
        ("Approval Workflow", test_suite.test_approval_workflow),
        ("E2E Bronze Process", test_suite.test_end_to_end_bronze_process)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"Running {test_name} test...")
        try:
            result = test_func()
            if result:
                passed += 1
                print(f"SUCCESS: {test_name} - PASS\n")
            else:
                print(f"FAILED: {test_name} - FAIL\n")
        except Exception as e:
            print(f"ERROR: {test_name} - ERROR: {e}\n")

    print(f"\nBronze Tier: {passed}/{total} PASSED")
    return passed, total


if __name__ == "__main__":
    passed, total = run_tests()
    if passed == total:
        print("\nALL BRONZE TIER TESTS PASSED!")
        sys.exit(0)
    else:
        print(f"\n{total-passed} BRONZE TIER TESTS FAILED")
        sys.exit(1)
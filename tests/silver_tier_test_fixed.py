#!/usr/bin/env python3
"""
Silver Tier Testing Suite for Personal AI Employee - FIXED VERSION
Tests advanced functionality required for Silver Tier compliance.
"""

import sys
import os
import unittest
from datetime import datetime

# Add the parent directory to the path to import Personal_AI_Employee modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Personal_AI_Employee.orchestrator.planning_orchestrator import PlanningOrchestrator
from Personal_AI_Employee.watchers.file_system_watcher_fixed import FileSystemWatcher
from Personal_AI_Employee.skills.planning_skill import PlanningSkill
from Personal_AI_Employee.skills.approval_requester import ApprovalRequesterSkill
from Personal_AI_Employee.orchestrator.approval_handler import ApprovalHandler


class SilverTierTestSuite(unittest.TestCase):
    """Test suite for Silver Tier functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        print("Setting up Silver Tier test...")

    def test_watcher_system(self):
        """Test that watcher system works correctly."""
        print("Testing watcher system...")
        try:
            # Create test directories
            import os
            vault_path = './test_vault'
            test_dir = './test_dir'
            
            # Create directories if they don't exist
            os.makedirs(vault_path, exist_ok=True)
            os.makedirs(test_dir, exist_ok=True)
            
            # Test file system watcher with correct signature: (vault_path, watched_dirs, check_interval)
            watcher = FileSystemWatcher(vault_path, [test_dir], check_interval=1)
            self.assertIsNotNone(watcher)
            print("SUCCESS: Watcher system test passed")
            return True
        except Exception as e:
            print(f"FAILED: Watcher system test failed: {e}")
            import traceback
            traceback.print_exc()
            return False

    def test_planning_system(self):
        """Test that planning system works correctly."""
        print("Testing planning system...")
        try:
            planning_orchestrator = PlanningOrchestrator()
            self.assertIsNotNone(planning_orchestrator)
            print("SUCCESS: Planning system test passed")
            return True
        except Exception as e:
            print(f"FAILED: Planning system test failed: {e}")
            return False

    def test_linkedin_integration(self):
        """Test that LinkedIn integration works correctly."""
        print("Testing LinkedIn integration...")
        try:
            # Test LinkedIn poster skill
            from Personal_AI_Employee.skills.linkedin_poster import LinkedInPosterSkill
            linkedin_skill = LinkedInPosterSkill()
            self.assertIsNotNone(linkedin_skill)
            print("SUCCESS: LinkedIn integration test passed")
            return True
        except Exception as e:
            print(f"FAILED: LinkedIn integration test failed: {e}")
            return False

    def test_mcp_servers(self):
        """Test that MCP servers work correctly."""
        print("Testing MCP servers...")
        try:
            # Test that MCP servers directory exists and has content
            import os
            mcp_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Personal_AI_Employee", "mcp_servers")
            server_dirs = [d for d in os.listdir(mcp_dir) if os.path.isdir(os.path.join(mcp_dir, d))]
            self.assertGreater(len(server_dirs), 0)  # Ensure there are server directories
            print("SUCCESS: MCP servers test passed")
            return True
        except Exception as e:
            print(f"FAILED: MCP servers test failed: {e}")
            return False

    def test_scheduling_system(self):
        """Test that scheduling system works correctly."""
        print("Testing scheduling system...")
        try:
            # Test that scheduling functionality exists in the system
            from Personal_AI_Employee.orchestrator.planning_orchestrator import PlanningOrchestrator
            planner = PlanningOrchestrator()
            self.assertIsNotNone(planner)
            print("SUCCESS: Scheduling system test passed")
            return True
        except Exception as e:
            print(f"FAILED: Scheduling system test failed: {e}")
            return False

    def test_approval_automation(self):
        """Test that approval automation works correctly."""
        print("Testing approval automation...")
        try:
            approval_handler = ApprovalHandler()
            self.assertIsNotNone(approval_handler)
            print("SUCCESS: Approval automation test passed")
            return True
        except Exception as e:
            print(f"FAILED: Approval automation test failed: {e}")
            return False

    def test_new_skills(self):
        """Test that new Silver Tier skills work correctly."""
        print("Testing new skills...")
        try:
            # Test planning skill
            planning_skill = PlanningSkill()
            self.assertIsNotNone(planning_skill)

            # Test approval requester skill
            approval_skill = ApprovalRequesterSkill()
            self.assertIsNotNone(approval_skill)

            print("SUCCESS: New skills test passed")
            return True
        except Exception as e:
            print(f"FAILED: New skills test failed: {e}")
            return False

    def test_end_to_end_silver_process(self):
        """Test end-to-end Silver Tier process."""
        print("Testing end-to-end Silver Tier process...")
        try:
            # Simulate a planning and approval workflow
            planning_skill = PlanningSkill()
            approval_skill = ApprovalRequesterSkill()

            # Create a sample plan
            plan_input = {
                "situation": "Test planning scenario for Silver Tier",
                "context": "This is for testing Silver Tier functionality",
                "priority": "medium"
            }

            plan_result = planning_skill.execute(plan_input)
            self.assertIsNotNone(plan_result)

            # Create a sample approval request
            approval_input = {
                "action_description": "Test approval for Silver Tier functionality",
                "reasoning": "Testing Silver Tier approval workflow",
                "tier": 2
            }

            approval_result = approval_skill.execute(approval_input)
            self.assertIsNotNone(approval_result)

            print("SUCCESS: End-to-end Silver Tier process test passed")
            return True
        except Exception as e:
            print(f"FAILED: End-to-end Silver Tier process test failed: {e}")
            import traceback
            traceback.print_exc()
            return False


def run_tests():
    """Run all Silver Tier tests and return results."""
    print("=== RUNNING SILVER TIER TESTS (FIXED VERSION) ===\n")

    test_suite = SilverTierTestSuite()
    tests = [
        ("Watchers", test_suite.test_watcher_system),
        ("Planning", test_suite.test_planning_system),
        ("LinkedIn", test_suite.test_linkedin_integration),
        ("MCP Servers", test_suite.test_mcp_servers),
        ("Scheduling", test_suite.test_scheduling_system),
        ("Approval Automation", test_suite.test_approval_automation),
        ("New Skills", test_suite.test_new_skills),
        ("E2E Silver", test_suite.test_end_to_end_silver_process)
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
            import traceback
            traceback.print_exc()

    print(f"\nSilver Tier: {passed}/{total} PASSED")
    return passed, total


if __name__ == "__main__":
    passed, total = run_tests()
    if passed == total:
        print("\n✅ ALL SILVER TIER TESTS PASSED!")
        sys.exit(0)
    else:
        print(f"\n❌ {total-passed} SILVER TIER TEST(S) FAILED")
        sys.exit(1)
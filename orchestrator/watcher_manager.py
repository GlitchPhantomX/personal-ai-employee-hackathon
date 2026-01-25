#!/usr/bin/env python3
"""
Watcher Manager for Personal AI Employee
Manages watcher lifecycle with CLI interface.
"""

import argparse
import sys
import os
from typing import Dict, List, Optional

# Add the parent directory to the path to import Personal_AI_Employee modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Personal_AI_Employee.watchers.file_system_watcher import FileSystemWatcher
from Personal_AI_Employee.watchers.gmail_watcher import GmailWatcher
from Personal_AI_Employee.watchers.base_watcher import BaseWatcher


class WatcherManager:
    """Manages multiple watchers with start/stop/restart functionality."""

    def __init__(self):
        self.watchers: Dict[str, BaseWatcher] = {}
        self._initialize_watchers()

    def _initialize_watchers(self):
        """Initialize default watchers."""
        try:
            # Initialize file system watcher
            fs_watcher = FileSystemWatcher(
                watched_dirs=[os.path.join("AI_Employee_Vault", "Needs_Action")],
                poll_interval=5
            )
            self.watchers["file_system"] = fs_watcher

            # Initialize other watchers as needed
            print("SUCCESS: Watchers initialized successfully")
        except Exception as e:
            print(f"FAILED: Error initializing watchers: {e}")

    def list_watcher_status(self) -> Dict[str, str]:
        """Show status of all watchers."""
        status_report = {}
        for name, watcher in self.watchers.items():
            status = "RUNNING" if watcher.is_running else "STOPPED"
            status_report[name] = status
        return status_report

    def start_watcher(self, watcher_name: str) -> bool:
        """Start a specific watcher."""
        if watcher_name not in self.watchers:
            print(f"❌ Watcher '{watcher_name}' not found")
            return False

        try:
            self.watchers[watcher_name].start()
            print(f"SUCCESS: Watcher '{watcher_name}' started successfully")
            return True
        except Exception as e:
            print(f"FAILED: Error starting watcher '{watcher_name}': {e}")
            return False

    def stop_watcher(self, watcher_name: str) -> bool:
        """Stop a specific watcher."""
        if watcher_name not in self.watchers:
            print(f"FAILED: Watcher '{watcher_name}' not found")
            return False

        try:
            self.watchers[watcher_name].stop()
            print(f"SUCCESS: Watcher '{watcher_name}' stopped successfully")
            return True
        except Exception as e:
            print(f"FAILED: Error stopping watcher '{watcher_name}': {e}")
            return False

    def restart_watcher(self, watcher_name: str) -> bool:
        """Restart a specific watcher."""
        if watcher_name not in self.watchers:
            print(f"FAILED: Watcher '{watcher_name}' not found")
            return False

        try:
            self.watchers[watcher_name].restart()
            print(f"SUCCESS: Watcher '{watcher_name}' restarted successfully")
            return True
        except Exception as e:
            print(f"FAILED: Error restarting watcher '{watcher_name}': {e}")
            return False

    def start_all_watchers(self) -> bool:
        """Start all watchers."""
        success = True
        for name in self.watchers.keys():
            if not self.start_watcher(name):
                success = False
        return success

    def stop_all_watchers(self) -> bool:
        """Stop all watchers."""
        success = True
        for name in self.watchers.keys():
            if not self.stop_watcher(name):
                success = False
        return success


def main():
    """Command line interface for watcher management."""
    parser = argparse.ArgumentParser(description="Watcher Manager for Personal AI Employee")
    parser.add_argument("--status", action="store_true", help="Show all watcher status")
    parser.add_argument("--start", type=str, help="Start specific watcher by name")
    parser.add_argument("--stop", type=str, help="Stop specific watcher by name")
    parser.add_argument("--restart", type=str, help="Restart specific watcher by name")
    parser.add_argument("--start-all", action="store_true", help="Start all watchers")
    parser.add_argument("--stop-all", action="store_true", help="Stop all watchers")

    args = parser.parse_args()

    manager = WatcherManager()

    if args.status:
        print("=== WATCHER STATUS ===")
        status_report = manager.list_watcher_status()
        for name, status in status_report.items():
            print(f"{name}: {status}")
        return 0

    if args.start:
        print(f"Starting watcher: {args.start}")
        success = manager.start_watcher(args.start)
        return 0 if success else 1

    if args.stop:
        print(f"Stopping watcher: {args.stop}")
        success = manager.stop_watcher(args.stop)
        return 0 if success else 1

    if args.restart:
        print(f"Restarting watcher: {args.restart}")
        success = manager.restart_watcher(args.restart)
        return 0 if success else 1

    if args.start_all:
        print("Starting all watchers...")
        success = manager.start_all_watchers()
        return 0 if success else 1

    if args.stop_all:
        print("Stopping all watchers...")
        success = manager.stop_all_watchers()
        return 0 if success else 1

    # If no arguments provided, show help
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
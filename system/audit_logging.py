#!/usr/bin/env python3
"""
Comprehensive Audit Logging System
Tracks all system activities, user interactions, and system changes
"""

import logging
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
import threading
import queue
from dataclasses import dataclass, asdict
from enum import Enum

class AuditEventType(Enum):
    """Types of audit events"""
    SYSTEM_STARTUP = "system_startup"
    SYSTEM_SHUTDOWN = "system_shutdown"
    USER_ACTION = "user_action"
    FILE_CREATED = "file_created"
    FILE_MODIFIED = "file_modified"
    FILE_DELETED = "file_deleted"
    PERMISSION_GRANTED = "permission_granted"
    PERMISSION_DENIED = "permission_denied"
    DATA_ACCESS = "data_access"
    CONFIG_CHANGE = "config_change"
    ERROR_OCCURRED = "error_occurred"
    APPROVAL_GRANTED = "approval_granted"
    APPROVAL_DENIED = "approval_denied"
    MCP_CALL = "mcp_call"
    MCP_RESPONSE = "mcp_response"
    SOCIAL_POST = "social_post"
    INVOICE_CREATED = "invoice_created"
    EXPENSE_RECORDED = "expense_recorded"

@dataclass
class AuditEntry:
    """Structure for audit log entries"""
    timestamp: str
    event_type: str
    user_id: Optional[str]
    action: str
    resource: str
    ip_address: Optional[str]
    user_agent: Optional[str]
    metadata: Dict[str, Any]
    severity: str = "info"

class AuditLogger:
    """
    Comprehensive audit logging system
    """

    def __init__(self, vault_path: str, max_log_size: int = 10 * 1024 * 1024):  # 10MB
        self.vault_path = Path(vault_path)
        self.audit_dir = self.vault_path / 'Audit_Logs'
        self.max_log_size = max_log_size

        # Create audit directory
        self.audit_dir.mkdir(exist_ok=True)

        # Setup logging
        self.logger = logging.getLogger('AuditLogger')
        self.logger.setLevel(logging.INFO)

        # File handler for audit logs
        self.audit_file = self.audit_dir / f'audit_{datetime.now().strftime("%Y%m%d")}.log'
        self.file_handler = logging.FileHandler(self.audit_file, encoding='utf-8')
        self.file_handler.setFormatter(
            logging.Formatter('%(asctime)s - AUDIT - %(message)s')
        )
        self.logger.addHandler(self.file_handler)

        # Queue for asynchronous logging
        self.log_queue = queue.Queue()
        self.worker_thread = threading.Thread(target=self._process_log_queue, daemon=True)
        self.worker_thread.start()

        self.logger.info('Audit Logger initialized')

    def log_event(self, event_type: AuditEventType, user_id: str = None, action: str = "",
                  resource: str = "", ip_address: str = None, user_agent: str = None,
                  metadata: Dict[str, Any] = None, severity: str = "info"):
        """
        Log an audit event
        """
        if metadata is None:
            metadata = {}

        entry = AuditEntry(
            timestamp=datetime.now().isoformat(),
            event_type=event_type.value,
            user_id=user_id,
            action=action,
            resource=resource,
            ip_address=ip_address,
            user_agent=user_agent,
            metadata=metadata,
            severity=severity
        )

        # Add to queue for async processing
        self.log_queue.put(entry)

    def _process_log_queue(self):
        """
        Process log entries from queue asynchronously
        """
        while True:
            try:
                entry = self.log_queue.get(timeout=1)
                self._write_log_entry(entry)
                self.log_queue.task_done()
            except queue.Empty:
                continue

    def _write_log_entry(self, entry: AuditEntry):
        """
        Write audit entry to log file
        """
        try:
            # Rotate log file if it's too large
            if self.audit_file.exists() and self.audit_file.stat().st_size > self.max_log_size:
                self._rotate_log_file()

            # Create JSON log entry
            log_data = {
                'timestamp': entry.timestamp,
                'event_type': entry.event_type,
                'user_id': entry.user_id,
                'action': entry.action,
                'resource': entry.resource,
                'ip_address': entry.ip_address,
                'user_agent': entry.user_agent,
                'metadata': entry.metadata,
                'severity': entry.severity
            }

            # Write to file
            with open(self.audit_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_data) + '\n')

            # Also write to standard logger for immediate visibility
            self.logger.info(f"AUDIT: {entry.event_type} - {entry.action} - {entry.resource}")

        except Exception as e:
            print(f"Error writing audit log: {e}")

    def _rotate_log_file(self):
        """
        Rotate log file to prevent it from getting too large
        """
        old_file = self.audit_file
        new_filename = f'audit_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        rotated_file = self.audit_dir / new_filename
        old_file.rename(rotated_file)

        # Create new log file
        self.audit_file = self.audit_dir / f'audit_{datetime.now().strftime("%Y%m%d")}.log'
        self.file_handler.close()
        self.file_handler = logging.FileHandler(self.audit_file, encoding='utf-8')
        self.file_handler.setFormatter(
            logging.Formatter('%(asctime)s - AUDIT - %(message)s')
        )
        self.logger.addHandler(self.file_handler)

    def search_logs(self, start_date: str = None, end_date: str = None,
                   event_types: list = None, severity: str = None) -> list:
        """
        Search audit logs with filters
        """
        results = []

        # Find relevant log files
        log_files = list(self.audit_dir.glob('audit_*.log'))

        for log_file in log_files:
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            try:
                                log_entry = json.loads(line.strip())

                                # Apply filters
                                if start_date and log_entry['timestamp'] < start_date:
                                    continue
                                if end_date and log_entry['timestamp'] > end_date:
                                    continue
                                if event_types and log_entry['event_type'] not in event_types:
                                    continue
                                if severity and log_entry['severity'] != severity:
                                    continue

                                results.append(log_entry)
                            except json.JSONDecodeError:
                                continue
            except Exception as e:
                print(f"Error reading log file {log_file}: {e}")

        return results

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get audit log statistics
        """
        stats = {
            'total_entries': 0,
            'by_event_type': {},
            'by_severity': {},
            'date_range': {'start': None, 'end': None},
            'recent_activity': []
        }

        # Find relevant log files
        log_files = list(self.audit_dir.glob('audit_*.log'))

        for log_file in log_files:
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            try:
                                log_entry = json.loads(line.strip())

                                stats['total_entries'] += 1

                                # Count by event type
                                event_type = log_entry['event_type']
                                stats['by_event_type'][event_type] = stats['by_event_type'].get(event_type, 0) + 1

                                # Count by severity
                                severity = log_entry['severity']
                                stats['by_severity'][severity] = stats['by_severity'].get(severity, 0) + 1

                                # Track date range
                                if not stats['date_range']['start'] or log_entry['timestamp'] < stats['date_range']['start']:
                                    stats['date_range']['start'] = log_entry['timestamp']
                                if not stats['date_range']['end'] or log_entry['timestamp'] > stats['date_range']['end']:
                                    stats['date_range']['end'] = log_entry['timestamp']

                            except json.JSONDecodeError:
                                continue
            except Exception as e:
                print(f"Error reading log file {log_file}: {e}")

        # Get recent activity (last 10 entries)
        recent_logs = self.search_logs()
        stats['recent_activity'] = recent_logs[-10:] if recent_logs else []

        return stats

    def export_logs(self, filename: str, start_date: str = None, end_date: str = None) -> Path:
        """
        Export audit logs to a file
        """
        export_path = self.audit_dir / f'export_{filename}.json'

        logs = self.search_logs(start_date=start_date, end_date=end_date)

        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2)

        return export_path

# Global audit logger instance
_audit_logger = None

def get_audit_logger(vault_path: str = None) -> AuditLogger:
    """
    Get singleton instance of audit logger
    """
    global _audit_logger
    if _audit_logger is None and vault_path:
        _audit_logger = AuditLogger(vault_path)
    return _audit_logger

def audit_event(event_type: AuditEventType, user_id: str = None, action: str = "",
               resource: str = "", ip_address: str = None, user_agent: str = None,
               metadata: Dict[str, Any] = None, severity: str = "info"):
    """
    Convenience function to log audit events
    """
    logger = get_audit_logger()
    if logger:
        logger.log_event(event_type, user_id, action, resource, ip_address, user_agent, metadata, severity)

# Example usage and testing
if __name__ == '__main__':
    # Initialize audit logger
    audit_logger = AuditLogger('../AI_Employee_Vault')

    print("Testing audit logging system...")

    # Log some sample events
    audit_logger.log_event(
        AuditEventType.SYSTEM_STARTUP,
        user_id="system",
        action="Starting AI Employee System",
        resource="orchestration/enhanced_orchestrator.py",
        metadata={"version": "Gold Tier", "features": ["xero", "social_media", "twitter"]}
    )

    audit_logger.log_event(
        AuditEventType.USER_ACTION,
        user_id="admin",
        action="Created new social media post",
        resource="Needs_Action/FACEBOOK_20260114_post_request.md",
        metadata={"platform": "facebook", "content_type": "update"}
    )

    audit_logger.log_event(
        AuditEventType.MCP_CALL,
        user_id="system",
        action="Called Xero API",
        resource="mcp_servers/xero_server",
        metadata={"method": "create_invoice", "success": True}
    )

    # Get statistics
    stats = audit_logger.get_statistics()
    print(f"Total audit entries: {stats['total_entries']}")
    print(f"Event types: {list(stats['by_event_type'].keys())}")
    print(f"Severity distribution: {stats['by_severity']}")

    # Search logs
    recent_logs = audit_logger.search_logs(severity="info")
    print(f"Found {len(recent_logs)} info-level events")

    print("Audit logging system initialized successfully!")
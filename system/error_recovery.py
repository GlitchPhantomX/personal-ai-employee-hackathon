#!/usr/bin/env python3
"""
Error Recovery and Graceful Degradation System
Handles error detection, recovery, and fallback mechanisms
"""

import logging
import traceback
from pathlib import Path
from datetime import datetime
import time
import json
from typing import Callable, Any, Optional
from functools import wraps

class ErrorRecoverySystem:
    """
    Comprehensive error recovery and graceful degradation system
    """

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.errors_dir = self.vault_path / 'Errors'
        self.backup_dir = self.vault_path / 'Backups'

        # Create necessary directories
        self.errors_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)

        self.logger = logging.getLogger('ErrorRecovery')

        # Error tracking
        self.error_history = []
        self.max_error_history = 100

        self.logger.info('Error Recovery System initialized')

    def log_error(self, error: Exception, context: str = "", severity: str = "error"):
        """
        Log an error with context and severity
        """
        error_entry = {
            'timestamp': datetime.now().isoformat(),
            'context': context,
            'severity': severity,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'traceback': traceback.format_exc()
        }

        # Add to history
        self.error_history.append(error_entry)
        if len(self.error_history) > self.max_error_history:
            self.error_history.pop(0)

        # Save to error log file
        error_file = self.errors_dir / f'error_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(error_file, 'w', encoding='utf-8') as f:
            json.dump(error_entry, f, indent=2)

        # Log to standard logger
        self.logger.error(f"[{severity.upper()}] {context}: {str(error)}")

    def retry_on_failure(self, max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
        """
        Decorator for retrying functions that fail
        """
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None

                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        self.log_error(e, f"{func.__name__} attempt {attempt + 1}/{max_attempts}")

                        if attempt < max_attempts - 1:  # Don't sleep on last attempt
                            time.sleep(delay * (backoff ** attempt))

                raise last_exception
            return wrapper
        return decorator

    def create_backup(self, file_path: Path) -> Optional[Path]:
        """
        Create a backup of a file
        """
        try:
            if not file_path.exists():
                return None

            backup_path = self.backup_dir / f"{file_path.name}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
            backup_path.write_text(file_path.read_text(encoding='utf-8'), encoding='utf-8')

            self.logger.info(f'Backup created: {backup_path}')
            return backup_path
        except Exception as e:
            self.log_error(e, f"Failed to create backup for {file_path}")
            return None

    def recover_from_backup(self, original_path: Path) -> bool:
        """
        Recover a file from the most recent backup
        """
        try:
            # Find the most recent backup
            backups = list(self.backup_dir.glob(f"{original_path.name}.*.bak"))
            if not backups:
                self.logger.warning(f'No backup found for {original_path}')
                return False

            # Sort by modification time (most recent first)
            latest_backup = max(backups, key=lambda x: x.stat().st_mtime)

            # Restore from backup
            original_path.write_text(latest_backup.read_text(encoding='utf-8'), encoding='utf-8')
            self.logger.info(f'Recovered {original_path} from {latest_backup}')

            return True
        except Exception as e:
            self.log_error(e, f"Failed to recover {original_path} from backup")
            return False

    def graceful_degrade(self, primary_func: Callable, fallback_func: Callable, *args, **kwargs) -> Any:
        """
        Execute primary function, fall back to secondary if primary fails
        """
        try:
            return primary_func(*args, **kwargs)
        except Exception as e:
            self.log_error(e, f"Primary function failed, using fallback: {primary_func.__name__}")
            try:
                return fallback_func(*args, **kwargs)
            except Exception as fallback_error:
                self.log_error(fallback_error, f"Fallback function also failed: {fallback_func.__name__}")
                raise e  # Re-raise original error

    def health_check(self) -> dict:
        """
        Perform system health check
        """
        total_errors = len(self.error_history) if self.error_history else 0
        recent_errors_count = len(self.error_history[-10:]) if self.error_history else 0
        last_100_errors_count = len(self.error_history[-100:]) if self.error_history else 0

        error_rate = last_100_errors_count / min(total_errors, 100) if total_errors > 0 else 0

        health_status = {
            'timestamp': datetime.now().isoformat(),
            'services': {},
            'recent_errors': recent_errors_count,  # Last 10 errors
            'error_rate': error_rate,  # Error rate in last 100
            'system_status': 'healthy' if recent_errors_count == 0 else 'degraded'
        }

        # Check if recent errors indicate system issues
        recent_error_count = len(self.error_history[-10:]) if self.error_history else 0
        if recent_error_count > 5:  # More than 5 errors in last 10
            health_status['system_status'] = 'critical'
        elif recent_error_count > 2:  # More than 2 errors in last 10
            health_status['system_status'] = 'warning'

        return health_status

    def get_error_summary(self) -> dict:
        """
        Get summary of recent errors
        """
        if not self.error_history:
            return {'total_errors': 0, 'recent_errors': [], 'by_severity': {}}

        recent_errors = self.error_history[-10:]  # Last 10 errors
        by_severity = {}
        by_type = {}

        for error in self.error_history[-100:]:  # Analyze last 100 errors
            severity = error['severity']
            error_type = error['error_type']

            by_severity[severity] = by_severity.get(severity, 0) + 1
            by_type[error_type] = by_type.get(error_type, 0) + 1

        return {
            'total_errors': len(self.error_history),
            'recent_errors': recent_errors,
            'by_severity': by_severity,
            'by_type': by_type,
            'most_common_errors': sorted(by_type.items(), key=lambda x: x[1], reverse=True)[:5]
        }

def enhanced_error_handler(func: Callable) -> Callable:
    """
    Decorator to enhance error handling for any function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Log the error
            import logging
            logger = logging.getLogger(func.__module__)
            logger.error(f"Error in {func.__name__}: {str(e)}")
            logger.error(f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception
            raise e
    return wrapper

# Example usage and testing
if __name__ == '__main__':
    # Initialize error recovery system
    recovery_system = ErrorRecoverySystem('../AI_Employee_Vault')

    # Example of using retry decorator
    @recovery_system.retry_on_failure(max_attempts=3, delay=0.5)
    def unreliable_function():
        import random
        if random.random() < 0.7:  # 70% chance of failure
            raise Exception("Random failure for testing")
        return "Success!"

    # Example of using graceful degradation
    def primary_operation():
        raise Exception("Primary operation failed")

    def fallback_operation():
        return "Fallback operation succeeded"

    print("Testing error recovery system...")

    # Test health check
    health = recovery_system.health_check()
    print(f"Health status: {health['system_status']}")

    # Test error summary
    summary = recovery_system.get_error_summary()
    print(f"Error summary: {summary['total_errors']} total errors")

    # Test graceful degradation
    try:
        result = recovery_system.graceful_degrade(primary_operation, fallback_operation)
        print(f"Graceful degradation result: {result}")
    except Exception as e:
        print(f"Even fallback failed: {e}")

    print("Error recovery system initialized successfully!")
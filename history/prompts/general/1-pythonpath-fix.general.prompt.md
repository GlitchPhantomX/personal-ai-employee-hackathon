---
id: 1
title: "PYTHONPATH Fix for Import Issues"
stage: "general"
date_iso: "2026-01-24"
surface: "agent"
model: "Claude Sonnet 4.5"
feature: "none"
branch: "001-silver-tier-enhancement"
user: "user"
command: "python-path-fix"
labels: ["python", "imports", "fix", "path"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "Personal_AI_Employee/watchers/base_watcher.py"
  - "Personal_AI_Employee/watchers/gmail_watcher.py"
  - "Personal_AI_Employee/watchers/linkedin_watcher.py"
  - "Personal_AI_Employee/watchers/file_system_watcher.py"
  - "Personal_AI_Employee/orchestrator/approval_handler.py"
tests_yaml: []
---

# PYTHONPATH Fix for Import Issues

## PROMPT_TEXT

FINAL FIX - GUARANTEED TO WORK

THE REAL PROBLEM: The `Personal_AI_Employee` module is not in Python's path when running scripts directly.

THE SIMPLE SOLUTION: Add PYTHONPATH setup to the VERY TOP of these files:

FILE 1: watchers/gmail_watcher.py
FILE 2: watchers/linkedin_watcher.py
FILE 3: watchers/file_system_watcher.py
FILE 4: watchers/base_watcher.py
FILE 5: orchestrator/approval_handler.py

Each file should have at the top:
```python
#!/usr/bin/env python3
"""[File description]"""

import sys
from pathlib import Path

# CRITICAL: Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import time
import os
from datetime import datetime

# Now these imports will work
from Personal_AI_Employee.watchers.base_watcher import BaseWatcher
from Personal_AI_Employee.utils.custom_logging import log_event, log_error
```

## RESPONSE_TEXT

Successfully applied the PYTHONPATH fixes to all required files. The changes ensure that when running individual watcher scripts directly, the Personal_AI_Employee module can be properly imported by adding the project root to Python's sys.path at runtime.

Files updated:
- Personal_AI_Employee/watchers/base_watcher.py
- Personal_AI_Employee/watchers/gmail_watcher.py
- Personal_AI_Employee/watchers/linkedin_watcher.py
- Personal_AI_Employee/watchers/file_system_watcher.py
- Personal_AI_Employee/orchestrator/approval_handler.py

Each file now has the required import structure at the top to ensure the project root is added to Python's path before attempting to import modules from the Personal_AI_Employee package.

## OUTCOME

The PYTHONPATH issue has been resolved by adding dynamic path resolution to the top of each file. This ensures that regardless of where the script is run from, it will be able to find and import the Personal_AI_Employee module and its submodules.

## EVALUATION

The fix was successfully applied to all five files as requested. The import structure follows the exact pattern specified in the requirements, using Path objects to dynamically determine the project root and insert it into sys.path. This should resolve the import errors when running individual watcher scripts directly.
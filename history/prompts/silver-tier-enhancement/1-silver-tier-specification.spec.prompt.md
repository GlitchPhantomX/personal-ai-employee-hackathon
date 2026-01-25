---
id: 1
title: Silver Tier Specification
stage: spec
date: 2026-01-23
surface: agent
model: claude-sonnet-4-5-20250929
feature: silver-tier-enhancement
branch: 001-silver-tier-enhancement
user: user
command: "/sp.specify"
labels: [specification,silver-tier,ai-employee]
links:
  spec: specs/001-silver-tier-enhancement/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-silver-tier-enhancement/spec.md
  - specs/001-silver-tier-enhancement/checklists/requirements.md
tests:
  - specs/001-silver-tier-enhancement/checklists/requirements.md
---

## Prompt

# SILVER TIER SPECIFICATION
## Functional Assistant Level - Personal AI Employee

**Status:** 🔄 Review & Enhancement Required

**Prerequisites:** ✅ Bronze Tier Complete

---

## CORE REQUIREMENTS (All Bronze + Following)

### 1. Multiple Watchers (2+ Required)
**Current Status:** ✅ Multiple watchers exist
```
watchers/
├── gmail_watcher.py           ✅ EXISTS
├── linkedin_watcher.py        ✅ EXISTS
├── file_system_watcher.py     ✅ EXISTS (NEW)
├── filesystem_watcher.py      ✅ EXISTS (OLD - may be duplicate)
├── social_media_watcher.py    ✅ EXISTS
├── twitter_watcher.py         ✅ EXISTS
├── xero_watcher.py            ✅ EXISTS
└── base_watcher.py            ✅ EXISTS
```

**Required:** Minimum 2 working watchers (Gmail + LinkedIn OR WhatsApp)
**Action:** ⚠️ Verify which watchers are functional, remove duplicates

---

### 2. Automated LinkedIn Posting
**Requirement:** AI Employee automatically posts on LinkedIn for business development

**Current Status:** ✅ Partial implementation
- `linkedin_watcher.py` exists ✅
- `linkedin_poster.py` skill exists ✅
- MCP server: `mcp_servers/linkedin_server/` ✅

**Missing Components:**
- [ ] LinkedIn posting schedule configuration
- [ ] Content generation for posts
- [ ] Post approval workflow
- [ ] Post performance tracking
- [ ] Integration with business goals

**Files to Check/Create:**
```
AI_Employee_Vault/
├── linkedin_schedule.json     ✅ EXISTS (verify format)
└── Skills/
    └── linkedin_poster.md     ✅ EXISTS (verify completeness)

mcp_servers/linkedin_server/
└── index.js                   ✅ EXISTS (verify functionality)

skills/
└── linkedin_poster.py         ✅ EXISTS (add auto-posting)
```

---

### 3. Claude Reasoning Loop (Plan.md Generation)
**Requirement:** Claude analyzes situations and creates structured Plan.md files

**Current Status:** 🔄 Needs Implementation
- Plans/ folder exists ✅
- Skills exist ✅
- No automated planning orchestrator ❌

**Required Components:**
- [ ] Planning orchestrator that triggers on events
- [ ] Plan.md template structure
- [ ] Reasoning chain documentation
- [ ] Plan execution tracking
- [ ] Plan review mechanism

**Files to Create:**
```
orchestrator/
└── planning_orchestrator.py   ❌ CREATE

AI_Employee_Vault/Plans/
├── TEMPLATE_PLAN.md           ❌ CREATE
└── README.md                  ❌ CREATE (planning guide)

models/
└── plan.py                    ❌ CREATE (plan data model)
```

---

### 4. Working MCP Server (Email Minimum)
**Requirement:** At least one MCP server for external actions

**Current Status:** ✅ Multiple MCP servers exist
```
mcp_servers/
├── browser_server/     ✅ EXISTS
├── email_server/       ✅ EXISTS
├── linkedin_server/    ✅ EXISTS
```

**Action Required:**
- [ ] Test email_server functionality
- [ ] Verify MCP server can send emails
- [ ] Create integration tests
- [ ] Document usage examples

---

### 5. Human-In-The-Loop Approval Workflow (Programmatic)
**Requirement:** Automated approval system with file-based workflow

**Current Status:** ✅ Partially implemented
- `orchestrator/approval_handler.py` exists ✅
- Pending_Approval/ folder exists ✅
- Approved/ folder exists ✅
- Rejection handling exists ✅

**Missing Components:**
- [ ] Automated monitoring of Pending_Approval folder
- [ ] Timeout handling for stale approvals
- [ ] Approval notification system
- [ ] Multi-tier approval levels
- [ ] Approval history tracking

**Files to Enhance:**
```
orchestrator/
└── approval_handler.py        ✅ EXISTS (add automation)

utils/
└── workflow_monitor.py        ✅ EXISTS (add approval watching)

models/
└── approval_request.py        ✅ EXISTS (verify completeness)
```

---

### 6. Scheduling System (Cron/Task Scheduler)
**Requirement:** Automated task scheduling for recurring operations

**Current Status:** ⚠️ Needs Implementation
- `orchestration/scheduler.py` exists ✅ (in old structure)
- PM2 ecosystem.config.js exists ✅
- No active scheduling ❌

**Required Components:**
- [ ] Cron-based scheduler for Linux/Mac
- [ ] Task Scheduler integration for Windows
- [ ] PM2 process management setup
- [ ] Scheduled task definitions
- [ ] Health check scheduling

**Files to Create/Enhance:**
```
orchestrator/
└── task_scheduler.py          ❌ CREATE

config/
└── schedule_config.py         ❌ CREATE

scripts/
├── setup_cron.sh              ❌ CREATE (Linux/Mac)
└── setup_task_scheduler.ps1   ❌ CREATE (Windows)
```

---

### 7. All Functionality as Agent Skills
**Requirement:** Every capability must be implemented as Agent Skills

**Current Status:** ✅ Skills exist
```
skills/
├── email_processor.py         ✅
├── invoice_generator.py       ✅
├── linkedin_poster.py         ✅
├── task_creator.py            ✅
└── whatsapp_handler.py        ✅

AI_Employee_Vault/Skills/
├── email_processor.md         ✅
├── invoice_generator.md       ✅
├── linkedin_poster.md         ✅
├── task_creator.md            ✅
└── whatsapp_handler.md        ✅
```

**Missing Skills (Silver Tier):**
- [ ] Planning skill (create_plan.md)
- [ ] Approval requester skill (request_approval.md)
- [ ] LinkedIn auto-poster skill (auto_post_linkedin.md)
- [ ] Email sender skill (send_email.md)

---

## ENHANCEMENT CHECKLIST

### Phase 1: Watcher Consolidation & Testing
- [ ] Identify duplicate watchers (file_system_watcher vs filesystem_watcher)
- [ ] Remove or merge duplicates
- [ ] Test each watcher independently
- [ ] Document watcher configuration
- [ ] Verify auto-restart functionality
- [ ] Create watcher health check script

### Phase 2: LinkedIn Automation Complete
- [ ] Review linkedin_schedule.json format
- [ ] Implement content generation for posts
- [ ] Create approval workflow for posts
- [ ] Test MCP server integration
- [ ] Add post success/failure logging
- [ ] Document LinkedIn automation setup

### Phase 3: Planning System Implementation
- [ ] Create planning_orchestrator.py
- [ ] Design Plan.md template structure
- [ ] Implement reasoning chain logic
- [ ] Add plan execution tracking
- [ ] Create plan review mechanism
- [ ] Test end-to-end planning workflow

### Phase 4: MCP Server Integration
- [ ] Test email_server functionality
- [ ] Create integration tests for MCP servers
- [ ] Document MCP server usage
- [ ] Add error handling for MCP failures
- [ ] Implement retry logic
- [ ] Create MCP server health checks

### Phase 5: Approval Workflow Automation
- [ ] Implement folder watching for Pending_Approval
- [ ] Add timeout handling (default: 24h)
- [ ] Create notification system for pending approvals
- [ ] Implement approval tier logic (Tier 0-3)
- [ ] Add approval history tracking
- [ ] Test complete approval workflow

### Phase 6: Scheduling System Setup
- [ ] Create task_scheduler.py with cron support
- [ ] Define scheduled tasks (CEO Briefing, health checks)
- [ ] Setup PM2 for process management
- [ ] Create platform-specific setup scripts
- [ ] Test scheduled task execution
- [ ] Document scheduling configuration

### Phase 7: New Agent Skills
- [ ] Create planning skill
- [ ] Create approval requester skill
- [ ] Create auto-poster skill for LinkedIn
- [ ] Create email sender skill
- [ ] Test all new skills
- [ ] Document skill usage

---

## PRIORITY FIXES

### 🔴 High Priority (Must Fix)
1. **Remove duplicate watchers** (file_system_watcher vs filesystem_watcher)
2. **Implement planning_orchestrator.py** (core Silver requirement)
3. **Setup scheduling system** (cron/PM2)
4. **Complete LinkedIn automation** (auto-posting)

### 🟡 Medium Priority
5. Enhance approval workflow automation
6. Test and document MCP servers
7. Add new Agent Skills for Silver tier
8. Create integration tests

### 🟢 Low Priority
9. Performance optimization
10. Advanced error recovery
11. Dashboard enhancements for Silver metrics

---

## SUCCESS CRITERIA (Silver Complete)

### Functional Requirements
- [ ] ✅ 2+ watchers operational and tested
- [ ] ✅ LinkedIn posts automatically on schedule
- [ ] ✅ Claude generates Plan.md files from events
- [ ] ✅ At least one MCP server working (email)
- [ ] ✅ HITL workflow programmatically enforced
- [ ] ✅ Tasks scheduled via cron/PM2
- [ ] ✅ All new functionality as Agent Skills

### Quality Requirements
- [ ] 30 consecutive days stable operation
- [ ] 100+ events handled successfully
- [ ] Zero critical failures
- [ ] Approval workflow <24h turnaround
- [ ] Plans generated show clear reasoning

### Documentation
- [ ] All new components documented
- [ ] Scheduling setup guide complete
- [ ] MCP server usage examples
- [ ] LinkedIn automation guide
- [ ] Updated architecture diagram

---

## NEW FILES REQUIRED FOR SILVER

### Orchestrator
```
orchestrator/
├── planning_orchestrator.py   ❌ CREATE
├── task_scheduler.py          ❌ CREATE
└── mcp_orchestrator.py        ❌ CREATE
```

### Models
```
models/
└── plan.py                    ❌ CREATE
```

### Config
```
config/
└── schedule_config.py         ❌ CREATE
```

### Skills (New)
```
skills/
├── planning_skill.py          ❌ CREATE
├── approval_requester.py      ❌ CREATE
└── email_sender.py            ❌ CREATE

AI_Employee_Vault/Skills/
├── create_plan.md             ❌ CREATE
├── request_approval.md        ❌ CREATE
└── send_email.md              ❌ CREATE
```

### Scripts
```
scripts/
├── setup_pm2.sh               ❌ CREATE
├── setup_cron.sh              ❌ CREATE
└── test_silver_tier.py        ❌ CREATE
```

### Templates
```
AI_Employee_Vault/Plans/
├── TEMPLATE_PLAN.md           ❌ CREATE
└── README.md                  ❌ CREATE
```

---

## ESTIMATED TIME

- **Watcher Cleanup:** 1-2 hours
- **Planning System:** 4-6 hours
- **LinkedIn Automation:** 3-4 hours
- **MCP Integration:** 2-3 hours
- **Approval Automation:** 3-4 hours
- **Scheduling Setup:** 2-3 hours
- **New Skills:** 3-4 hours
- **Testing & Documentation:** 4-5 hours
- **Total:** 22-31 hours

---

## INTEGRATION WITH BRONZE

**Silver builds on Bronze foundation:**
- Uses Bronze vault structure ✅
- Extends Bronze skills ✅
- Adds Bronze logging ✅
- Enhances Bronze approval workflow ✅

**No breaking changes to Bronze components!**

---

## QUICK WINS (Start Here)

1. **Remove duplicate watchers** → Clean up confusion
2. **Test existing MCP servers** → Verify email works
3. **Create planning_orchestrator.py** → Core Silver feature
4. **Setup PM2** → Enable 24/7 operation
5. **Test LinkedIn posting** → Verify automation works

---

## NEXT STEPS TO GOLD TIER

Once Silver is complete:
- ✅ Cross-domain integration (Personal + Business)
- ⚠️ Xero accounting integration
- ⚠️ Monday Morning CEO Briefing
- ⚠️ Advanced browser automation
- ⚠️ Multi-domain orchestration
- ⚠️ Dashboard UI

---

**Remember:** Silver is about AUTOMATION. Make it run 24/7 without manual intervention!

**Test Silver ONLY after Bronze is 100% passing!** ✅

## Response snapshot

Successfully created the Silver Tier Enhancement specification for the Personal AI Employee system. The specification includes:

1. **User Stories**: Seven prioritized user stories covering automated LinkedIn posting (P1), Claude reasoning loops with Plan.md generation (P1), multiple watchers monitoring (P1), MCP server integration (P2), programmatic approval workflow (P2), scheduling system (P2), and agent skills architecture (P3).

2. **Functional Requirements**: Ten specific requirements (FR-001 through FR-010) covering all core Silver Tier capabilities including watchers, LinkedIn automation, planning system, MCP servers, approval workflows, scheduling, and agent skills.

3. **Key Entities**: Defined five key entities (Watcher, Plan.md, Approval Request, Agent Skill, MCP Server) that represent the core concepts of the system.

4. **Success Criteria**: Eight measurable outcomes (SC-001 through SC-008) that define how the Silver Tier Enhancement will be evaluated for success, including uptime, event handling, LinkedIn posting success rate, reasoning clarity, approval workflow efficiency, skill implementation, scheduling reliability, and watcher coordination.

5. **Quality Assurance**: Created a comprehensive checklist confirming that the specification meets all quality requirements with no implementation details, clear user value focus, and properly defined testable requirements.

The specification is complete, follows the template structure, and is ready for the planning phase.

## Outcome

- ✅ Impact: Complete Silver Tier Enhancement specification created with clear requirements and success criteria
- 🧪 Tests: All requirements are testable with defined acceptance scenarios
- 📁 Files: spec.md and requirements checklist created and validated
- 🔁 Next prompts: Ready for planning phase (/sp.plan)
- 🧠 Reflection: Specification captures all Silver Tier requirements while maintaining user-centric focus

## Evaluation notes (flywheel)

- Failure modes observed: None - all requirements clearly defined
- Graders run and results (PASS/FAIL): All validation checks PASS
- Prompt variant (if applicable): Standard specification creation
- Next experiment (smallest change to try): Proceed to planning phase
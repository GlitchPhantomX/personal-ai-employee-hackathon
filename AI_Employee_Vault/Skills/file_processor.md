# SKILL: File Processor

## Purpose
Process and categorize files placed in the drop folder, extracting relevant information and triggering appropriate actions

## Context
You are a file processing assistant that analyzes incoming files to extract important information, categorize content, and initiate appropriate workflows. Your goal is to efficiently route information to the right place while capturing important details.

## Input Format
```yaml
file_path: "Full path to the file being processed"
file_type: "document|spreadsheet|image|video|audio|other"
file_name: "Original filename"
file_size: "Size in bytes"
creation_date: "File creation date"
tags: ["list", "of", "extracted", "tags"]
content_preview: "First few lines or summary of content"
```

## Capabilities

### 1. Content Analysis
- Extract key information from documents
- Identify important dates, people, or entities
- Recognize file types and their significance

### 2. Categorization
- Classify files by business function (finance, HR, operations, etc.)
- Determine priority level based on content
- Identify files requiring immediate attention

### 3. Action Triggering
- Create action items for urgent matters
- Schedule follow-ups for time-sensitive content
- Archive routine documents appropriately

### 4. Information Extraction
- Pull out important dates, names, and figures
- Identify contacts and relationships
- Capture financial or operational metrics

## Output Format

```markdown
---
type: file_processing_result
status: [processed|needs_attention|deferred]
priority: [low|medium|high|critical]
category: [finance|hr|operations|marketing|legal|other]
actions_taken: [list of actions performed]
---

## File Analysis

**Original File:** [file_name]
**Type:** [file_type]
**Size:** [file_size] bytes
**Date:** [creation_date]

## Extracted Information

### Key Entities
- People: [list of names identified]
- Organizations: [list of companies/organizations]
- Dates: [important dates found]
- Numbers: [financial figures, quantities, etc.]

### Content Summary
[Brief summary of file content]

## Recommended Actions

### Immediate
- [ ] [Action 1]
- [ ] [Action 2]

### Follow-up
- [ ] [Action 3]
- [ ] [Action 4]

## Categorization
- **Primary Category:** [category]
- **Secondary Tags:** [list of tags]
- **Priority Level:** [priority]

## Next Steps
- [Suggested workflow for this file type]
- [People who should be notified]
- [Systems that need updating]

## Approval Checklist
- [ ] Important information extracted
- [ ] Appropriate category assigned
- [ ] Correct priority level set
- [ ] Required actions identified
- [ ] Privacy/sensitivity considered
```

## Examples

### Example 1: Invoice Processing
**Input:**
```yaml
file_path: "drop_folder/invoice_ACME_12345.pdf"
file_type: "document"
file_name: "invoice_ACME_12345.pdf"
file_size: 245000
creation_date: "2026-01-14"
tags: ["invoice", "acme_corp", "january", "utilities"]
content_preview: "ACME Corporation - Invoice #12345 - Electric Utilities - $2,450.00 - Due: 2026-02-14"
```

**Output:**
```markdown
---
type: file_processing_result
status: needs_attention
priority: high
category: finance
actions_taken: ["extracted_amount", "identified_due_date", "flagged_for_approval"]
---

## File Analysis

**Original File:** invoice_ACME_12345.pdf
**Type:** document
**Size:** 245000 bytes
**Date:** 2026-01-14

## Extracted Information

### Key Entities
- People: N/A
- Organizations: ACME Corporation
- Dates: Due: 2026-02-14
- Numbers: $2,450.00

### Content Summary
Electric utilities invoice from ACME Corporation for January 2026. Amount: $2,450.00. Due in 30 days.

## Recommended Actions

### Immediate
- [ ] Route to accounts payable for approval
- [ ] Verify invoice against purchase order

### Follow-up
- [ ] Process payment before due date
- [ ] Update vendor payment calendar

## Categorization
- **Primary Category:** finance
- **Secondary Tags:** [invoice, utilities, acme_corp, january_2026]
- **Priority Level:** high

## Next Steps
- Move to Pending_Approval folder for review
- Notify finance team of new invoice
- Schedule payment for 2026-02-10 (4 days before due date)

## Approval Checklist
- [x] Important information extracted
- [x] Appropriate category assigned
- [x] Correct priority level set
- [x] Required actions identified
- [x] Privacy/sensitivity considered
```

### Example 2: Contract Document
**Input:**
```yaml
file_path: "drop_folder/NDA_ClientXYZ_2026.pdf"
file_type: "document"
file_name: "NDA_ClientXYZ_2026.pdf"
file_size: 387000
creation_date: "2026-01-14"
tags: ["nda", "contract", "client_xyz", "legal"]
content_preview: "Non-Disclosure Agreement - Client XYZ - Effective: 2026-01-15 - Duration: 2 years"
```

**Output:**
```markdown
---
type: file_processing_result
status: needs_attention
priority: critical
category: legal
actions_taken: ["identified_as_contract", "flagged_for_legal_review", "extracted_key_dates"]
---

## File Analysis

**Original File:** NDA_ClientXYZ_2026.pdf
**Type:** document
**Size:** 387000 bytes
**Date:** 2026-01-14

## Extracted Information

### Key Entities
- People: N/A
- Organizations: Client XYZ
- Dates: Effective: 2026-01-15, Duration: 2 years
- Numbers: N/A

### Content Summary
Non-Disclosure Agreement from Client XYZ. Becomes effective tomorrow (2026-01-15) and lasts for 2 years.

## Recommended Actions

### Immediate
- [ ] Send to legal team for review
- [ ] Identify stakeholders who need to be aware

### Follow-up
- [ ] Obtain signatures if acceptable
- [ ] Update contract management system

## Categorization
- **Primary Category:** legal
- **Secondary Tags:** [nda, contract, client_xyz, 2_years]
- **Priority Level:** critical

## Next Steps
- Forward to legal department immediately
- Alert business development team of pending NDA
- Prepare signature workflow if approved by legal
```

## Quality Checks
- [ ] Key information extracted accurately
- [ ] File properly categorized
- [ ] Appropriate priority assigned
- [ ] Relevant actions identified
- [ ] Sensitive information handled appropriately
- [ ] Compliance requirements considered
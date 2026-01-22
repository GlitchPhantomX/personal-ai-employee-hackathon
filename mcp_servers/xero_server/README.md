# Xero MCP Server

## Purpose
Integrates Personal AI Employee with Xero accounting software for automated financial management.

## Gold Tier Implementation

### Current Status: Simulated
For hackathon demonstration, this server simulates Xero operations. All responses are mocked data.

### Production Integration
For production use:
1. Sign up for Xero: https://www.xero.com/
2. Get API credentials
3. Use official Xero MCP: https://github.com/XeroAPI/xero-mcp-server
4. Replace simulated calls with actual Xero API calls

## Available Operations

### 1. Create Invoice
```json
{
  "client": "Client Name",
  "amount": 5000,
  "description": "Services rendered",
  "due_date": "2026-02-15"
}
```

### 2. Record Expense
```json
{
  "vendor": "AWS",
  "amount": 150.50,
  "category": "Cloud Services",
  "description": "Monthly hosting"
}
```

### 3. Get Financial Summary
```json
{
  "start_date": "2026-01-01",
  "end_date": "2026-01-31"
}
```

### 4. Get Account Balance
```json
{}
```

## Setup for Production

```bash
# Install dependencies
npm install

# Set Xero credentials in .env
XERO_CLIENT_ID=your_client_id
XERO_CLIENT_SECRET=your_client_secret
XERO_REDIRECT_URI=your_redirect_uri

# Start server
npm start
```

## Integration with Personal AI Employee

The Xero watcher monitors for:
- Weekly financial summaries (every Monday)
- New invoices requiring creation
- Expenses to record
- Account reconciliation needs

All data is synced to the Obsidian vault for human review and AI processing.
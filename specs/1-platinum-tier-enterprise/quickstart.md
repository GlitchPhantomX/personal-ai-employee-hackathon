# Platinum Tier Enterprise - Quick Start Guide

## Overview
This guide provides instructions for setting up and running the Platinum Tier Enterprise features of the AI Employee system. The system extends the existing Gold Tier with multi-tenancy, multi-user support, advanced AI capabilities, mobile access, and enterprise integrations.

## Prerequisites

### System Requirements
- Python 3.13+
- Node.js v24+
- PostgreSQL 13+
- Redis 6+
- Git
- Docker (optional, for containerized deployment)

### Environment Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd personal-ai-employee-hackathon-0
   git checkout 1-platinum-tier-enterprise
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env`:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Database Setup

### PostgreSQL Configuration
1. Create the database:
   ```sql
   CREATE DATABASE ai_employee_platinum;
   ```

2. Set up the schema:
   ```bash
   python -m src.database.setup
   ```

3. Enable Row-Level Security (RLS):
   ```sql
   -- This is handled automatically by the setup script
   -- But you can verify with:
   SELECT schemaname, tablename, rowsecurity FROM pg_tables WHERE schemaname = 'public';
   ```

## Running the Application

### Backend Services
1. Start the main API server:
   ```bash
   cd backend
   uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. Start MCP servers for integrations:
   ```bash
   # For each required MCP server:
   cd mcp_servers/[server_name]
   node server.mjs
   ```

### Frontend Applications
1. Dashboard (Web):
   ```bash
   cd frontend/dashboard
   npm install
   npm run dev
   ```

2. PWA (Mobile):
   ```bash
   cd frontend/pwa
   npm install
   npm run dev
   ```

### Background Services
1. Start Redis for session management:
   ```bash
   redis-server
   ```

2. Start background workers (for async tasks):
   ```bash
   python -m src.workers.main
   ```

## Initial Setup

### Create First Tenant
1. Register an admin user through the web interface
2. Or use the CLI:
   ```bash
   python -m src.cli.tenant create --name "My Company" --admin-email "admin@example.com"
   ```

### Configure Integrations
1. Navigate to Settings > Integrations in the dashboard
2. Add credentials for required enterprise systems:
   - CRM (Salesforce, HubSpot)
   - Calendar (Google, Outlook)
   - Payment (Stripe, PayPal)
   - Communication (Slack, Teams)

## Key Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Tenant Management
- `GET /api/tenants` - List tenants (admin only)
- `POST /api/tenants` - Create new tenant
- `GET /api/tenants/{id}` - Get tenant details

### User Management
- `GET /api/users` - List users in tenant
- `POST /api/users` - Create new user
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user

### Workflows
- `GET /api/workflows` - List workflows
- `POST /api/workflows` - Create workflow
- `PUT /api/workflows/{id}` - Update workflow
- `DELETE /api/workflows/{id}` - Delete workflow

## Mobile Access

### PWA Installation
1. Access the dashboard from a mobile browser
2. Look for "Add to Home Screen" option
3. The PWA will provide native-like experience

### Mobile Features
- View and approve tasks
- Receive push notifications
- Access key dashboard functionality
- Offline mode support

## Enterprise Integrations

### Available MCP Servers
- `salesforce_server` - Salesforce CRM integration
- `hubspot_server` - HubSpot CRM integration
- `slack_server` - Slack communication
- `calendar_server` - Google/Outlook Calendar
- `stripe_server` - Payment processing
- `twilio_server` - SMS/Phone notifications

### Adding New Integrations
1. Create new MCP server in `mcp_servers/` directory
2. Follow the MCP server template
3. Register the integration in the admin panel
4. Add configuration to tenant settings

## AI Learning Configuration

### Privacy Settings
1. By default, AI learning is enabled with data anonymization
2. Users can opt out in their preferences
3. Administrators can disable learning for entire tenants

### Training Data
- Conversations are stored for context and learning
- Personal data is anonymized before processing
- Users can request deletion of their data

## Security & Compliance

### Multi-Tenancy Isolation
- Row-level security prevents cross-tenant data access
- Each tenant has isolated configuration
- Resource quotas prevent one tenant from affecting others

### Compliance Features
- SOC 2 Type II controls implemented
- GDPR-compliant data handling
- Comprehensive audit logging
- Data retention policies

## Troubleshooting

### Common Issues
1. **Database connection errors**: Verify PostgreSQL is running and credentials in `.env` are correct
2. **MCP servers not connecting**: Check that all required MCP servers are running
3. **Authentication issues**: Ensure Redis is running for session management
4. **Mobile access problems**: Verify CORS settings in backend configuration

### Logs
- Backend: `logs/backend.log`
- MCP servers: `logs/mcp_servers.log`
- Frontend: Browser console
- Database: PostgreSQL logs

## Development

### Running Tests
```bash
# Backend tests
python -m pytest tests/backend/

# Frontend tests
cd frontend/dashboard && npm run test
cd frontend/pwa && npm run test

# Integration tests
python -m pytest tests/integration/
```

### Adding New Features
1. Update the data model in `data-model.md`
2. Create new API endpoints following existing patterns
3. Add tests for new functionality
4. Update documentation as needed

## Production Deployment

### Containerized Deployment
```bash
# Build Docker images
docker-compose build

# Run in production
docker-compose up -d
```

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `JWT_SECRET`: Secret for JWT signing
- `CLAUDE_API_KEY`: API key for Claude integration
- `ENCRYPTION_KEY`: Key for data encryption

## Next Steps

1. Customize the system for your specific business needs
2. Add domain-specific skills to the system
3. Configure enterprise integrations for your workflow
4. Train the AI system with your specific data and preferences
5. Set up monitoring and alerting for production use

For more detailed information, refer to the full documentation in the `docs/` directory.
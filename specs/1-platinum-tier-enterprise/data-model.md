# Data Model: Platinum Tier Enterprise

## Overview
This document defines the data model for the Platinum Tier Enterprise features, extending the existing AI Employee system with multi-tenant, multi-user, and enterprise capabilities.

## Core Entities

### Tenant
Represents a business/client organization with isolated data, configurations, and billing.

**Fields:**
- `id` (UUID, Primary Key)
- `name` (VARCHAR(255), Required)
- `slug` (VARCHAR(100), Unique, Required, Regex: ^[a-z0-9-]+$)
- `config` (JSONB, Optional)
- `billing_info` (JSONB, Optional)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)
- `status` (ENUM: active, suspended, cancelled, Required, Default: active)

**Validation:**
- Name must be 2-255 characters
- Slug must be unique and follow kebab-case convention
- Status must be one of allowed values

**Relationships:**
- One-to-Many: Users
- One-to-Many: Workflows
- One-to-Many: Skills (installed)

### User
Individual account within a tenant with specific role-based permissions and access rights.

**Fields:**
- `id` (UUID, Primary Key)
- `tenant_id` (UUID, Foreign Key to Tenant.id, Required)
- `email` (VARCHAR(255), Unique, Required)
- `password_hash` (VARCHAR(255), Required)
- `name` (VARCHAR(255), Required)
- `role` (VARCHAR(50), Required, Default: "user")
- `status` (ENUM: active, inactive, invited, Required, Default: active)
- `last_login` (TIMESTAMP, Optional)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)

**Validation:**
- Email must be valid email format
- Role must be one of: admin, manager, user, viewer
- Email must be unique within tenant

**Relationships:**
- Many-to-One: Tenant
- Many-to-Many: Roles (through user_roles junction table)

### Role
Permission level defining what actions and data a user can access within the system.

**Fields:**
- `id` (UUID, Primary Key)
- `name` (VARCHAR(100), Required)
- `description` (TEXT, Optional)
- `permissions` (JSONB, Required)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)

**Validation:**
- Name must be unique across system
- Permissions must be valid JSON structure

**Relationships:**
- Many-to-Many: Users (through user_roles junction table)

### UserRole (Junction Table)
Associates users with roles within a tenant context.

**Fields:**
- `user_id` (UUID, Foreign Key to User.id, Required)
- `role_id` (UUID, Foreign Key to Role.id, Required)
- `assigned_at` (TIMESTAMP, Required)
- `assigned_by` (UUID, Foreign Key to User.id, Optional)

**Primary Key:** (user_id, role_id)

**Relationships:**
- Many-to-One: User
- Many-to-One: Role

### Workflow
Configurable business process with conditional logic, parallel execution, and integration points.

**Fields:**
- `id` (UUID, Primary Key)
- `tenant_id` (UUID, Foreign Key to Tenant.id, Required)
- `name` (VARCHAR(255), Required)
- `definition` (JSONB, Required)
- `created_by` (UUID, Foreign Key to User.id, Required)
- `status` (ENUM: draft, active, paused, archived, Required, Default: draft)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)

**Validation:**
- Definition must be valid workflow structure
- Status must be one of allowed values

**Relationships:**
- Many-to-One: Tenant
- Many-to-One: User (creator)

### Skill
Reusable functional component that can be installed and configured for specific capabilities.

**Fields:**
- `id` (UUID, Primary Key)
- `name` (VARCHAR(255), Required)
- `description` (TEXT, Optional)
- `category` (VARCHAR(100), Required)
- `definition` (JSONB, Required)
- `author` (VARCHAR(255), Optional)
- `version` (VARCHAR(20), Required, Default: "1.0.0")
- `price` (DECIMAL(10,2), Optional, Default: 0.00)
- `rating` (DECIMAL(3,2), Optional, Min: 0, Max: 5)
- `downloads` (INTEGER, Optional, Default: 0)
- `is_public` (BOOLEAN, Required, Default: false)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)

**Validation:**
- Price must be >= 0
- Rating must be between 0 and 5
- Version must follow semantic versioning

**Relationships:**
- One-to-Many: InstalledSkills (per tenant)

### InstalledSkill
Tracks which skills are installed in which tenants.

**Fields:**
- `id` (UUID, Primary Key)
- `tenant_id` (UUID, Foreign Key to Tenant.id, Required)
- `skill_id` (UUID, Foreign Key to Skill.id, Required)
- `config` (JSONB, Optional)
- `installed_by` (UUID, Foreign Key to User.id, Required)
- `installed_at` (TIMESTAMP, Required)
- `status` (ENUM: active, disabled, Required, Default: active)

**Validation:**
- Status must be one of allowed values

**Relationships:**
- Many-to-One: Tenant
- Many-to-One: Skill
- Many-to-One: User (installer)

### Notification
Multi-channel alert system supporting email, SMS, push, and chat platform delivery.

**Fields:**
- `id` (UUID, Primary Key)
- `tenant_id` (UUID, Foreign Key to Tenant.id, Required)
- `recipient_user_id` (UUID, Foreign Key to User.id, Required)
- `type` (VARCHAR(50), Required)
- `title` (VARCHAR(255), Required)
- `message` (TEXT, Required)
- `channel` (VARCHAR(50), Required, Enum: email, sms, push, slack, discord)
- `priority` (ENUM: low, medium, high, urgent, Required, Default: medium)
- `sent_at` (TIMESTAMP, Optional)
- `delivered_at` (TIMESTAMP, Optional)
- `read_at` (TIMESTAMP, Optional)
- `created_at` (TIMESTAMP, Required)

**Validation:**
- Channel must be one of allowed values
- Priority must be one of allowed values

**Relationships:**
- Many-to-One: Tenant
- Many-to-One: User (recipient)

### Conversation
Stores conversation history for AI learning and context preservation.

**Fields:**
- `id` (UUID, Primary Key)
- `tenant_id` (UUID, Foreign Key to Tenant.id, Required)
- `user_id` (UUID, Foreign Key to User.id, Required)
- `session_id` (VARCHAR(255), Required)
- `input_text` (TEXT, Required)
- `output_text` (TEXT, Required)
- `context_data` (JSONB, Optional)
- `created_at` (TIMESTAMP, Required)

**Relationships:**
- Many-to-One: Tenant
- Many-to-One: User

### UserPreference
Stores user-specific preferences for AI interaction and system behavior.

**Fields:**
- `id` (UUID, Primary Key)
- `user_id` (UUID, Foreign Key to User.id, Required)
- `preference_key` (VARCHAR(100), Required)
- `preference_value` (TEXT, Required)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)

**Validation:**
- preference_key must be unique per user

**Relationships:**
- Many-to-One: User

### AuditEvent
Comprehensive audit logging for security and compliance requirements.

**Fields:**
- `id` (UUID, Primary Key)
- `tenant_id` (UUID, Foreign Key to Tenant.id, Required)
- `user_id` (UUID, Foreign Key to User.id, Optional)
- `action` (VARCHAR(100), Required)
- `resource_type` (VARCHAR(100), Required)
- `resource_id` (VARCHAR(255), Optional)
- `details` (JSONB, Optional)
- `ip_address` (INET, Optional)
- `user_agent` (TEXT, Optional)
- `timestamp` (TIMESTAMP, Required)

**Relationships:**
- Many-to-One: Tenant
- Many-to-One: User (optional)

## Additional Tables

### Session
Manages user sessions for authentication.

**Fields:**
- `id` (VARCHAR(255), Primary Key)
- `user_id` (UUID, Foreign Key to User.id, Required)
- `expires_at` (TIMESTAMP, Required)
- `created_at` (TIMESTAMP, Required)

### TenantConfig
Stores tenant-specific configuration settings.

**Fields:**
- `tenant_id` (UUID, Foreign Key to Tenant.id, Primary Key)
- `config_key` (VARCHAR(100), Required)
- `config_value` (TEXT, Required)
- `updated_at` (TIMESTAMP, Required)

### MarketplaceSkill
Skills available in the marketplace.

**Fields:**
- `id` (UUID, Primary Key)
- `name` (VARCHAR(255), Required)
- `description` (TEXT, Required)
- `category` (VARCHAR(100), Required)
- `price` (DECIMAL(10,2), Required, Default: 0.00)
- `rating` (DECIMAL(3,2), Optional)
- `downloads` (INTEGER, Default: 0)
- `developer_id` (UUID, Optional)
- `status` (ENUM: active, pending, rejected, archived, Required, Default: pending)
- `created_at` (TIMESTAMP, Required)
- `updated_at` (TIMESTAMP, Required)

## Security Considerations

### Row-Level Security (RLS)
- All tables (except global ones like Roles) must include tenant_id
- RLS policies enforce tenant isolation
- Users can only access data from their tenant

### Data Encryption
- Password hashes stored using bcrypt or similar
- Sensitive fields encrypted at rest when required
- Connection encryption enforced

### Audit Trail
- All data modifications logged in audit_events
- Read operations for sensitive data also logged
- Compliance with SOC 2 and GDPR requirements
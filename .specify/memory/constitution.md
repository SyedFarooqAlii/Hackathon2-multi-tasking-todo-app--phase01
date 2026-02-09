<!-- SYNC IMPACT REPORT:
     Version change: 1.0.0 → 1.1.0
     Modified principles: None (new principles added)
     Added sections: Core Principles 1-6, Additional Constraints, Development Workflow, Governance rules
     Removed sections: None
     Templates requiring updates: N/A
     Follow-up TODOs: None
-->
# Phase II – Todo Full-Stack Web Application (Multi-User, Authenticated) Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All implementation must follow written specs. Features must be derived directly from approved specifications, with every implementation detail traceable back to spec requirements. No feature creep or deviation from approved specs without formal amendment process.
<!-- Spec-driven development (all implementation must follow written specs) -->

### II. Security-First Authentication and Authorization
Security-first approach to authentication and authorization. Every API endpoint must enforce JWT-based authentication, with user data isolation and ownership enforcement. Cross-user data access is strictly forbidden.
<!-- Security-first authentication and authorization -->

### III. Clear Separation of Concerns
Maintain clear separation between Frontend, Backend, Database, and Authentication layers. Each layer must have well-defined interfaces and responsibilities, with minimal coupling between components.
<!-- Clear separation of concerns (Frontend, Backend, Database, Auth) -->

### IV. Deterministic, Reviewable Agent Workflow
No manual coding outside Claude Code framework. All development must follow deterministic, reviewable agent workflow using Claude Code + Spec-Kit Plus only, ensuring reproducible and auditable development process.
<!-- Deterministic, reviewable agent workflow (no manual coding) -->

### V. User Data Isolation and Ownership Enforcement
Every API call must validate task ownership on read/write operations. User_id must be derived from token, not trusted from client input, ensuring strict data isolation between users.
<!-- User data isolation and ownership enforcement -->

### VI. Clean Architecture and Best Practices
Code must follow clean architecture principles and modern best practices. All errors must be explicit, user-safe, and spec-defined, with proper error handling throughout the application.
<!-- Code must follow clean architecture and modern best practices -->

## Additional Constraints
- All features must be derived directly from approved specs
- Every API endpoint must enforce JWT-based authentication
- Task ownership must be validated on every read/write operation
- Frontend, backend, and auth flows must remain consistent
- Errors must be explicit, user-safe, and spec-defined
- Code must follow clean architecture and modern best practices

## Architecture Standards
- Frontend: Next.js 16+ App Router
- Backend: FastAPI (Python)
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT tokens
- Shared JWT secret via environment variables
- Stateless backend authentication (no session coupling)

## Security Rules
- All API requests require a valid JWT token
- JWT must be verified on every request
- user_id must be derived from token, not trusted from client input
- Cross-user data access is strictly forbidden
- Unauthorized requests must return 401
- Invalid or expired tokens must be rejected

## API Standards
- RESTful endpoints only
- Endpoints remain stable but behavior is auth-enforced
- All queries filtered by authenticated user
- Task ownership enforced on create, read, update, delete, complete

## Development Workflow Constraints
Follow Agentic Dev Stack strictly: Spec → Plan → Tasks → Implementation. No manual coding outside Claude Code. All decisions must be documented in specs. Iterations must preserve backward correctness.

## Deliverable Standards
- Fully functional authenticated web app
- Persistent storage via Neon PostgreSQL
- Responsive frontend UI
- Secure multi-user task management

## Governance
All implementation must follow the Agentic Dev Stack workflow (Spec → Plan → Tasks → Implementation) using Claude Code + Spec-Kit Plus only. Constitution supersedes all other practices. Amendments require formal documentation, approval, and migration planning. All API endpoints must enforce JWT-based authentication with user data isolation. All development must be deterministic and reviewable.

**Version**: 1.1.0 | **Ratified**: 2026-01-16 | **Last Amended**: 2026-01-16

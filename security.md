# Security Design

## Authentication
- Users log in using username/email and password
- Flask sessions are used to maintain login state

## Password Security
- Passwords are hashed before storing in the database
- Plain text passwords are never stored

## Data Protection
- Each user can only access their own classes and assignments

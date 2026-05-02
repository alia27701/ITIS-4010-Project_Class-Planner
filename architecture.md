# Architecture Summary

## For this system, it follows a 3-tier architecture:
- Frontend
  - HTML (structure)
  - CSS (styling)
  - JavaScript (logic, API calls)
- Backend
  - Python + Flask
- Database
  - MySQL (originally meant for storing the information of the users credentials. Current version uses in-memory storage)

## Data Flow
1. User interacts with frontend
2. Frontend sends API request to Flask backend
3. Backend processes logic and queries MySQL
4. Response is returned to frontend

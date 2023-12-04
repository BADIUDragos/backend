from datetime import timedelta

ACCESS_TOKEN_LIFETIME = timedelta(minutes=10)
REFRESH_TOKEN_LIFETIME = timedelta(days=1)
SIGNING_KEY = "S-XaAKGH70dyODsFJH18HphHG2zsa1gha4RG6OLbo2E"

DB_NAME = 'backend'
DB_USER = 'postgres'
DB_PASSWORD = 'Maudeg12.34'
DB_HOST = 'localhost'
DB_PORT = '5432'

TIME_ZONE = 'UTC'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

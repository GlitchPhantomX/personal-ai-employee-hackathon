import asyncio
import os
from pathlib import Path
from mcp_servers.calendar_server.google_calendar_client import GoogleCalendarClient

async def authenticate():
    credentials_path = os.getenv('GOOGLE_CALENDAR_CREDENTIALS_PATH', 'credentials.json')
    token_path = os.getenv('GOOGLE_CALENDAR_TOKEN_PATH', 'token.json')
    
    client = GoogleCalendarClient(
        credentials_path=credentials_path,
        token_path=token_path
    )
    
    success = await client.authenticate()
    
    if success:
        print("✅ Successfully authenticated with Google Calendar!")
    else:
        print("❌ Authentication failed")

if __name__ == "__main__":
    asyncio.run(authenticate())
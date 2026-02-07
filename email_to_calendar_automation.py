"""
Email to Calendar Event Automation Script
Reads emails from Needs_Action folder and creates calendar events
"""
import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path


class CalendarAutomation:
    def __init__(self, server_url="http://localhost:8085"):
        self.server_url = server_url
        self.vault_path = Path("Personal_AI_Employee/AI_Employee_Vault")
        self.needs_action_path = self.vault_path / "Needs_Action"
        self.approved_path = self.vault_path / "Approved"
        
    def read_email_file(self, filepath):
        """Read and parse email markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return None
    
    def extract_meeting_info(self, email_content):
        """Extract meeting information from email content"""
        # Simple keyword detection
        keywords = ['meeting', 'call', 'interview', 'discussion', 'standup']
        
        if not any(keyword in email_content.lower() for keyword in keywords):
            return None
        
        # Extract subject (usually in first line or after "Subject:")
        lines = email_content.split('\n')
        subject = lines[0].strip('#').strip() if lines else "Untitled Meeting"
        
        # For demo, create event for tomorrow
        tomorrow = datetime.now() + timedelta(days=1)
        start_time = tomorrow.replace(hour=14, minute=0, second=0, microsecond=0)
        end_time = start_time + timedelta(hours=1)
        
        return {
            "summary": subject[:50],  # Limit to 50 chars
            "start_time": start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "end_time": end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "description": f"Auto-created from email\n\n{email_content[:200]}...",
            "calendar_id": "work"
        }
    
    def create_calendar_event(self, event_data):
        """Create event in Google Calendar via MCP server"""
        try:
            response = requests.post(
                f"{self.server_url}/calendar/google/create_event",
                json=event_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('result', {})
            else:
                print(f"Error: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error creating event: {e}")
            return None
    
    def save_result(self, filename, data):
        """Save result to Approved folder"""
        try:
            output_path = self.approved_path / filename
            self.approved_path.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            
            print(f"✅ Saved: {output_path}")
            return True
        except Exception as e:
            print(f"Error saving result: {e}")
            return False
    
    def process_emails(self, limit=5):
        """Process emails from Needs_Action folder"""
        print("🔍 Scanning Needs_Action folder...")
        
        if not self.needs_action_path.exists():
            print(f"❌ Folder not found: {self.needs_action_path}")
            return
        
        # Get all email files
        email_files = list(self.needs_action_path.glob("EMAIL_*.md"))
        
        if not email_files:
            print("📭 No email files found")
            return
        
        print(f"📧 Found {len(email_files)} email(s)")
        print(f"📝 Processing first {limit} emails...\n")
        
        processed = 0
        created = 0
        
        for email_file in email_files[:limit]:
            print(f"\n📄 Processing: {email_file.name}")
            
            # Read email
            content = self.read_email_file(email_file)
            if not content:
                continue
            
            # Extract meeting info
            meeting_info = self.extract_meeting_info(content)
            if not meeting_info:
                print("   ⏭️  No meeting keywords found, skipping")
                processed += 1
                continue
            
            print(f"   📅 Creating event: {meeting_info['summary']}")
            
            # Create calendar event
            result = self.create_calendar_event(meeting_info)
            
            if result and result.get('success'):
                print(f"   ✅ Event created successfully!")
                
                # Save result
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_filename = f"CALENDAR_EVENT_{timestamp}_{email_file.stem}.json"
                
                self.save_result(output_filename, {
                    'source_email': email_file.name,
                    'event_data': meeting_info,
                    'calendar_response': result,
                    'created_at': timestamp
                })
                
                created += 1
            else:
                print(f"   ❌ Failed to create event")
                print(f"   Error: {result}")
            
            processed += 1
        
        print(f"\n\n{'='*50}")
        print(f"📊 Summary:")
        print(f"   Processed: {processed} emails")
        print(f"   Created: {created} calendar events")
        print(f"   Results saved in: {self.approved_path}")
        print(f"{'='*50}")
    
    def test_connection(self):
        """Test connection to MCP server"""
        try:
            response = requests.get(f"{self.server_url}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Server connection OK")
                print(f"   Status: {data.get('status')}")
                print(f"   Server: {data.get('server')}")
                return True
            else:
                print(f"❌ Server returned: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Cannot connect to server: {e}")
            print(f"   Make sure server is running on {self.server_url}")
            return False


def main():
    """Main function"""
    print("="*50)
    print("📧 Email to Calendar Automation")
    print("="*50)
    print()
    
    automation = CalendarAutomation()
    
    # Test server connection
    if not automation.test_connection():
        print("\n⚠️  Please start the MCP server first:")
        print("   cd Personal_AI_Employee")
        print("   python -m mcp_servers.calendar_server.main")
        return
    
    print()
    
    # Process emails
    automation.process_emails(limit=5)


if __name__ == "__main__":
    main()
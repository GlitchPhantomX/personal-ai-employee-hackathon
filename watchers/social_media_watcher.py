#!/usr/bin/env python3
"""
Social Media Watcher (Facebook & Instagram)
Monitors posting schedule and generates content requests
"""

from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timedelta
import json
import sys

sys.path.insert(0, str(Path(__file__).parent))
from base_watcher import BaseWatcher

class SocialMediaWatcher(BaseWatcher):
    """
    Monitors social media posting schedule for Facebook and Instagram
    Generates content creation requests based on schedule
    """

    def __init__(self, vault_path: str, check_interval: int = 14400):  # 4 hours
        """
        Initialize social media watcher

        Args:
            vault_path: Path to Obsidian vault
            check_interval: Seconds between checks (14400 = 4 hours)
        """
        super().__init__(vault_path, check_interval)

        self.schedule_file = self.vault_path / 'social_media_schedule.json'
        self.last_post_file = self.vault_path / 'Logs' / 'social_last_post.json'

        # Initialize schedule
        if not self.schedule_file.exists():
            self._create_default_schedule()

        # Initialize last post tracking
        if not self.last_post_file.exists():
            self._save_last_posts({
                'facebook': None,
                'instagram': None,
                'last_check': datetime.now().isoformat()
            })

        self.logger.info('Social Media Watcher initialized')

    def _create_default_schedule(self):
        """Create default posting schedule"""
        default_schedule = {
            "posting_frequency": {
                "facebook": "3x_per_week",
                "instagram": "4x_per_week"
            },
            "preferred_days": {
                "facebook": ["Monday", "Wednesday", "Friday"],
                "instagram": ["Monday", "Tuesday", "Thursday", "Saturday"]
            },
            "preferred_times": {
                "facebook": "10:00",
                "instagram": "14:00"
            },
            "content_mix": {
                "business_updates": 30,
                "industry_insights": 25,
                "testimonials": 20,
                "behind_scenes": 15,
                "products": 10
            },
            "hashtag_strategy": {
                "branded": ["#YourCompany", "#YourBrand"],
                "industry": ["#Industry", "#BusinessTips"],
                "trending": "use_current_trends"
            }
        }

        self.schedule_file.write_text(json.dumps(default_schedule, indent=2))
        self.logger.info(f'Created default social media schedule')

    def _save_last_posts(self, data: dict):
        """Save last post information"""
        self.last_post_file.write_text(json.dumps(data, indent=2))

    def _load_last_posts(self) -> dict:
        """Load last post information"""
        if self.last_post_file.exists():
            return json.loads(self.last_post_file.read_text())
        return {}

    def check_for_updates(self) -> List[Dict[str, Any]]:
        """
        Check if new social media posts are needed

        Returns:
            List of post requests
        """
        posts_needed = []

        try:
            schedule = json.loads(self.schedule_file.read_text())
            last_posts = self._load_last_posts()
            now = datetime.now()

            # Check Facebook
            fb_last = last_posts.get('facebook')
            if not fb_last or self._should_post('facebook', fb_last, schedule):
                content_type = self._select_content_type(schedule['content_mix'])
                posts_needed.append({
                    'platform': 'facebook',
                    'content_type': content_type,
                    'scheduled_time': schedule['preferred_times']['facebook'],
                    'last_post': fb_last
                })
                last_posts['facebook'] = now.isoformat()

            # Check Instagram
            ig_last = last_posts.get('instagram')
            if not ig_last or self._should_post('instagram', ig_last, schedule):
                content_type = self._select_content_type(schedule['content_mix'])
                posts_needed.append({
                    'platform': 'instagram',
                    'content_type': content_type,
                    'scheduled_time': schedule['preferred_times']['instagram'],
                    'last_post': ig_last
                })
                last_posts['instagram'] = now.isoformat()

            if posts_needed:
                last_posts['last_check'] = now.isoformat()
                self._save_last_posts(last_posts)

            self.logger.info(f'Social media check: {len(posts_needed)} post(s) needed')

        except Exception as e:
            self.logger.error(f'Error checking social media schedule: {e}')

        return posts_needed

    def _should_post(self, platform: str, last_post: str, schedule: dict) -> bool:
        """Determine if platform needs new post"""
        if not last_post:
            return True

        last = datetime.fromisoformat(last_post)
        days_since = (datetime.now() - last).days

        frequency = schedule['posting_frequency'][platform]

        if '3x' in frequency and days_since >= 2:
            return True
        elif '4x' in frequency and days_since >= 1:
            return True
        elif 'daily' in frequency and days_since >= 1:
            return True

        return False

    def _select_content_type(self, content_mix: dict) -> str:
        """Select content type based on strategy mix"""
        import random
        content_types = list(content_mix.keys())
        weights = list(content_mix.values())

        return random.choices(content_types, weights=weights)[0]

    def create_action_file(self, item: Dict[str, Any]) -> Path:
        """
        Create social media post request

        Args:
            item: Post information

        Returns:
            Path to created action file
        """
        unique_id = self._generate_unique_id()
        platform = item['platform'].upper()
        content_type = item['content_type'].replace('_', '-')

        action_filename = f'{platform}_{unique_id}_{content_type}.md'
        action_path = self.needs_action / action_filename

        content = f"""---
type: social_media_post
platform: {item['platform']}
content_type: {item['content_type']}
status: pending
priority: medium
created: {datetime.now().isoformat()}
scheduled_time: {item['scheduled_time']}
---

# {item['platform'].title()} Post Request

## Task
Generate {item['platform'].title()} post for {item['content_type'].replace('_', ' ')}

## Requirements
- Platform: {item['platform'].title()}
- Content Type: {item['content_type'].replace('_', ' ').title()}
- Scheduled Time: {item['scheduled_time']}
- Include image/video suggestion
- Follow brand guidelines
- Include 5-10 relevant hashtags

## Instructions for AI
1. Use skill: [[Skills/facebook_instagram_manager]]
2. Generate engaging content optimized for {item['platform'].title()}
3. Include media suggestion
4. Add relevant hashtags
5. Create approval request in [[Pending_Approval]]
6. After approval, schedule for posting

## Last Post
Previous {item['platform'].title()} post: {item['last_post'] or 'First post'}

## Content Strategy Reference
See [[social_media_schedule.json]] for content mix and guidelines

---
*Auto-generated by SocialMediaWatcher*
*Use facebook_instagram_manager skill for content generation*
"""

        action_path.write_text(content, encoding='utf-8')
        self.logger.info(f'Created {item["platform"]} post request: {action_filename}')

        return action_path

# Standalone execution
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print('Usage: python social_media_watcher.py <vault_path> [check_interval]')
        print('Example: python social_media_watcher.py ../AI_Employee_Vault 14400')
        sys.exit(1)

    vault_path = sys.argv[1]
    check_interval = int(sys.argv[2]) if len(sys.argv) > 2 else 14400

    watcher = SocialMediaWatcher(vault_path, check_interval)

    print(f'\n{"="*60}')
    print(f'[*] Social Media Watcher Started (Facebook & Instagram)')
    print(f'{"="*60}')
    print(f'Vault: {vault_path}')
    print(f'Check Interval: {check_interval}s ({check_interval//3600}h)')
    print(f'{"="*60}\n')
    print('Monitoring social media posting schedule...')
    print('Facebook: 3x per week')
    print('Instagram: 4x per week')
    print('Press Ctrl+C to stop\n')

    try:
        watcher.run()
    except KeyboardInterrupt:
        print('\n\n[*] Watcher stopped by user')
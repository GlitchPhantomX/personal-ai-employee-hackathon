#!/usr/bin/env python3
"""
Twitter (X) Watcher
Monitors posting schedule and engagement opportunities
"""

from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timedelta
import json
import sys

sys.path.insert(0, str(Path(__file__).parent))
from base_watcher import BaseWatcher

class TwitterWatcher(BaseWatcher):
    """
    Monitors Twitter posting schedule
    Generates tweet requests based on strategy
    """

    def __init__(self, vault_path: str, check_interval: int = 10800):  # 3 hours
        """
        Initialize Twitter watcher

        Args:
            vault_path: Path to Obsidian vault
            check_interval: Seconds between checks (10800 = 3 hours)
        """
        super().__init__(vault_path, check_interval)

        self.schedule_file = self.vault_path / 'twitter_schedule.json'
        self.last_tweet_file = self.vault_path / 'Logs' / 'twitter_last_tweet.json'

        if not self.schedule_file.exists():
            self._create_default_schedule()

        if not self.last_tweet_file.exists():
            self._save_last_tweet({
                'last_tweet': None,
                'tweets_today': 0,
                'date': datetime.now().strftime('%Y-%m-%d')
            })

        self.logger.info('Twitter Watcher initialized')

    def _create_default_schedule(self):
        """Create default Twitter strategy"""
        strategy = {
            "daily_tweet_target": 3,
            "content_mix": {
                "industry_insights": 40,
                "tips_tricks": 25,
                "engagement": 20,
                "company_updates": 10,
                "retweets": 5
            },
            "optimal_times": ["09:00", "13:00", "17:00"],
            "hashtag_limit": 2,
            "thread_frequency": "2x_per_week"
        }

        self.schedule_file.write_text(json.dumps(strategy, indent=2))

    def _save_last_tweet(self, data: dict):
        """Save last tweet info"""
        self.last_tweet_file.write_text(json.dumps(data, indent=2))

    def _load_last_tweet(self) -> dict:
        """Load last tweet info"""
        if self.last_tweet_file.exists():
            return json.loads(self.last_tweet_file.read_text())
        return {}

    def check_for_updates(self) -> List[Dict[str, Any]]:
        """
        Check if new tweets are needed

        Returns:
            List of tweet requests
        """
        tweets_needed = []

        try:
            strategy = json.loads(self.schedule_file.read_text())
            last_info = self._load_last_tweet()
            now = datetime.now()
            today = now.strftime('%Y-%m-%d')

            # Reset count if new day
            if last_info.get('date') != today:
                last_info = {
                    'last_tweet': None,
                    'tweets_today': 0,
                    'date': today
                }

            # Check if we need more tweets today
            target = strategy['daily_tweet_target']
            current = last_info.get('tweets_today', 0)

            if current < target:
                # Determine content type
                content_type = self._select_content_type(strategy['content_mix'])

                tweets_needed.append({
                    'content_type': content_type,
                    'tweet_number': current + 1,
                    'target_time': strategy['optimal_times'][current % len(strategy['optimal_times'])],
                    'last_tweet': last_info.get('last_tweet')
                })

                # Update count
                last_info['tweets_today'] = current + 1
                last_info['last_tweet'] = now.isoformat()
                last_info['date'] = today
                self._save_last_tweet(last_info)

        except Exception as e:
            self.logger.error(f'Error checking Twitter schedule: {e}')

        return tweets_needed

    def _select_content_type(self, content_mix: dict) -> str:
        """Select content type based on strategy"""
        import random
        types = list(content_mix.keys())
        weights = list(content_mix.values())
        return random.choices(types, weights=weights)[0]

    def create_action_file(self, item: Dict[str, Any]) -> Path:
        """
        Create tweet request

        Args:
            item: Tweet information

        Returns:
            Path to created action file
        """
        unique_id = self._generate_unique_id()
        content_type = item['content_type'].replace('_', '-')

        action_filename = f'TWITTER_{unique_id}_{content_type}.md'
        action_path = self.needs_action / action_filename

        content = f"""---
type: twitter_post
content_type: {item['content_type']}
tweet_number: {item['tweet_number']}/3
status: pending
priority: medium
created: {datetime.now().isoformat()}
target_time: {item['target_time']}
---

# Twitter Post Request

## Task
Generate Twitter/X post for {item['content_type'].replace('_', ' ')}

## Requirements
- Max 280 characters
- Content Type: {item['content_type'].replace('_', ' ').title()}
- Target Time: {item['target_time']}
- Include 1-2 relevant hashtags (max)
- Engaging and professional tone

## Instructions for AI
1. Use skill: [[Skills/twitter_manager]]
2. Generate concise, engaging tweet
3. Keep under 280 characters
4. Add maximum 2 hashtags
5. Create approval request in [[Pending_Approval]]
6. After approval, schedule for posting

## Tweet #{item['tweet_number']} of 3 today

## Last Tweet
Previous tweet: {item['last_tweet'] or 'First tweet of the day'}

## Strategy Reference
See [[twitter_schedule.json]] for content mix

---
*Auto-generated by TwitterWatcher*
*Use twitter_manager skill for content generation*
"""

        action_path.write_text(content, encoding='utf-8')
        self.logger.info(f'Created Twitter post request: {action_filename}')

        return action_path

# Standalone execution
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print('Usage: python twitter_watcher.py <vault_path> [check_interval]')
        print('Example: python twitter_watcher.py ../AI_Employee_Vault 10800')
        sys.exit(1)

    vault_path = sys.argv[1]
    check_interval = int(sys.argv[2]) if len(sys.argv) > 2 else 10800

    watcher = TwitterWatcher(vault_path, check_interval)

    print(f'\n{"="*60}')
    print(f'[*] Twitter Watcher Started')
    print(f'{"="*60}')
    print(f'Vault: {vault_path}')
    print(f'Check Interval: {check_interval}s ({check_interval//3600}h)')
    print(f'{"="*60}\n')
    print('Monitoring Twitter posting schedule...')
    print('Target: 3 tweets per day')
    print('Press Ctrl+C to stop\n')

    try:
        watcher.run()
    except KeyboardInterrupt:
        print('\n\n[*] Watcher stopped by user')
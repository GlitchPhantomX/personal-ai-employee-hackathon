# SKILL: Twitter Manager

## Purpose
Manage Twitter/X presence for professional networking and thought leadership

## Context
Twitter is for real-time engagement, industry news, and professional networking. Keep tweets concise, relevant, and engaging.

## Tweet Strategy

### Content Types
1. **Industry Insights** (40%) - Trends, observations
2. **Tips & Tricks** (25%) - Actionable advice
3. **Engagement** (20%) - Questions, polls
4. **Company Updates** (10%) - Announcements
5. **Retweets/Comments** (5%) - Community engagement

### Best Practices
- Keep under 280 characters
- Use 1-2 relevant hashtags max
- Tweet 2-3x per day
- Engage with replies within 1 hour
- Retweet industry leaders
- Use threads for longer content

## Input Format

```yaml
action: [tweet|thread|reply]
content: [text]
hashtags: [list]
mention: [if replying to someone]
```

## Output Format

```markdown
---
type: twitter_post
action: [tweet|thread]
status: [draft|pending|posted]
---

## Tweet Content

[Tweet text - max 280 chars]

## Thread (if applicable)
1/ [First tweet]
2/ [Second tweet]
3/ [Third tweet]

## Hashtags
#hashtag1 #hashtag2

## Engagement Strategy
- [How to engage with replies]
- [Related accounts to tag]

## Metrics Target
- Impressions: [estimate]
- Engagement Rate: [target %]
```

## Examples

### Example 1: Industry Insight
**Input:**
```yaml
action: tweet
content: "The future of AI isn't replacing humans, it's augmenting our capabilities"
hashtags: ["AI", "FutureOfWork"]
```

**Output:**
```markdown
The future of AI isn't replacing humans—it's augmenting our capabilities.

Best teams = Human creativity + AI efficiency

What's your take? 👇

#AI #FutureOfWork
```

### Example 2: Thread
**Input:**
```yaml
action: thread
content: "How to build an AI employee system"
```

**Output:**
```markdown
1/ Building an AI Employee system in 2026 🧵

Here's what I learned building a 24/7 autonomous assistant:

2/ Architecture matters. Three layers:
- Watchers (perceive changes)
- Orchestrator (reasoning)
- MCP servers (take actions)

3/ Human-in-the-loop is crucial. AI shouldn't make all decisions alone.

Approval workflow prevents costly mistakes while maintaining automation.

4/ Testing validates everything. 6/6 integration tests passing = confidence.

Without tests, you're flying blind.

5/ Want to build your own? Check out @panaversity's hackathon.

Full code + documentation available.

#AI #Automation #AgenticAI
```
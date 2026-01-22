# SKILL: Facebook & Instagram Manager

## Purpose
Manage Facebook and Instagram presence including posting, engagement tracking, and summary generation

## Context
You are a social media manager responsible for maintaining active and engaging Facebook and Instagram profiles for the business. Focus on brand consistency, audience engagement, and lead generation.

## Social Media Strategy

### Content Types
1. **Business Updates** - Company news, achievements
2. **Industry Insights** - Trends, tips, how-tos
3. **Behind-the-Scenes** - Team culture, process
4. **Customer Testimonials** - Success stories
5. **Product/Service Highlights** - Features, benefits

### Best Practices
- Post consistently (3-5x per week)
- Use high-quality visuals
- Engage with comments within 24h
- Use relevant hashtags (5-10)
- Include call-to-action
- Track engagement metrics

## Input Format

```yaml
platform: [facebook|instagram|both]
action: [post|schedule|analyze|respond]
content_type: [update|insight|testimonial|product]
content: [text content]
media: [image_url or description]
hashtags: [list of hashtags]
```

## Output Format

```markdown
---
type: social_media_post
platform: [facebook|instagram|both]
status: [draft|pending|scheduled|posted]
engagement: {likes, comments, shares}
---

## Post Content

[Main post text - platform optimized]

## Media
[Image/video description or URL]

## Hashtags
#hashtag1 #hashtag2 #hashtag3

## Performance Metrics
- Estimated Reach: [low|medium|high]
- Best Time to Post: [day/time]
- Engagement Prediction: [score]

## Caption Variations

### Facebook Version
[Longer form content, 2-3 paragraphs]

### Instagram Version
[Shorter, visual-focused, more hashtags]

## Approval Required
- [ ] Content reviewed
- [ ] Image/video attached
- [ ] Hashtags relevant
- [ ] Timing appropriate
- [ ] Brand guidelines followed
```

## Examples

### Example 1: Business Achievement Post
**Input:**
```yaml
platform: both
action: post
content_type: update
content: "Celebrating 100 successful projects completed!"
```

**Output:**
```markdown
---
type: social_media_post
platform: both
status: draft
---

## Facebook Version

🎉 Milestone Achieved! 🎉

We're thrilled to announce that we've successfully completed our 100th project! This incredible journey wouldn't have been possible without the trust of our amazing clients and the dedication of our talented team.

From startups to enterprises, each project has been unique, challenging, and rewarding. Here's to the next 100! 🚀

Thank you for being part of our growth story. Looking forward to creating more success together!

#MilestoneAchievement #BusinessGrowth #100Projects #Gratitude #TeamSuccess

---

## Instagram Version

100 projects ✅
100 happy clients ❤️
100 learning experiences 📚
Infinite gratitude 🙏

Thank you for being part of this incredible journey! Here's to many more milestones together 🚀

#Milestone #BusinessSuccess #100Projects #Grateful #SmallBusinessGrowth #Entrepreneurship #ClientSuccess #TeamWork #BusinessGoals #Achievement

[Image suggestion: Team photo or infographic showing "100" creatively]

---

## Posting Strategy
- Facebook: Tomorrow at 10 AM (higher engagement)
- Instagram: Tomorrow at 2 PM (optimal for images)
- Boost post with $20 budget (optional)
```

### Example 2: Customer Testimonial
**Input:**
```yaml
platform: instagram
action: post
content_type: testimonial
content: "Working with them was a game-changer for our business!"
```

**Output:**
```markdown
---
type: social_media_post
platform: instagram
status: draft
---

## Instagram Post

💬 CLIENT LOVE 💬

"Working with them was a game-changer for our business!"
- Sarah T., Founder of TechStart

Nothing makes us happier than seeing our clients succeed! 🌟

Want to transform your business too? Let's talk! Link in bio 👆

#ClientTestimonial #CustomerSuccess #BusinessTransformation #ClientLove #SmallBusiness #Entrepreneur #SuccessStory #HappyClients #BusinessGrowth #Testimonial

[Image: Testimonial quote graphic with client photo (with permission)]

---

## Engagement Strategy
- Respond to all comments within 2 hours
- Save and share to stories
- Tag client (with permission)
- Use Instagram Shopping (if applicable)
```

## Quality Checks
- [ ] Content aligns with brand voice
- [ ] No spelling/grammar errors
- [ ] Appropriate hashtags (5-10)
- [ ] Image/video quality high
- [ ] Call-to-action included
- [ ] Complies with platform guidelines
- [ ] Legal/compliance reviewed (if needed)

## Performance Tracking

### Metrics to Monitor
- Reach & Impressions
- Engagement Rate (likes, comments, shares)
- Click-through Rate
- Follower Growth
- Best Performing Content Types

### Weekly Summary Format
```markdown
## Social Media Performance (Week of [Date])

### Facebook
- Posts: X
- Reach: Y
- Engagement: Z%
- Best Post: [link]

### Instagram
- Posts: X
- Reach: Y
- Engagement: Z%
- Best Post: [link]

### Insights
- What worked well
- What to improve
- Next week's strategy
```
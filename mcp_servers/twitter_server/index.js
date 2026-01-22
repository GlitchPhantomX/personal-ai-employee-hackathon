/**
 * Twitter MCP Server
 * Handles posting to Twitter/X
 */

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
require('dotenv').config();

class TwitterServer {
    constructor() {
        this.server = new Server({
            name: 'twitter-server',
            version: '1.0.0',
        }, {
            capabilities: {
                tools: {}
            }
        });

        this.setupHandlers();
        this.setupErrorHandling();
    }

    setupHandlers() {
        this.server.setRequestHandler('tools/list', async () => ({
            tools: [
                {
                    name: 'post_tweet',
                    description: 'Post a tweet to Twitter/X',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            content: { type: 'string', maxLength: 280 },
                            hashtags: { type: 'array', items: { type: 'string' }, maxItems: 2 }
                        },
                        required: ['content']
                    }
                },
                {
                    name: 'post_thread',
                    description: 'Post a Twitter thread',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            tweets: { type: 'array', items: { type: 'string' } }
                        },
                        required: ['tweets']
                    }
                },
                {
                    name: 'get_twitter_stats',
                    description: 'Get Twitter engagement statistics',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            days: { type: 'number', default: 7 }
                        }
                    }
                }
            ]
        }));

        this.server.setRequestHandler('tools/call', async (request) => {
            const { name, arguments: args } = request.params;

            switch (name) {
                case 'post_tweet':
                    return await this.postTweet(args);
                case 'post_thread':
                    return await this.postThread(args);
                case 'get_twitter_stats':
                    return await this.getTwitterStats(args);
                default:
                    throw new Error(`Unknown tool: ${name}`);
            }
        });
    }

    async postTweet(args) {
        const { content, hashtags = [] } = args;

        console.error('[Twitter MCP] Posting tweet...');

        const tweet = {
            status: 'simulated',
            message: 'Tweet would be posted to Twitter/X',
            content: content,
            hashtags: hashtags,
            timestamp: new Date().toISOString(),
            estimated_impressions: Math.floor(Math.random() * 5000) + 500,
            tweet_id: `TW_${Date.now()}`,
            note: 'For production, integrate Twitter API v2'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(tweet, null, 2)
            }]
        };
    }

    async postThread(args) {
        const { tweets } = args;

        console.error(`[Twitter MCP] Posting thread (${tweets.length} tweets)...`);

        const thread = {
            status: 'simulated',
            message: 'Thread would be posted to Twitter/X',
            tweets: tweets,
            tweet_count: tweets.length,
            timestamp: new Date().toISOString(),
            estimated_impressions: Math.floor(Math.random() * 10000) + 1000,
            thread_id: `TH_${Date.now()}`,
            note: 'For production, integrate Twitter API v2'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(thread, null, 2)
            }]
        };
    }

    async getTwitterStats(args) {
        const { days = 7 } = args;

        console.error(`[Twitter MCP] Getting stats for last ${days} days...`);

        const stats = {
            status: 'simulated',
            period: `Last ${days} days`,
            tweets: Math.floor(Math.random() * 20) + 10,
            impressions: Math.floor(Math.random() * 50000) + 10000,
            engagement_rate: (Math.random() * 3 + 1).toFixed(2) + '%',
            likes: Math.floor(Math.random() * 500) + 100,
            retweets: Math.floor(Math.random() * 100) + 20,
            replies: Math.floor(Math.random() * 150) + 30,
            followers_gained: Math.floor(Math.random() * 50) + 10,
            note: 'Simulated data - integrate Twitter API v2 for production'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(stats, null, 2)
            }]
        };
    }

    setupErrorHandling() {
        this.server.onerror = (error) => {
            console.error('[Twitter MCP] Error:', error);
        };

        process.on('SIGINT', async () => {
            console.error('[Twitter MCP] Shutting down...');
            await this.server.close();
            process.exit(0);
        });
    }

    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('[Twitter MCP] Server running on stdio');
    }
}

const server = new TwitterServer();
server.run().catch(console.error);
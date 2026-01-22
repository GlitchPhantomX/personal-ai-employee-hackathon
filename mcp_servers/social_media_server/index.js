/**
 * Social Media MCP Server (Facebook & Instagram)
 * Handles posting to Facebook and Instagram
 */

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
require('dotenv').config();

class SocialMediaServer {
    constructor() {
        this.server = new Server({
            name: 'social-media-server',
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
                    name: 'post_facebook',
                    description: 'Post content to Facebook',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            content: { type: 'string' },
                            image_url: { type: 'string' },
                            hashtags: { type: 'array', items: { type: 'string' } }
                        },
                        required: ['content']
                    }
                },
                {
                    name: 'post_instagram',
                    description: 'Post content to Instagram',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            content: { type: 'string' },
                            image_url: { type: 'string' },
                            hashtags: { type: 'array', items: { type: 'string' } }
                        },
                        required: ['content', 'image_url']
                    }
                },
                {
                    name: 'get_engagement_stats',
                    description: 'Get engagement statistics',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            platform: { type: 'string', enum: ['facebook', 'instagram', 'both'] },
                            days: { type: 'number', default: 7 }
                        }
                    }
                }
            ]
        }));

        this.server.setRequestHandler('tools/call', async (request) => {
            const { name, arguments: args } = request.params;

            switch (name) {
                case 'post_facebook':
                    return await this.postFacebook(args);
                case 'post_instagram':
                    return await this.postInstagram(args);
                case 'get_engagement_stats':
                    return await this.getEngagementStats(args);
                default:
                    throw new Error(`Unknown tool: ${name}`);
            }
        });
    }

    async postFacebook(args) {
        const { content, image_url, hashtags = [] } = args;

        console.error('[Social MCP] Posting to Facebook...');

        const post = {
            status: 'simulated',
            message: 'Post would be published to Facebook',
            platform: 'facebook',
            content: content,
            image_url: image_url,
            hashtags: hashtags,
            timestamp: new Date().toISOString(),
            estimated_reach: Math.floor(Math.random() * 5000) + 1000,
            post_id: `FB_${Date.now()}`,
            note: 'For production, integrate Facebook Graph API'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(post, null, 2)
            }]
        };
    }

    async postInstagram(args) {
        const { content, image_url, hashtags = [] } = args;

        console.error('[Social MCP] Posting to Instagram...');

        const post = {
            status: 'simulated',
            message: 'Post would be published to Instagram',
            platform: 'instagram',
            content: content,
            image_url: image_url,
            hashtags: hashtags,
            timestamp: new Date().toISOString(),
            estimated_reach: Math.floor(Math.random() * 3000) + 500,
            post_id: `IG_${Date.now()}`,
            note: 'For production, integrate Instagram Graph API'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(post, null, 2)
            }]
        };
    }

    async getEngagementStats(args) {
        const { platform = 'both', days = 7 } = args;

        console.error(`[Social MCP] Getting ${platform} stats for last ${days} days...`);

        const stats = {
            status: 'simulated',
            period: `Last ${days} days`,
            platform: platform,
            facebook: platform === 'facebook' || platform === 'both' ? {
                posts: Math.floor(Math.random() * 10) + 3,
                reach: Math.floor(Math.random() * 10000) + 5000,
                engagement_rate: (Math.random() * 5 + 2).toFixed(2) + '%',
                likes: Math.floor(Math.random() * 500) + 100,
                comments: Math.floor(Math.random() * 50) + 10,
                shares: Math.floor(Math.random() * 30) + 5
            } : null,
            instagram: platform === 'instagram' || platform === 'both' ? {
                posts: Math.floor(Math.random() * 12) + 4,
                reach: Math.floor(Math.random() * 8000) + 3000,
                engagement_rate: (Math.random() * 6 + 3).toFixed(2) + '%',
                likes: Math.floor(Math.random() * 600) + 150,
                comments: Math.floor(Math.random() * 60) + 15,
                saves: Math.floor(Math.random() * 40) + 10
            } : null,
            note: 'Simulated data - integrate actual API for production'
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
            console.error('[Social MCP] Error:', error);
        };

        process.on('SIGINT', async () => {
            console.error('[Social MCP] Shutting down...');
            await this.server.close();
            process.exit(0);
        });
    }

    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('[Social MCP] Server running on stdio');
    }
}

const server = new SocialMediaServer();
server.run().catch(console.error);
/**
 * Xero MCP Server (Gold Tier)
 * Integrates with Xero accounting API
 *
 * For initial implementation: Simulates Xero operations
 * For production: Uses actual Xero API with OAuth
 *
 * Official Xero MCP: https://github.com/XeroAPI/xero-mcp-server
 */

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
require('dotenv').config();

class XeroServer {
    constructor() {
        this.server = new Server({
            name: 'xero-server',
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
        // List available tools
        this.server.setRequestHandler('tools/list', async () => ({
            tools: [
                {
                    name: 'create_invoice',
                    description: 'Create an invoice in Xero',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            client: { type: 'string', description: 'Client name' },
                            amount: { type: 'number', description: 'Invoice amount' },
                            description: { type: 'string', description: 'Invoice description' },
                            due_date: { type: 'string', description: 'Payment due date' }
                        },
                        required: ['client', 'amount', 'description']
                    }
                },
                {
                    name: 'record_expense',
                    description: 'Record a business expense in Xero',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            vendor: { type: 'string' },
                            amount: { type: 'number' },
                            category: { type: 'string' },
                            description: { type: 'string' }
                        },
                        required: ['vendor', 'amount', 'category']
                    }
                },
                {
                    name: 'get_financial_summary',
                    description: 'Get financial summary for a period',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            start_date: { type: 'string' },
                            end_date: { type: 'string' }
                        },
                        required: ['start_date', 'end_date']
                    }
                },
                {
                    name: 'get_account_balance',
                    description: 'Get current account balance',
                    inputSchema: {
                        type: 'object',
                        properties: {}
                    }
                }
            ]
        }));

        // Handle tool execution
        this.server.setRequestHandler('tools/call', async (request) => {
            const { name, arguments: args } = request.params;

            switch (name) {
                case 'create_invoice':
                    return await this.createInvoice(args);
                case 'record_expense':
                    return await this.recordExpense(args);
                case 'get_financial_summary':
                    return await this.getFinancialSummary(args);
                case 'get_account_balance':
                    return await this.getAccountBalance(args);
                default:
                    throw new Error(`Unknown tool: ${name}`);
            }
        });
    }

    async createInvoice(args) {
        const { client, amount, description, due_date } = args;

        console.error('[Xero MCP] Creating invoice...');
        console.error(`Client: ${client}, Amount: ${amount}`);

        // Gold Tier: Simulate invoice creation
        // Production: Would call actual Xero API

        const invoice = {
            status: 'simulated',
            message: 'Invoice created in Xero (simulated)',
            invoice_number: `INV-${Date.now()}`,
            client: client,
            amount: amount,
            description: description,
            due_date: due_date || this.getDefaultDueDate(),
            created_date: new Date().toISOString(),
            status_xero: 'DRAFT',
            note: 'For production, integrate with actual Xero API using OAuth'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(invoice, null, 2)
            }]
        };
    }

    async recordExpense(args) {
        const { vendor, amount, category, description } = args;

        console.error('[Xero MCP] Recording expense...');
        console.error(`Vendor: ${vendor}, Amount: ${amount}`);

        const expense = {
            status: 'simulated',
            message: 'Expense recorded in Xero (simulated)',
            expense_id: `EXP-${Date.now()}`,
            vendor: vendor,
            amount: amount,
            category: category,
            description: description,
            date: new Date().toISOString(),
            tax_amount: (amount * 0.1).toFixed(2),
            note: 'For production, integrate with actual Xero API'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(expense, null, 2)
            }]
        };
    }

    async getFinancialSummary(args) {
        const { start_date, end_date } = args;

        console.error('[Xero MCP] Getting financial summary...');
        console.error(`Period: ${start_date} to ${end_date}`);

        // Simulated financial data
        const summary = {
            status: 'simulated',
            period: {
                start: start_date,
                end: end_date
            },
            revenue: {
                total_invoiced: 15000,
                total_paid: 12000,
                outstanding: 3000
            },
            expenses: {
                total: 5000,
                by_category: {
                    'Cloud Services': 500,
                    'Software': 800,
                    'Marketing': 1200,
                    'Operations': 2500
                }
            },
            profit: {
                gross: 10000,
                net: 7000,
                margin: '46.7%'
            },
            cash_flow: {
                opening_balance: 25000,
                closing_balance: 32000,
                net_change: 7000
            },
            note: 'Simulated data - integrate actual Xero API for production'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(summary, null, 2)
            }]
        };
    }

    async getAccountBalance(args) {
        console.error('[Xero MCP] Getting account balance...');

        const balance = {
            status: 'simulated',
            accounts: [
                {
                    name: 'Business Checking',
                    balance: 32000,
                    currency: 'USD'
                },
                {
                    name: 'Savings',
                    balance: 15000,
                    currency: 'USD'
                }
            ],
            total: 47000,
            updated: new Date().toISOString(),
            note: 'Simulated data - integrate actual Xero API for production'
        };

        return {
            content: [{
                type: 'text',
                text: JSON.stringify(balance, null, 2)
            }]
        };
    }

    getDefaultDueDate() {
        const date = new Date();
        date.setDate(date.getDate() + 30); // 30 days from now
        return date.toISOString().split('T')[0];
    }

    setupErrorHandling() {
        this.server.onerror = (error) => {
            console.error('[Xero MCP] Error:', error);
        };

        process.on('SIGINT', async () => {
            console.error('[Xero MCP] Shutting down...');
            await this.server.close();
            process.exit(0);
        });
    }

    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('[Xero MCP] Server running on stdio');
        console.error('[Xero MCP] Note: Using simulated data for Gold tier demo');
        console.error('[Xero MCP] For production: Integrate with https://github.com/XeroAPI/xero-mcp-server');
    }
}

// Start server
const server = new XeroServer();
server.run().catch(console.error);
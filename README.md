# 🚀 CapsuleCRM MCP Server

Transform your CRM workflow with AI! This MCP (Model Context Protocol) server connects Claude AI directly to your CapsuleCRM account, enabling natural language interactions with your customer data.

## ✨ What This Server Does

This server acts as a bridge between Claude AI and your CapsuleCRM account, allowing you to:

- 🗣️ **Talk to your CRM in plain English** - Ask questions like "Show me all VIP customers from last month" or "Create a new opportunity for Acme Corp"
- 🔍 **Smart search and filtering** - Find exactly what you need using powerful search capabilities
- 📊 **Get instant insights** - Query your sales pipeline, customer data, and tasks without clicking through CapsuleCRM's interface
- ⚡ **Automate routine tasks** - Create, update, and manage CRM data through conversational AI

## 🎯 Key Capabilities

### 👥 Customer Management (Parties)
- **View all customers**: List people and organizations with pagination
- **Smart search**: Find customers by name, email, phone, or address
- **Advanced filtering**: Filter by tags, location, contact info, and more
- **Full CRUD operations**: Create, read, update customer records
- **Rich details**: Access complete contact information, addresses, and custom fields

### 💼 Sales Pipeline (Opportunities)
- **Track deals**: Monitor all sales opportunities and their progress
- **Value calculations**: Automatic probability-weighted values for accurate reporting
- **Pipeline stages**: View and update opportunities through different milestones
- **Comprehensive filtering**: Find deals by status, owner, value, close date, and more
- **Revenue insights**: Get real-time view of your sales pipeline value

### ✅ Task Management
- **Stay organized**: View, create, and update tasks across your team
- **Status tracking**: Filter tasks by open, completed, or pending status
- **Due date management**: Track deadlines and overdue items
- **Assignment control**: See who's responsible for what
- **Context awareness**: Link tasks to specific customers or deals

### 🎯 Pipeline Configuration
- **Milestone overview**: View all pipeline stages and their settings
- **Progress tracking**: Understand where opportunities stand in your sales process

## 🔧 Advanced Search Features

### Simple Text Search
```
"Find customers named John"
"Show me tasks due this week"
"Search for opportunities with 'software' in the name"
```

### Powerful Filtering
```
Filter customers by:
- 🏷️ Tags (VIP, Hot Lead, etc.)
- 📍 Location (city, country)
- 👤 Owner/Team assignment
- 📅 Date ranges (added, updated, last contacted)

Filter opportunities by:
- 📈 Status (open, closed, won, lost)
- 💰 Value ranges
- 🎯 Pipeline stages
- 👥 Assigned owners
- 📅 Expected close dates

Filter tasks by:
- ✅ Status (open, completed, pending)
- 👤 Assignee
- 📅 Due dates
- 🏷️ Categories and tags
```

### Advanced Operator Support
Use sophisticated filtering with operators like:
- `contains` - Find partial matches
- `starts with` / `ends with` - Prefix/suffix matching
- `is after` / `is before` - Date comparisons
- `is greater than` / `is less than` - Numerical comparisons
- `is within last` - Recent time periods

## 🚀 Getting Started

### Prerequisites
- CapsuleCRM account with API access
- Claude desktop app or compatible MCP client
- Your CapsuleCRM API token

### Quick Setup
1. **Get your API token** from CapsuleCRM (Account Settings → API)
2. **Set environment variable**: `CAPSULECRM_ACCESS_TOKEN=your_token_here`
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Run the server**: `python mcp_server.py`

### Connect to Claude
Add this server to your Claude desktop configuration to start using natural language CRM commands!

## 💡 Example Use Cases

### 📊 Sales Reporting
- "What's the total value of our open opportunities?"
- "Show me all deals closing this quarter"
- "Which opportunities have the highest probability?"

### 👥 Customer Insights
- "Find all VIP customers in New York"
- "Show me customers we haven't contacted in 30 days"
- "List all organizations in the technology sector"

### ✅ Task Management
- "What tasks are overdue?"
- "Show me all tasks assigned to Sarah"
- "Create a follow-up task for next week"

### 🔍 Data Discovery
- "Find opportunities over $50,000"
- "Show me customers added this month"
- "Which deals are stuck in the proposal stage?"

## 🔧 Technical Features

### 🎯 User-Centric Design
- **Privacy-friendly**: No internal IDs exposed to users
- **Calculated values**: Automatic probability-weighted opportunity values
- **Smart value handling**: Supports both per-unit and total value types for opportunities
- **Rich documentation**: All tools and models clearly documented for AI understanding

### 🔍 Intelligent Search
- **Automatic method selection**: Uses search vs. filter based on query type
- **Multiple operators**: Support for 8+ filter operators
- **Flexible syntax**: Two ways to specify operators in queries
- **Pagination support**: Handle large datasets efficiently

### 💰 Opportunity Value Logic
When creating opportunities, specify whether the value is:
- **Per unit** (`value_type: "per_unit"`): e.g., $1000 per month
- **Total** (`value_type: "total"`): e.g., $6000 total for 6 months

The server automatically calculates:
- **Total value**: Base amount × duration
- **Current value**: Probability-weighted value for reporting

## 🛡️ Security & Privacy

- **Secure authentication**: Uses official CapsuleCRM API with token-based auth
- **Read/write permissions**: Full control over your CRM data through AI
- **No data storage**: Server acts as a real-time bridge, doesn't store your data
- **Environment variables**: API tokens stored securely in environment variables

## 🎉 Why Use This?

Instead of clicking through CRM interfaces, you can now:
- **Save time**: Get answers in seconds, not minutes
- **Ask complex questions**: Combine multiple filters and searches naturally
- **Automate workflows**: Let AI handle routine CRM tasks
- **Stay in flow**: Work with your CRM data without context switching
- **Discover insights**: Ask questions you might not have thought to explore in the UI

Transform your CRM experience from manual data entry to intelligent conversation! 🚀

---

*Built with FastMCP and love for better CRM workflows* ❤️
# 🚀 CapsuleCRM MCP Server

Transform your CRM workflow with AI! 🤖✨ Connect Claude directly to your CapsuleCRM account for natural language customer and sales management.

## 🎯 What it does

- 🗣️ **Talk to your CRM in plain English** - "Show me all VIP customers from last month"
- 🔍 **Smart search and filtering** - Find exactly what you need with powerful queries
- 📊 **Get instant insights** - Query sales pipeline, customer data, and tasks
- ⚡ **Automate routine tasks** - Create, update, and manage CRM data through conversation

## 🎉 Installation

### 🖥️ Claude Desktop 
1. 📥 Download the `capsulecrm-mcp.dxt` file
2. 👆 Double-click to install in Claude Desktop
3. 🔑 Enter your CapsuleCRM API key when prompted
4. 🎊 Start using natural language CRM commands!

## 🔑 Getting Your API Key

1. 🌐 Log in to your CapsuleCRM dashboard
2. ⚙️ Go to **Account Settings** → **API**
3. ✨ Generate a new API token
4. 💾 Copy and store securely (you won't see it again!)

## 💡 Usage Examples

### 👥 Customer Management
- 🔍 "Find all VIP customers in New York"
- 📅 "Show me customers we haven't contacted in 30 days"
- ➕ "Create a new person: John Smith, john@acme.com"

### 💰 Sales Pipeline
- 💎 "What's the total value of our open opportunities?"
- 📈 "Show me deals closing this quarter"
- 🎯 "Create a new opportunity for Acme Corp worth $25,000"

### ✅ Task Management
- ⏰ "What tasks are overdue?"
- 👩‍💼 "Show me all tasks assigned to Sarah"
- 📝 "Create a follow-up task for next Friday"

### 🔮 Advanced Filtering
Ask complex questions like:
- 💵 "Find opportunities worth more than $50,000 that are in proposal stage"
- 🏷️ "Show me customers added in the last 30 days with hot-lead tags"
- 👥 "List all overdue tasks assigned to my team"

## 🎪 Capabilities

**👥 Customer Management (Parties)**
- 👀 View, create, update people and organizations
- 🔎 Search by name, email, phone, address
- 🏷️ Filter by tags, location, contact info

**💼 Sales Pipeline (Opportunities)**
- 📊 Track deals and progress through stages
- 🎲 Automatic probability-weighted values
- 🔍 Comprehensive filtering and search
- 💰 Revenue insights and reporting

**✅ Task Management**
- 📋 Create, view, and update tasks
- 🎯 Filter by status, assignee, due dates
- 🔗 Link tasks to customers and deals

**🎯 Pipeline Configuration**
- 📈 View all pipeline milestones
- 🚀 Track opportunity progress through stages

## 🔧 Search Operators

- 🔍 `contains` - Find partial matches
- 🎯 `starts with` / `ends with` - Prefix/suffix matching
- 📅 `is after` / `is before` - Date comparisons
- 📊 `is greater than` / `is less than` - Numerical filtering
- ⏰ `is within last` - Recent time periods

## 🚨 Troubleshooting

**🚫 Extension won't start:**
- ✅ Verify your API key is correct
- 🌐 Check internet connection to CapsuleCRM
- 🐍 Ensure Python 3.11+ is installed

**📦 "No module found" errors:**
- 🎁 Dependencies are bundled in the extension
- 🔄 Try reinstalling the extension

**⚠️ API errors:**
- 🔐 Verify API key permissions in CapsuleCRM
- 🚦 Check rate limits aren't exceeded

**🐛 Debug Mode:**
Set environment variable `LOG_LEVEL=DEBUG` for detailed logging.

## 🛡️ Security & Privacy

- 🔐 Uses official CapsuleCRM API with secure token authentication
- 🚫 No data storage - acts as real-time bridge
- 🔒 Environment variables for secure token storage
- ✅ Full read/write permissions as configured in CapsuleCRM

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏢 About

Developed by [Monads AG](https://monads.ch) - specialists in AI automation and business process optimization.

---

*Ready to transform your CRM experience? Let's make data management fun! 🎉🚀*
# 🧳 Corporate Travel Concierge Agent  
### Multi-Agent AI System | Capstone Project | 2025

This project is a fully functional **multi-agent corporate travel automation system** designed to streamline end-to-end business travel for organizations.  

It demonstrates the key concepts required for the capstone:

- Multi-Agent Systems  
- LLM-powered Agents  
- Parallel & Sequential Agents  
- Tools (Custom + Built-in)  
- Sessions & State Management  
- Long-Term Memory  
- Observability  
- Agent Evaluation  
- Deployment-ready structure  

---

# 📌 1. Problem Statement

Organizations frequently struggle with managing corporate travel due to fragmented processes involving requests, approvals, booking coordination, and expense submissions.  

Manual workflows lead to:  
- Delays in travel approvals  
- Policy violations  
- Higher travel costs  
- Poor visibility into employee travel  
- Increased HR/admin overhead  

---

# 🎯 2. Solution Overview

This project introduces an **AI-Powered Corporate Travel Concierge Agent** that automates the full travel workflow:

1. Parse natural-language travel requests  
2. Validate against corporate policy  
3. Search for flights  
4. Book the best option  
5. Create expense report drafts  
6. Notify employees  
7. Store trip history (long-term memory)

Built using a **multi-agent architecture**, each agent handles a specific responsibility.

---

# 🤖 3. Multi-Agent Architecture

### **Agents**
| Agent | Responsibility |
|-------|----------------|
| **RequestAgent** | Converts natural language → structured JSON |
| **PolicyAgent** | Validates compliance with corporate rules |
| **SearchAgent** | Retrieves and filters flight options |
| **BookingAgent** | Creates flight booking confirmations |
| **ExpenseAgent** | Generates expense draft post-booking |

### **Memory**
| Module | Purpose |
|--------|---------|
| **SessionManager** | Short-term workflow memory |
| **LongTermMemory** | Stores historical trips & preferences |

### **Tools**
| Tool | Usage |
|------|-------|
| **TravelAPIMock** | Returns sample flights (API simulation) |
| **NotificationTool** | Simulates notifications |
| **OCR Tool** | (Optional) Extracts invoice data |

---

# 🧩 4. Architecture Diagram

```mermaid
flowchart TD

A[User Input] --> B[Request Agent]
B --> C[Policy Agent]
C -->|Approved| D[Search Agent]
D --> E[Booking Agent]
E --> F[Expense Agent]
F --> G[Notification Tool]

E --> H[Long-Term Memory]
B --> I[Session Memory]
C --> I
D --> I
E --> I

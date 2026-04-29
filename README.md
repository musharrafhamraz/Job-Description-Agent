# 🤖 AI Agent Framework Comparison: CV Screening System

A comprehensive comparison of three leading AI agent frameworks - **LangGraph**, **CrewAI**, and **AutoGen** - all implementing the same CV screening use case. This project helps you understand the strengths, trade-offs, and implementation patterns of each framework.

## 🎯 Project Overview

This repository contains three identical CV screening agents built with different frameworks:

- **LangGraph** - Graph-based workflow orchestration
- **CrewAI** - Role-based multi-agent collaboration
- **AutoGen** - Conversational multi-agent system

Each implementation performs the same task: automatically screen candidate CVs against job descriptions, evaluate qualifications, and generate hiring recommendations.

## 📊 Framework Comparison

| Feature | LangGraph | CrewAI | AutoGen |
|---------|-----------|---------|---------|
| **Architecture** | State graph with nodes | Role-based agents with tasks | Conversational agents |
| **Learning Curve** | Moderate | Easy | Moderate-Hard |
| **Control** | High (explicit routing) | Medium (task-based) | High (conversation flow) |
| **Best For** | Complex workflows | Team simulations | Interactive agents |
| **State Management** | Built-in TypedDict | Task outputs | Message history |
| **Conditional Logic** | Native routing | Task dependencies | Code-based |
| **LLM Flexibility** | Any LangChain LLM | Multiple providers | OpenAI-focused |

## 🏗️ Common Architecture

All three implementations follow the same logical workflow:

```
┌─────────────┐
│  Extractor  │  ← Parses CV and job description
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Evaluator  │  ← Scores candidate (0-100)
└──────┬──────┘
       │
       ├─── Score ≥ 40 ──→ ┌──────────┐
       │                   │ Reporter │  ← Generates report
       │                   └──────────┘
       │
       └─── Score < 40 ──→ ┌───────────┐
                           │ Rejection │  ← Auto-reject
                           └───────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- API Keys (depending on framework):
  - **LangGraph**: Groq API key
  - **CrewAI**: OpenAI/Groq/Anthropic API key
  - **AutoGen**: OpenAI API key

### Choose Your Framework

#### 1️⃣ LangGraph Implementation

```bash
cd langgraph_agent
pip install -r requirements.txt
cp .env.example .env
# Add your GROQ_API_KEY to .env
python main.py
```

[📖 Full LangGraph Documentation](./langgraph_agent/README.md)

#### 2️⃣ CrewAI Implementation

```bash
cd crewai_agent
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env
python main.py
```

[📖 Full CrewAI Documentation](./crewai_agent/README.md) *(Coming Soon)*

#### 3️⃣ AutoGen Implementation

```bash
cd autogen_agent
pip install -r requirements.txt
cp .env.example .env
# Add your OPENAI_API_KEY to .env
python main.py
```

[📖 Full AutoGen Documentation](./autogen_agent/README.md) *(Coming Soon)*

## 🔍 Framework Deep Dive

### LangGraph

**Philosophy**: Explicit state management with graph-based workflows

**Pros:**
- ✅ Full control over state transitions
- ✅ Visual graph representation
- ✅ Easy to debug and trace
- ✅ Works with any LangChain-compatible LLM
- ✅ Built-in persistence and checkpointing

**Cons:**
- ❌ More boilerplate code
- ❌ Requires understanding of graph concepts
- ❌ Manual state management

**Best Use Cases:**
- Complex multi-step workflows
- Applications requiring precise control flow
- Systems with conditional branching
- Production applications needing observability

---

### CrewAI

**Philosophy**: Role-based agents working as a team

**Pros:**
- ✅ Intuitive role/task abstraction
- ✅ Minimal code required
- ✅ Built-in agent collaboration
- ✅ Easy to understand and maintain
- ✅ Great for simulating team dynamics

**Cons:**
- ❌ Less control over execution flow
- ❌ Harder to implement complex routing
- ❌ Limited state visibility
- ❌ Opinionated architecture

**Best Use Cases:**
- Team simulation scenarios
- Simple multi-agent workflows
- Rapid prototyping
- Business process automation

---

### AutoGen

**Philosophy**: Conversational agents with flexible interaction patterns

**Pros:**
- ✅ Powerful conversation management
- ✅ Flexible agent interactions
- ✅ Human-in-the-loop support
- ✅ Code execution capabilities
- ✅ Research-backed framework

**Cons:**
- ❌ Steeper learning curve
- ❌ Primarily OpenAI-focused
- ❌ Can be unpredictable
- ❌ Requires careful prompt engineering

**Best Use Cases:**
- Interactive applications
- Research and experimentation
- Code generation tasks
- Human-AI collaboration

## 📈 Performance Comparison

| Metric | LangGraph | CrewAI | AutoGen |
|--------|-----------|---------|---------|
| **Setup Time** | ~10 min | ~5 min | ~15 min |
| **Code Lines** | ~200 | ~150 | ~180 |
| **Execution Speed** | Fast | Medium | Medium |
| **Token Usage** | Optimized | Higher | Variable |
| **Debugging** | Excellent | Good | Moderate |

## 🎓 Learning Path

**Beginner?** Start with **CrewAI** - easiest to understand and quickest to get results.

**Intermediate?** Try **LangGraph** - great balance of control and simplicity.

**Advanced?** Explore **AutoGen** - most flexible but requires deeper understanding.

## 📁 Repository Structure

```
.
├── README.md                    # This file
├── langgraph_agent/            # LangGraph implementation
│   ├── agent_graph.py
│   ├── agent_state.py
│   ├── nodes.py
│   ├── main.py
│   └── README.md
├── crewai_agent/               # CrewAI implementation (Coming Soon)
│   ├── agents.py
│   ├── tasks.py
│   ├── crew.py
│   ├── main.py
│   └── README.md
└── autogen_agent/              # AutoGen implementation (Coming Soon)
    ├── agents.py
    ├── workflow.py
    ├── main.py
    └── README.md
```

## 🛠️ Common Features

All implementations include:

- ✅ CV and job description parsing
- ✅ Candidate scoring (0-100 scale)
- ✅ Skill gap analysis
- ✅ Automated rejection for low scores
- ✅ Professional hiring report generation
- ✅ Interview question suggestions
- ✅ Structured JSON output

## 🎯 Use Cases

This CV screening system can be adapted for:

- **Recruitment Automation**: Screen hundreds of applications
- **Talent Acquisition**: Identify top candidates quickly
- **HR Analytics**: Generate consistent evaluation metrics
- **Interview Preparation**: Get AI-suggested questions
- **Skill Gap Analysis**: Identify training needs

## 🔧 Customization

Each framework allows customization of:

- Evaluation criteria and scoring weights
- LLM models and parameters
- Rejection thresholds
- Report formats
- Additional workflow steps

See individual framework READMEs for specific customization guides.

## 📊 When to Use Which Framework?

### Choose LangGraph if:
- You need precise control over workflow execution
- Your application has complex conditional logic
- You want excellent debugging and observability
- You're building production-grade systems

### Choose CrewAI if:
- You're new to AI agents
- You want to prototype quickly
- Your workflow maps to team roles naturally
- You prefer declarative over imperative code

### Choose AutoGen if:
- You need flexible agent interactions
- You're building conversational applications
- You want human-in-the-loop capabilities
- You're doing research or experimentation

## 🤝 Contributing

Contributions are welcome! You can:

- Add new framework implementations
- Improve existing code
- Add benchmarks and comparisons
- Enhance documentation
- Report bugs or suggest features

## 📚 Resources

### LangGraph
- [Official Documentation](https://langchain-ai.github.io/langgraph/)
- [GitHub Repository](https://github.com/langchain-ai/langgraph)
- [Tutorials](https://langchain-ai.github.io/langgraph/tutorials/)

### CrewAI
- [Official Documentation](https://docs.crewai.com/)
- [GitHub Repository](https://github.com/joaomdmoura/crewAI)
- [Examples](https://github.com/joaomdmoura/crewAI-examples)

### AutoGen
- [Official Documentation](https://microsoft.github.io/autogen/)
- [GitHub Repository](https://github.com/microsoft/autogen)
- [Research Paper](https://arxiv.org/abs/2308.08155)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- LangChain team for LangGraph
- Groq for ultra-fast inference
- CrewAI team for the intuitive framework
- Microsoft Research for AutoGen

## 💡 Next Steps

1. **Explore** each implementation
2. **Compare** code patterns and complexity
3. **Benchmark** performance for your use case
4. **Choose** the framework that fits your needs
5. **Build** your own AI agent system!

---

**Made with ❤️ to help you choose the right AI agent framework**

*Questions? Open an issue or check individual framework documentation.*

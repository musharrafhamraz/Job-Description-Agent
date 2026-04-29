# 🤖 AI-Powered CV Screening Agent

An intelligent multi-agent system built with **LangGraph** and **Groq** that automates the CV screening process. This system extracts candidate information, evaluates qualifications against job requirements, and generates comprehensive hiring reports.

![Agent Workflow](Screenshot%202026-04-29%20143348.png)

## ✨ Features

- **🔍 Intelligent Extraction**: Automatically parses CVs and job descriptions to extract structured information
- **📊 Smart Evaluation**: Scores candidates on a 0-100 scale with detailed skill matching analysis
- **📝 Professional Reports**: Generates comprehensive hiring recommendations with interview questions
- **🔀 Conditional Routing**: Automatically routes low-scoring candidates to rejection workflow
- **⚡ Powered by Groq**: Ultra-fast inference using Groq's LPU technology with Llama 3.3 70B

## 🏗️ Architecture

The system uses a **multi-agent workflow** with three specialized nodes:

1. **Extractor Agent**: Parses CV and job description into structured data
2. **Evaluator Agent**: Scores candidate fit and identifies gaps/strengths
3. **Reporter Agent**: Generates final hiring recommendation report

### Workflow Diagram

```
┌─────────────┐
│  Extractor  │  ← Extracts structured info
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Evaluator  │  ← Scores & evaluates
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
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   cd langgraph_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

### Running the Agent

```bash
python main.py
```

## 📋 Usage Example

The system processes a CV against a job description and outputs:

### Input
- **CV**: Candidate's resume with skills, experience, and education
- **Job Description**: Role requirements, must-have/nice-to-have skills

### Output

**Structured Evaluation:**
```json
{
  "overall_score": 82,
  "verdict": "Strong Yes",
  "matched_skills": ["Python", "FastAPI", "AWS", "LangChain"],
  "missing_skills": ["Kubernetes", "Pinecone"],
  "strengths": ["Strong backend experience", "AI framework knowledge"],
  "red_flags": [],
  "experience_match": "Good Match",
  "interview_topics": ["MLOps practices", "Vector database experience", "System design"]
}
```

**Professional Report:**
```
EXECUTIVE SUMMARY
Strong Yes - Candidate demonstrates excellent technical fit with 6 years of 
relevant experience and strong alignment with core requirements...

SKILL MATCH ANALYSIS
✓ Python (6 years) - Exceeds requirement
✓ LangChain - Direct match
✓ AWS - Strong cloud experience
✗ Kubernetes - Missing but not critical
...
```

## 🛠️ Customization

### Modify Evaluation Criteria

Edit `nodes.py` to adjust the evaluation prompt:

```python
def evaluator_node(state: AgentState) -> dict:
    prompt = f"""
    # Customize your evaluation criteria here
    """
```

### Change LLM Model

Update the model in `nodes.py`:

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # or "mixtral-8x7b-32768"
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)
```

### Adjust Rejection Threshold

Modify the score threshold in `conditional_routing.py`:

```python
def should_continue(state: AgentState) -> str:
    score = state['evaluation']['overall_score']
    if score < 40:  # Change this threshold
        return "reject"
    else:
        return "report"
```

## 📁 Project Structure

```
langgraph_agent/
├── agent_state.py           # State schema definition
├── nodes.py                 # Agent node implementations
├── agent_graph.py           # Graph structure & compilation
├── conditional_routing.py   # Routing logic
├── main.py                  # Entry point with sample data
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | ✅ Yes |

### Available Groq Models

- `llama-3.3-70b-versatile` (Default) - Best for complex reasoning
- `llama-3.1-8b-instant` - Faster, good for simpler tasks
- `mixtral-8x7b-32768` - Large context window

## 🎯 Use Cases

- **Recruitment Automation**: Screen hundreds of CVs in minutes
- **Talent Acquisition**: Identify top candidates quickly
- **HR Analytics**: Generate consistent evaluation metrics
- **Interview Preparation**: Get AI-suggested interview questions

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph) by LangChain
- Powered by [Groq](https://groq.com/) for ultra-fast inference
- Uses [LangChain](https://github.com/langchain-ai/langchain) framework

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- Visit [Groq documentation](https://console.groq.com/docs)

---

**Made with ❤️ using LangGraph and Groq**

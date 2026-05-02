# 🤖 AI-Powered CV Screening Agent (CrewAI)

An intelligent multi-agent system built with **CrewAI** and **Groq** that automates the CV screening process. This system uses role-based agents working as a team to extract candidate information, evaluate qualifications against job requirements, and generate comprehensive hiring reports.

## ✨ Features

- **🔍 Intelligent Extraction**: Automatically parses CVs and job descriptions to extract structured information
- **📊 Smart Evaluation**: Scores candidates on a 0-100 scale with detailed skill matching analysis
- **📝 Professional Reports**: Generates comprehensive hiring recommendations with interview questions
- **👥 Role-Based Agents**: Three specialized agents working collaboratively
- **⚡ Powered by Groq**: Ultra-fast inference using Groq's LPU technology
- **📋 Structured Output**: Pydantic models ensure consistent, validated evaluation data

## 🏗️ Architecture

The system uses **CrewAI's role-based architecture** with three specialized agents:

1. **Extractor Agent** (Technical Recruiter Assistant): Parses CV and job description into structured data
2. **Evaluator Agent** (Senior Hiring Manager): Scores candidate fit and identifies gaps/strengths
3. **Reporter Agent** (Professional Report Writer): Generates final hiring recommendation report

### Workflow Diagram

```
┌─────────────────────┐
│  Extractor Agent    │  ← Extracts structured info
│  (Recruiter)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Evaluator Agent    │  ← Scores & evaluates
│  (Hiring Manager)   │     (Structured Pydantic output)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Reporter Agent     │  ← Generates report
│  (Report Writer)    │     (Markdown output)
└─────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10-3.13
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Navigate to the project directory**
   ```bash
   cd agent_crewai
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
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

**Option 1: Using Python directly**
```bash
python -m agent_crewai.main
```

**Option 2: Using the installed script**
```bash
run_crew
```

**Option 3: From Python code**
```python
from agent_crewai.crew import AgentCrewai

inputs = {
    'cv_text': "Your CV text here...",
    'job_description': "Your job description here..."
}

result = AgentCrewai().crew().kickoff(inputs=inputs)
```

## 📋 Usage Example

### Input
- **CV**: Candidate's resume with skills, experience, and education
- **Job Description**: Role requirements, must-have/nice-to-have skills

### Output

**Console Output:**
```
================================================================================
CV SCREENING COMPLETE
================================================================================

📊 Overall Score: 82/100
✅ Verdict: Strong Yes

🎯 Matched Skills: Python, FastAPI, AWS, LangChain
❌ Missing Skills: Kubernetes, Pinecone

💪 Key Strengths:
   - Strong backend experience with 6 years
   - Direct experience with LangChain and AI frameworks
   - Solid cloud deployment experience with AWS

📈 Experience Match: Good Match

💬 Interview Topics:
   - MLOps practices and experience
   - Vector database knowledge
   - System design for AI applications

================================================================================
📄 Full report saved to: hiring_report.md
================================================================================
```

**Structured Evaluation (Pydantic):**
```python
{
  "overall_score": 82,
  "verdict": "Strong Yes",
  "matched_skills": ["Python", "FastAPI", "AWS", "LangChain"],
  "missing_skills": ["Kubernetes", "Pinecone"],
  "strengths": [
    "Strong backend experience",
    "AI framework knowledge",
    "Cloud deployment expertise"
  ],
  "red_flags": [],
  "experience_match": "Good Match",
  "interview_topics": [
    "MLOps practices",
    "Vector database experience",
    "System design"
  ]
}
```

**Professional Report (hiring_report.md):**
```markdown
# EXECUTIVE SUMMARY
Strong Yes - Candidate demonstrates excellent technical fit with 6 years of 
relevant experience and strong alignment with core requirements...

# SKILL MATCH ANALYSIS
✓ Python (6 years) - Exceeds requirement
✓ LangChain - Direct match
✓ AWS - Strong cloud experience
✗ Kubernetes - Missing but not critical
...
```

## 🛠️ Customization

### Modify Agent Roles and Behaviors

Edit `src/agent_crewai/config/agents.yaml`:

```yaml
evaluator_agent:
  role: >
    Senior Technical Hiring Manager
  goal: >
    Your custom goal here
  backstory: >
    Your custom backstory here
```

### Modify Task Descriptions

Edit `src/agent_crewai/config/tasks.yaml`:

```yaml
evaluation_task:
  description: >
    Your custom task description here
  expected_output: >
    Your expected output format here
```

### Change LLM Provider

CrewAI supports multiple LLM providers. Update your `.env`:

**For OpenAI:**
```bash
OPENAI_API_KEY=your_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
```

**For Anthropic:**
```bash
ANTHROPIC_API_KEY=your_key_here
```

**For Groq (default):**
```bash
GROQ_API_KEY=your_key_here
```

### Adjust Evaluation Criteria

Modify the scoring logic in `config/tasks.yaml` under `evaluation_task`:

```yaml
evaluation_task:
  description: >
    Provide an objective score from 0-100 where:
    - 0-39: Not a fit (reject)
    - 40-59: Possible fit (maybe)
    - 60-79: Good fit (yes)
    - 80-100: Excellent fit (strong yes)
```

### Add Custom Tools

Create tools in `src/agent_crewai/tools/` and assign them to agents:

```python
from crewai_tools import tool

@tool
def custom_skill_matcher(skills: str) -> str:
    """Custom skill matching logic"""
    # Your implementation
    pass
```

Then add to an agent in `crew.py`:

```python
@agent
def evaluator_agent(self) -> Agent:
    return Agent(
        config=self.agents_config['evaluator_agent'],
        tools=[custom_skill_matcher],
        verbose=True
    )
```

## 📁 Project Structure

```
agent_crewai/
├── src/
│   └── agent_crewai/
│       ├── config/
│       │   ├── agents.yaml       # Agent definitions
│       │   └── tasks.yaml        # Task definitions
│       ├── tools/                # Custom tools (optional)
│       ├── crew.py               # Crew orchestration
│       ├── main.py               # Entry point
│       └── __init__.py
├── pyproject.toml               # Project configuration & dependencies
├── .env.example                 # Environment template
├── .gitignore
└── README.md                    # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | ✅ Yes (or use alternative) |
| `OPENAI_API_KEY` | Your OpenAI API key | Alternative |
| `ANTHROPIC_API_KEY` | Your Anthropic API key | Alternative |

### Available Models

**Groq (Recommended - Fast & Free):**
- `llama-3.3-70b-versatile` (Default)
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`

**OpenAI:**
- `gpt-4o-mini`
- `gpt-4o`
- `gpt-4-turbo`

**Anthropic:**
- `claude-3-5-sonnet-20241022`
- `claude-3-opus-20240229`

## 🎯 Use Cases

- **Recruitment Automation**: Screen hundreds of CVs in minutes
- **Talent Acquisition**: Identify top candidates quickly
- **HR Analytics**: Generate consistent evaluation metrics
- **Interview Preparation**: Get AI-suggested interview questions
- **Skill Gap Analysis**: Identify training needs for existing teams

## 🔄 Advanced Features

### Training the Crew

Improve agent performance through training:

```bash
train 5 training_data.pkl
```

### Testing the Crew

Evaluate crew performance:

```bash
test 3 gpt-4o-mini
```

### Replaying Tasks

Replay a specific task execution:

```bash
replay <task_id>
```

## 🆚 CrewAI vs LangGraph

| Feature | CrewAI | LangGraph |
|---------|--------|-----------|
| **Abstraction** | High (role-based) | Medium (graph-based) |
| **Code Complexity** | Lower | Higher |
| **Control** | Task dependencies | Explicit routing |
| **Best For** | Team simulations | Complex workflows |
| **Learning Curve** | Easy | Moderate |

**Choose CrewAI if:**
- You want quick setup and minimal code
- Your workflow maps naturally to team roles
- You prefer declarative configuration (YAML)
- You're new to AI agents

**Choose LangGraph if:**
- You need precise control over execution flow
- You have complex conditional logic
- You want explicit state management
- You need advanced debugging capabilities

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [CrewAI](https://www.crewai.com/) framework
- Powered by [Groq](https://groq.com/) for ultra-fast inference
- Uses [LangChain](https://github.com/langchain-ai/langchain) ecosystem

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Check the [CrewAI documentation](https://docs.crewai.com/)
- Visit [Groq documentation](https://console.groq.com/docs)

## 🔗 Related Implementations

This CV screening system is also implemented with:
- **LangGraph**: Graph-based workflow orchestration
- **AutoGen**: Conversational multi-agent system

See the main repository README for comparisons.

---

**Made with ❤️ using CrewAI and Groq**

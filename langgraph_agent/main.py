from langgraph_agent.agent_graph import app

# Sample data
cv = """
John Smith
Senior Software Engineer — 6 years experience

Skills: Python, FastAPI, PostgreSQL, Docker, AWS, Redis, LangChain
Education: BSc Computer Science, University of Manchester (2018)

Experience:
- Senior Engineer at TechCorp (2021-present): Built ML pipelines, REST APIs
- Backend Engineer at StartupXYZ (2018-2021): Python microservices, AWS Lambda
"""

jd = """
We are looking for a Senior AI Engineer to join our team.

Must-have:
- 5+ years Python experience
- Experience with LLMs and AI frameworks (LangChain, LlamaIndex, etc.)
- Cloud deployment (AWS or GCP)
- Strong API design skills

Nice-to-have:
- Kubernetes experience
- Vector database experience (Pinecone, Weaviate)
- MLOps background

Role: Build and maintain AI-powered backend systems.
"""

# Initial state — only set the inputs, everything else is None
initial_state = {
    "messages": [],
    "cv_text": cv,
    "job_description": jd,
    "research": None,
    "evaluation": None,
    "report": None
}

# Run the full graph
result = app.invoke(initial_state)

# Access the final report
print(result['report'])

# Access the structured evaluation
print(result['evaluation']['overall_score'])   # e.g. 82
print(result['evaluation']['verdict'])         # e.g. "Strong Yes"
print(result['evaluation']['missing_skills'])  # e.g. ["Kubernetes", "Pinecone"]
import autogen
from agents import extractor, evaluator, reporter, user_proxy
from config import llm_config

# Sample data
cv = """
John Smith — Senior Software Engineer, 6 years experience

Skills: Python, FastAPI, PostgreSQL, Docker, AWS, Redis, LangChain
Education: BSc Computer Science, University of Manchester (2018)

Experience:
- Senior Engineer at TechCorp (2021-present): Built ML pipelines, REST APIs
- Backend Engineer at StartupXYZ (2018-2021): Python microservices, AWS Lambda
"""

jd = """
Senior AI Engineer

Must-have:
- 5+ years Python
- LLM frameworks (LangChain, LlamaIndex)
- Cloud deployment (AWS or GCP)
- Strong API design

Nice-to-have:
- Kubernetes
- Vector databases (Pinecone, Weaviate)
- MLOps

Role: Build and maintain AI-powered backend systems.
"""

# ── GROUP CHAT SETUP ──────────────────────────────────────────────
# Put all agents in a group chat
# The order in agents list is the DEFAULT speaking order
group_chat = autogen.GroupChat(
    agents=[user_proxy, extractor, evaluator, reporter],
    messages=[],           # starts empty — conversation builds here
    max_round=10,          # max back-and-forth rounds before force stop
    speaker_selection_method="auto",  # LLM decides who speaks next
)

# The manager is a special LLM agent that reads the chat
# and decides which agent should speak next
manager = autogen.GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

# ── RUN IT ────────────────────────────────────────────────────────
# UserProxy sends the first message — this kicks off the whole chain
user_proxy.initiate_chat(
    manager,
    message=f"""
    Please review this job application.
    
    CV:
    {cv}
    
    JOB DESCRIPTION:
    {jd}
    
    Extractor — please start by extracting the structured information.
    """
)

# ── ACCESS THE RESULTS ────────────────────────────────────────────
# The full conversation is stored in group_chat.messages
# Each message is a dict: {{"name": "Extractor", "content": "..."}}

print("\n" + "="*60)
print("FULL CONVERSATION HISTORY")
print("="*60)
for msg in group_chat.messages:
    print(f"\n[{msg['name']}]")
    print(msg['content'])

# Get just the final report — last message from Reporter
final_report = next(
    msg['content'] 
    for msg in reversed(group_chat.messages) 
    if msg['name'] == "Reporter"
)
print("\n" + "="*60)
print("FINAL REPORT")
print("="*60)
print(final_report)
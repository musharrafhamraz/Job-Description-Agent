from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from langgraph_agent.agent_state import AgentState
import json
import os

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


# ── NODE 1: Extractor ─────────────────────────────────────────────
def extractor_node(state: AgentState) -> dict:
    """
    Reads the raw CV and job description.
    Extracts structured info from both.
    Writes to: state['research']
    """
    prompt = f"""
    You are a technical recruiter assistant.
    
    Extract structured information from the CV and Job Description below.
    Return a clean summary with these sections:
    
    CANDIDATE:
    - Skills (list all technical skills)
    - Years of experience
    - Education
    - Previous roles
    
    JOB REQUIREMENTS:
    - Must-have skills
    - Nice-to-have skills
    - Required experience (years)
    - Role responsibilities
    
    CV:
    {state['cv_text']}
    
    JOB DESCRIPTION:
    {state['job_description']}
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Return ONLY the fields this node changes
    return {
        "research": response.content,
        "messages": state['messages'] + [
            AIMessage(content=response.content, name="extractor")
        ]
    }


# ── NODE 2: Evaluator ─────────────────────────────────────────────
def evaluator_node(state: AgentState) -> dict:
    """
    Reads the extracted research.
    Scores the candidate, finds gaps and strengths.
    Writes to: state['evaluation']
    """
    prompt = f"""
    You are a senior technical hiring manager.
    
    Based on the extracted information below, evaluate the candidate.
    
    Return your evaluation as valid JSON with this exact structure:
    {{
        "overall_score": <0-100 integer>,
        "verdict": "<Strong Yes | Yes | Maybe | No>",
        "matched_skills": ["skill1", "skill2"],
        "missing_skills": ["skill1", "skill2"],
        "strengths": ["strength1", "strength2"],
        "red_flags": ["flag1"] or [],
        "experience_match": "<Overqualified | Good Match | Underqualified>",
        "interview_topics": ["topic1", "topic2", "topic3"]
    }}
    
    Return ONLY valid JSON, no extra text.
    
    EXTRACTED INFORMATION:
    {state['research']}
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Parse the JSON response
    evaluation_data = json.loads(response.content)
    
    return {
        "evaluation": evaluation_data,
        "messages": state['messages'] + [
            AIMessage(content=response.content, name="evaluator")
        ]
    }


# ── NODE 3: Reporter ──────────────────────────────────────────────
def reporter_node(state: AgentState) -> dict:
    """
    Reads both research and evaluation.
    Writes the final human-readable hiring report.
    Writes to: state['report']
    """
    eval_data = state['evaluation']
    
    prompt = f"""
    You are a professional hiring report writer.
    
    Write a clear, structured hiring recommendation report based on:
    
    EXTRACTED DATA:
    {state['research']}
    
    EVALUATION SCORES:
    {json.dumps(eval_data, indent=2)}
    
    The report must include:
    1. Executive Summary (2-3 sentences, verdict upfront)
    2. Skill Match Analysis
    3. Key Strengths
    4. Concerns / Gaps
    5. Suggested Interview Questions (from evaluation)
    6. Final Recommendation
    
    Write professionally. Be direct and specific.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "report": response.content,
        "messages": state['messages'] + [
            AIMessage(content=response.content, name="reporter")
        ]
    }
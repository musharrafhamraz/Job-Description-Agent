from typing import TypedDict, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

class AgentState(TypedDict):
    # Full conversation history — every agent appends to this
    messages: list[BaseMessage]
    
    # The raw inputs — set once at the start, never changed
    cv_text: str
    job_description: str
    
    # Each agent writes to its own field
    research: Optional[str]       # Extractor fills this
    evaluation: Optional[dict]    # Evaluator fills this
    report: Optional[str]         # Reporter fills this
from langgraph.graph import END
from langgraph_agent.agent_state import AgentState

# Route based on score — skip reporter if score is too low
def should_continue(state: AgentState) -> str:
    score = state['evaluation']['overall_score']
    
    if score < 40:
        return "reject"   # go to a rejection node
    else:
        return "report"   # go to reporter normally

# Add a rejection node
def rejection_node(state: AgentState) -> dict:
    return {
        "report": f"Candidate does not meet minimum requirements. Score: {state['evaluation']['overall_score']}/100"
    }

def setup_conditional_routing(graph_builder):
    """
    Setup conditional routing for the agent graph.
    Call this function after creating the basic graph structure.
    """
    graph_builder.add_node("rejection", rejection_node)
    
    # Replace the fixed edge with a conditional one
    graph_builder.add_conditional_edges(
        "evaluator",              # from this node
        should_continue,          # call this function to decide
        {
            "report": "reporter", # if returns "report" → go to reporter
            "reject": "rejection" # if returns "reject" → go to rejection
        }
    )
    
    graph_builder.add_edge("rejection", END)
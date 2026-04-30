from langgraph.graph import StateGraph, END
from langgraph_agent.agent_state import AgentState
from langgraph_agent.nodes import extractor_node, evaluator_node, reporter_node

# 1. Create the graph with our state type
graph_builder = StateGraph(AgentState)

# 2. Add nodes — each node is a function
graph_builder.add_node("extractor", extractor_node)
graph_builder.add_node("evaluator", evaluator_node)
graph_builder.add_node("reporter", reporter_node)

# 3. Define edges — the flow between nodes
graph_builder.set_entry_point("extractor")        # where execution starts
graph_builder.add_edge("extractor", "evaluator")  # extractor → evaluator
graph_builder.add_edge("evaluator", "reporter")   # evaluator → reporter
graph_builder.add_edge("reporter", END)           # reporter → done

# 4. Compile into a runnable
app = graph_builder.compile()
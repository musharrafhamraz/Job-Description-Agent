# LLM configuration — AutoGen uses this dict format
llm_config = {
    "config_list": [
        {
            "model": "gpt-4o",
            "api_key": "your-openai-key-here",  
            # or use: os.environ["OPENAI_API_KEY"]
        }
    ],
    "temperature": 0,
}
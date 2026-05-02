#!/usr/bin/env python
import sys
import warnings

from agent_crewai.crew import AgentCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Sample CV and Job Description (same as LangGraph implementation)
SAMPLE_CV = """
John Smith
Senior Software Engineer — 6 years experience

Skills: Python, FastAPI, PostgreSQL, Docker, AWS, Redis, LangChain
Education: BSc Computer Science, University of Manchester (2018)

Experience:
- Senior Engineer at TechCorp (2021-present): Built ML pipelines, REST APIs
- Backend Engineer at StartupXYZ (2018-2021): Python microservices, AWS Lambda
"""

SAMPLE_JD = """
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

def run():
    """
    Run the CV screening crew with sample data.
    """
    inputs = {
        'cv_text': SAMPLE_CV,
        'job_description': SAMPLE_JD
    }

    try:
        result = AgentCrewai().crew().kickoff(inputs=inputs)
        
        print("\n" + "="*80)
        print("CV SCREENING COMPLETE")
        print("="*80)
        
        # Access the evaluation scores
        if hasattr(result, 'pydantic'):
            evaluation = result.pydantic
            print(f"\n📊 Overall Score: {evaluation.overall_score}/100")
            print(f"✅ Verdict: {evaluation.verdict}")
            print(f"\n🎯 Matched Skills: {', '.join(evaluation.matched_skills)}")
            print(f"❌ Missing Skills: {', '.join(evaluation.missing_skills)}")
            print(f"\n💪 Key Strengths:")
            for strength in evaluation.strengths:
                print(f"   - {strength}")
            
            if evaluation.red_flags:
                print(f"\n⚠️  Red Flags:")
                for flag in evaluation.red_flags:
                    print(f"   - {flag}")
            
            print(f"\n📈 Experience Match: {evaluation.experience_match}")
            print(f"\n💬 Interview Topics:")
            for topic in evaluation.interview_topics:
                print(f"   - {topic}")
        
        print("\n" + "="*80)
        print("📄 Full report saved to: hiring_report.md")
        print("="*80 + "\n")
        
        return result
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def run_custom(cv_text: str, job_description: str):
    """
    Run the crew with custom CV and job description.
    
    Args:
        cv_text: The candidate's CV text
        job_description: The job description text
    
    Returns:
        The crew execution result
    """
    inputs = {
        'cv_text': cv_text,
        'job_description': job_description
    }

    try:
        result = AgentCrewai().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'cv_text': SAMPLE_CV,
        'job_description': SAMPLE_JD
    }
    try:
        AgentCrewai().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgentCrewai().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'cv_text': SAMPLE_CV,
        'job_description': SAMPLE_JD
    }

    try:
        AgentCrewai().crew().test(
            n_iterations=int(sys.argv[1]), 
            eval_llm=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

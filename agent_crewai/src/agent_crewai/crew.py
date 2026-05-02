from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field

# Define structured output for evaluation
class CandidateEvaluation(BaseModel):
    """Structured evaluation of a candidate"""
    overall_score: int = Field(..., description="Score from 0-100")
    verdict: str = Field(..., description="Strong Yes, Yes, Maybe, or No")
    matched_skills: List[str] = Field(..., description="Skills that match job requirements")
    missing_skills: List[str] = Field(..., description="Required skills the candidate lacks")
    strengths: List[str] = Field(..., description="Key strengths of the candidate")
    red_flags: List[str] = Field(default_factory=list, description="Any concerns or red flags")
    experience_match: str = Field(..., description="Overqualified, Good Match, or Underqualified")
    interview_topics: List[str] = Field(..., description="Suggested interview questions/topics")

@CrewBase
class AgentCrewai():
    """CV Screening Agent Crew - Multi-agent system for automated candidate evaluation"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def extractor_agent(self) -> Agent:
        """Agent responsible for extracting structured information from CV and job description"""
        return Agent(
            config=self.agents_config['extractor_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def evaluator_agent(self) -> Agent:
        """Agent responsible for scoring and evaluating candidate fit"""
        return Agent(
            config=self.agents_config['evaluator_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reporter_agent(self) -> Agent:
        """Agent responsible for generating final hiring recommendation report"""
        return Agent(
            config=self.agents_config['reporter_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def extraction_task(self) -> Task:
        """Task to extract structured information from CV and job description"""
        return Task(
            config=self.tasks_config['extraction_task'], # type: ignore[index]
        )

    @task
    def evaluation_task(self) -> Task:
        """Task to evaluate candidate and generate structured scores"""
        return Task(
            config=self.tasks_config['evaluation_task'], # type: ignore[index]
            output_pydantic=CandidateEvaluation
        )

    @task
    def reporting_task(self) -> Task:
        """Task to generate final hiring recommendation report"""
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='hiring_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CV Screening crew with sequential process"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

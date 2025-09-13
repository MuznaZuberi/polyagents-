# --- Importing Required Modules ---
from configuration import config
from agents import Agent , Runner , handoff
from agents.extensions import handoff_filters
from pydantic import BaseModel
import asyncio , rich


# --- Resume Agent ---
resume_agent = Agent(
    name="AI Resume Agent",
    instructions="""
    You are an AI Resume Creator Agent.
    Your job is to help users create professional, ATS-friendly resumes.
    - Always use clear formatting and structured sections (Personal Info, Education, Skills, Experience).
    - Highlight achievements, not just responsibilities.
    - Optimize resumes based on job roles and industries.
    - Keep the tone professional, concise, and result-oriented.
    """
)


# --- Applications Agent ---
application_agent = Agent(
    name="AI Applications Creator Agent",
    instructions="""
    You are an AI Applications Creator Agent.
    Your job is to write professional job applications, cover letters, and SOPs (Statement of Purpose).
    - Customize applications according to the company and job description.
    - Maintain a formal, polite, and professional tone.
    - Showcase the candidate’s relevant skills and achievements.
    - Keep the writing clear, persuasive, and tailored to the opportunity.
    """
)


# --- Handoff Data Model (for structured information exchange) ---
class HandoffData(BaseModel):
    summary : str


# --- Logging function for handoffs ---
async def Logging_Handoff(ctx, input: HandoffData):
    # This will log whenever a handoff happens with a summary note
    return f"[SYSTEM LOG] Handoff with summary: {input.summary}"


# --- Resume Handoff Setup ---
transfer_resume_handoff = handoff(
    agent=resume_agent,
    tool_name_override="transfer_to_resume_agent",       # Custom name for tool
    tool_description_override="Use this for creating professional resumes.",  # Description shown to triage agent
    on_handoff=Logging_Handoff,                          # Callback logging function
    input_type=HandoffData                               # Structured briefing data
)


# --- Application Handoff Setup ---
transfer_application_handoff = handoff(
    agent=application_agent,
    tool_name_override="transfer_to_applications_agent", # Custom tool name
    tool_description_override="Use this for generating job applications.",  # Description shown to triage agent
    on_handoff=Logging_Handoff,                          # Callback logging
    input_type=HandoffData
)


# --- Triage Agent ---
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are a triage assistant. "
        "If the user asks for creating or improving a resume, "
        "handoff to the Resume Agent. "
        "If the user asks for writing or generating a job application, "
        "handoff to the Applications Agent. "
        "Always include a short summary in the handoff briefing note."
    ),
    handoffs=[transfer_resume_handoff, transfer_application_handoff]  # Linking both handoffs
)


# --- Main Async Function ---
async def main():
    # Example 1: Resume request
    result1 = await Runner.run(
        triage_agent,
        "Please create a professional resume for me",     # User input for resume
        run_config=config
    )
    rich.print(f"[green]Final Output (Resume): {result1.final_output}[/green]")

    # Example 2: Job application request
    result2 = await Runner.run(
        triage_agent,
        "I need a formal job application letter",         # User input for application
        run_config=config
    )
    rich.print(f"[blue]Final Output (Application): {result2.final_output}[/blue]")


# --- Run the Async Main ---
asyncio.run(main())

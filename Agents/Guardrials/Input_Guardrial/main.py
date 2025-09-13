from configuration import config
from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
import asyncio
import rich
from pydantic import BaseModel


class UserOutput(BaseModel):
    user_name: str
    user_email: str
    is_valid_data: bool
    response: str


# ✅ Allowed office employees list
ALLOWED_EMPLOYEES = [
    {"user_name": "Muzna Amir", "user_email": "muznazuberi123@gmail.com"},
    {"user_name": "Ali Khan", "user_email": "ali.khan@company.com"},
    {"user_name": "Sara Ahmed", "user_email": "sara.ahmed@company.com"}
]


# Office Security Agent
office_security_agent = Agent(
    name="Office_Security_Agent",
    instructions="""You are an office security agent. 
    Your job is to validate whether the employee is authorized to access the office.
    If the provided user_name and user_email match with allowed employees, grant access.
    Otherwise, deny access.""",
    output_type=UserOutput
)


# Guardrail for input validation
@input_guardrail
async def office_guardrail(ctx, agent, input):
    response = await Runner.run(office_security_agent, input, run_config=config)
    rich.print(response.final_output)

    # Check if employee is in allowed list
    for emp in ALLOWED_EMPLOYEES:
        if (
            response.final_output.user_name == emp["user_name"]
            and response.final_output.user_email == emp["user_email"]
        ):
            return GuardrailFunctionOutput(
                output_info="✅ Access Granted",
                tripwire_triggered=False
            )

    # ❌ Not authorized
    return GuardrailFunctionOutput(
        output_info="❌ Unauthorized Employee - Access Denied",
        tripwire_triggered=True
    )


# Main Office Agent with Guardrail
main_agent = Agent(
    name="Main_Office_Agent",
    instructions="You are the office check-in system.",
    input_guardrails=[office_guardrail]
)


# Run the program
async def main():
    try:
        result = await Runner.run(
            main_agent,
            "Employee: Muzna Amir, Email: muznazuberi123@gmail.com",
            run_config=config
        )
        print(f"Final_output : {result.final_output}")

    except InputGuardrailTripwireTriggered:
        print("❌ Employee not allowed inside office.")


asyncio.run(main())

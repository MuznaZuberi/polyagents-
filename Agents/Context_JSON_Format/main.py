from configuration import config
from agents import Agent, Runner, RunContextWrapper, function_tool
from pydantic import BaseModel
import asyncio


class UserInfo(BaseModel):
    user_name: str
    user_email: str
    gender: str
    nationality: str
    current_location: str


@function_tool
def access_user_data(wrapper: RunContextWrapper[UserInfo]) -> dict:
    return {
        "user_name": wrapper.context.user_name,
        "user_email": wrapper.context.user_email,
        "current_location": wrapper.context.current_location
    }


agent = Agent(
    name="AI Agent",
    instructions=(
        "You are a helpful AI Agent. "
        "When I ask about user_name, user_email or current_location, get it from the tool. "
        "When I ask about UserInfo, return all fields in JSON format."
    ),
    tools=[access_user_data]
)


user_information = UserInfo(
    user_name="Muzna Amir",
    user_email="muzi@gmail.com",
    gender="Female",
    nationality="Pakistani",
    current_location="Karachi"
)


async def main():
    prompt = "Tell me about UserInfo"
    response = await Runner.run(
        agent,
        prompt,
        context=user_information,
        run_config=config
    )
    print(response.final_output)


asyncio.run(main())

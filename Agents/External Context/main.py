import os
from configuration import config
from agents import Agent, Runner, function_tool, RunContextWrapper
import asyncio
from dataclasses import dataclass




# 👤 Define the context data structure (user info)
@dataclass
class User_info:
    user_name: str
    user_age: int
    user_id: int
    user_email: str




# 🛠️ Define a function tool that accesses user context
@function_tool
def access_user_data(wrapper: RunContextWrapper[User_info]) -> str:
    return f"Username: {wrapper.context.user_name}. User email: {wrapper.context.user_email}."





# 🚀 Async main function to run the agent
async def main():
    # 🧑‍💻 Create a user context instance
    get_info = User_info(
        user_name="Zaviyar Ali Khan",
        user_age=29,
        user_id=177717,
        user_email="zavi_22@gmail.com"
    )



    # 🤖 Define the agent with instructions and tools
    agent = Agent[User_info](
        name="AI Agent",
        instructions="You are a helpful assistant that introduces the user using the provided context (name and email).",
        tools=[access_user_data]
    )



    # 💬 Prompt to be processed by the agent
    prompt = "What is the username and useremail?"



    # 🏃 Run the agent with context and prompt
    res = await Runner.run(
        agent,
        prompt,
        context=get_info,
        run_config=config
    )
    # 🖨️ Display final output
    print(res.final_output)




# 🔁 Trigger the async main function
if __name__ == "__main__":
    asyncio.run(main())

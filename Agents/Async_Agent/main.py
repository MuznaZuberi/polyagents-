# Importing necessary configurations and classes
from configuration import config  # Configuration settings (e.g., API keys, tools)
from agents import Agent, Runner  # Agent and Runner classes from the SDK
import asyncio  # For running asynchronous functions




# Creating an instance of an Agent with a name and a set of instructions
async_agent = Agent(
    name="AI Agent",
    instructions="You are a helpful AI agent"  # Agent behavior guidance
)




# Asking the user for input
prompt = input("Ask question: ")



# Defining the asynchronous main function
async def main():
    # Running the agent with the given prompt and config
    result = await Runner.run(
        async_agent,    # The AI agent instance
        prompt,         # User's input
        run_config=config  # Configuration for execution (e.g., tools, context, memory)
    )   
    # Printing the final output returned by the agent
    print(result.final_output)




# Entry point of the script
if __name__ == "__main__":
    asyncio.run(main())  # Runs the async main function

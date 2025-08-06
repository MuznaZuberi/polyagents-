from configuration import config  # Import configuration settings for the agent
from agents import Agent, Runner  # Import Agent and Runner classes




agent = Agent(
    name = "Assistant",  # Create an agent named "Assistant"
    instructions = "You are a helpful AI assistant."  # Set instructions for the agent
)



prompt = input("Ask any question: ")  # Take user input as a question prompt



response = Runner.run_sync(
    agent,  # Pass the agent to run
    prompt,  # User's input query
    run_config = config  # Use imported configuration settings
)
print(response.final_output)  # Print the final output from the agent

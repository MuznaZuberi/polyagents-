from configuration import config  # Import configuration settings for running the agent

from agents import Agent, Runner  # Import Agent and Runner classes

translate_agent = Agent(  
    name = "AI Translator",  # Create an agent named "AI Translator"
    instructions = "Translate any input text into Urdu only. Do not explain, just return the translated text."
)

prompt = input("Enter text to translate into Urdu: ")  # Take user input for the text to be translated into Urdu

response = Runner.run_sync(
    translate_agent,  # Pass the translator agent to the runner
    prompt,  # Provide the user's input to the agent
    run_config = config  # Use the imported configuration settings
)

print(response.final_output)  # Print the final translated output from the agent

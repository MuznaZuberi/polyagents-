from configuration import config  # Import configuration
from agents import Agent, Runner, function_tool  # Import Agent, Runner, and function_tool





# Tool: Single input → Full info return
@function_tool
def country_info(c_name: str) -> str:
    c = c_name.lower()

    if c == "pakistan":
        return "You selected Pakistan – land of the pure. Famous place: Badshahi Mosque, Lahore. Famous dish: Biryani."

    elif c == "turkey":
        return "You selected Turkey – where East meets West. Famous place: Hagia Sophia, Istanbul. Famous dish: Kebabs."

    elif c == "italy":
        return "You selected Italy – the heart of the Roman Empire. Famous place: Colosseum, Rome. Famous dish: Pizza."

    elif c == "japan":
        return "You selected Japan – land of the rising sun. Famous place: Mount Fuji. Famous dish: Sushi."

    elif c == "france":
        return "You selected France – country of love and fashion. Famous place: Eiffel Tower, Paris. Famous dish: Croissant."

    else:
        return "Sorry! Information for the selected country is not available."





# Create Agent
agent = Agent(
    name="Agent",
    instructions="You are a country knowledge assistant. You help users with information about countries, their famous places, and popular dishes.",
    tools=[country_info]
)




# Get User Input
prompt = input("Enter country name: ")




# Run the Agent
response = Runner.run_sync(
    agent,
    prompt,
    run_config=config
)
# Show Result
print(response.final_output)

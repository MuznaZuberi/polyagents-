from configuration import config  # Import configuration settings for running the agent
from agents import Agent, Runner  # Import Agent and Runner classes from your agent system






# 🍳 Cooking Advisor Agent
cooking_agent = Agent(
    name="Cooking Advisor",  # Name of the agent
    instructions="You are a cooking expert. Answer only cooking-related questions. Provide recipes, tips, or food suggestions. Ignore unrelated topics."  # Agent instructions
)




# 👗 Fashion Stylist Agent
fashion_agent = Agent(
    name="Fashion Stylist",  # Name of the agent
    instructions="You are a fashion stylist. Help users with outfit suggestions, color matching, and fashion trends. Answer only fashion-related queries."  # Agent instructions
)





# 🩺 Health Advisor Agent
health_agent = Agent(
    name="Health Advisor",  # Name of the agent
    instructions="You are a professional health advisor. Give advice on general health, fitness, diet, and mental wellness. Do not answer non-health-related queries."  # Agent instructions
)





# 📅 Appointment Scheduler Agent
appointment_agent = Agent(
    name="Appointment Scheduler",  # Name of the agent
    instructions="You are an appointment assistant. Help users book meetings, appointments, or set reminders. Do not answer other types of questions."  # Agent instructions
)




# 🤖 Triage Agent to route the query to the correct agent
triage_agent = Agent(
    name="Triage Agent",  # Name of the triage (router) agent
    instructions="You're a triage agent. Based on the user's question, decide whether it's about cooking, fashion, health, or appointments, and hand off to the right agent.",  # Short triage instructions
    handoffs=[cooking_agent, fashion_agent, health_agent, appointment_agent]  # List of sub-agents to hand off to
)




# 💬 Take user's question as input
prompt = input("Ask your question (e.g., What should I cook for dinner?): ")  # Get user input





# 🚀 Run the triage agent with user input
response = Runner.run_sync(
    triage_agent,  # The main agent that will decide routing
    prompt,        # The user's question
    run_config=config  # Configuration settings
)
# 📢 Display the final response to the user
print(response.final_output)  # Print the selected agent's answer

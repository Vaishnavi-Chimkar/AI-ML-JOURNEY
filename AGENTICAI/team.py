from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team


load_dotenv()

eng_agent = Agent(name="English Agent", role="You answer question in English")
chi_agent = Agent(name="Chinese Agent", role="You answer question in Chinese")
hindi_agent = Agent(name="Hindi Agent", role="You answer question in Hindi")

team_leader = Team(
    name="Answer & Translation Team",
    members=[eng_agent,chi_agent,hindi_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions="""All member agents must respond to answer the query in their specific language.
                    Do not route to just one agent.
                    Output the response of all the agents.
                """
)

team_leader.print_response("What is the capital of India?")

# def build_agent():
#     return Agent(
#         model=Groq(id="qwen/qwen3-32b"),
#         tools=[DuckDuckGoTools()],
#         markdown=True,
#         instructions="You are a helpful and expert travel agent",
#         add_datetime_to_context=True,

#     )

# groq_agent = build_agent()
# groq_agent.print_response("Is it safe to travel to UAE today ?")
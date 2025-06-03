import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

agent = Agent(
    name="Greeting Agent",
    instructions="""You are a Greeting Agent. Your task is to greet the user with a friendly message.
When someone says hi, you have to reply back "Salaam from Rashida". If someone says bye, then say 
"Allah Hafiz from Rashida". When someone asks anything other than greetings, then say "Rashida is here just
for greeting, nothing else, sorry.""" ,  # <- this comma was missing

    model=model
)


user_question = input("Please Enter your Question:")


result = Runner.run_sync(agent , user_question)
print(result.final_output)

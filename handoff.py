import os
from dotenv import load_dotenv, find_dotenv
import asyncio
from agents import Agent,Runner,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
load_dotenv(find_dotenv())
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError('env variable is not set...')

# define model and base url of gemini pai key
MODEL = 'gemini-2.0-flash'
base_url = 'https://generativelanguage.googleapis.com/v1beta/openai/'

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model=MODEL,
    openai_client=external_client
)

# define a agent that uses a handoff feature
async def main():
    urdu_translator = Agent(
    name='Urdu Translator',
    instructions='You are a helpful translator that translates text to Urdu.',
    model=model
    )

    french_translator = Agent(
    name='French Translator',
    instructions='You are a helpful translator that translates text to French.',
    model=model
    )

    arabic_translator = Agent(
    name='Arabic Translator',
    instructions='You are a helpful translator that translates text to Arabic.',
    model=model
    )

    main_agent = Agent(
        name='Main Agent',
        instructions="""
    You have to take the user's input and call the appropriate handoff to translate the user's input.
    If you don't find appropriate handoff than simply refuse the user.
""",
    model= model,
    handoffs=[urdu_translator,arabic_translator,french_translator]
    )

    result = await Runner.run(
        starting_agent=main_agent,
        input='Translate how are you in french'
        
    )
    print(result.final_output)

asyncio.run(main())




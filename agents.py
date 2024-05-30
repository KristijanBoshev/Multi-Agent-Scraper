from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-3.5-turbo"
 
youtube_researcher = Agent(
    role="Researcher for YouTube videos",
    goal="Get the relevant video transcription for the topic {topic} from the provided YouTube channels",
    verbose=True,
    memory=True,
    backstory=(
         "Expert and listener of English Songs from famous artists" 
        
    ),
    tools=[yt_tool],
    allow_delegation=True

)

blog_writer = Agent(
    role="Blog Writer",
    goal="Write a blog post about the topic {topic} from the provided YouTube channels",
    verbose=True,
    memory=True,
    backstory=(
        "With a keen eye for detail and a passion for storytelling, journey began in the bustling corridors of a renowned university, where earned a degree in Journalism and Communications."

    ),
    tools=[yt_tool],
    allow_delegation=False

) 
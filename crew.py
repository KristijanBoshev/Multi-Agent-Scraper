from crewai import Crew,Process
from agents import youtube_researcher, blog_writer
from tasks import research_task,write_task

crew = Crew(
  agents=[youtube_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential, 
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result=crew.kickoff(inputs={'topic':'Halo'})
print(result)
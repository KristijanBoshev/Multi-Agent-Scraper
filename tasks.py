from crewai import Task
from tools import yt_tool 
from agents import blog_writer,youtube_researcher

research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
    "It should capture all the necessary lyrics"
  ),
  expected_output='A comprehensive 10 paragraph detailed report based on the lyrics{topic} of video content, without including the technical part.',
  tools=[yt_tool],
  agent=youtube_researcher
)

write_task = Task(
  description=(
    "Get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md' 
)
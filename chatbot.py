
# Import Libraries and Set the OpenAI key
import os
import key

os.environ["OPENAI_API_KEY"] = key.OPENAI_API_KEY
from embedchain import App

chat_bot = App()

# Embed Online Resources
chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
chat_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
chat_bot.add("web_page", "https://nav.al/feedback")
chat_bot.add("web_page", "https://nav.al/agi")

# Embed Local Resources
chat_bot.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor."))

chat_bot.add('youtube_video', 'a_valid_youtube_url_here')
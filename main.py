import requests
from dotenv import load_dotenv
load_dotenv()
import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

while True:

    Blogpost_title = input("Please give me a blog post title: ")
    if Blogpost_title =="exit":
        break
    Blogpost_tonality= input("Please give me a blog post tonality: ")
    
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt="write an esay about"+Blogpost_title+"with a"+Blogpost_tonality+"tonality in 120 to 150 characters",
                                        max_tokens=2048 )
    print(response.choices[0].text)
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
with open('FeedMe.json', 'r') as myfile:
    data=myfile.read()

Toask=json.loads(data)
holding=[]
with open('Responses.json', 'w') as responses:
    for question in Toask["Data"]:

        Blogpost_title = question["title"]
        Blogpost_tonality= question["tonality"]
        
        response = openai.Completion.create(engine="text-davinci-003",
                                            prompt="write an esay about"+Blogpost_title+"with a"+Blogpost_tonality+"tonality in 120 to 150 characters",
                                            max_tokens=2048 )
        print(response.choices[0].text)
        temp={
            "title": Blogpost_title,
            "tonality" : Blogpost_tonality,
            "response" : response.choices[0].text
        }
        holding.append(temp)
    json.dump(holding,responses,indent=4)
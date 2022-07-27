import os
import openai
from dotenv import load_dotenv

load_dotenv()

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def GPT_Completion(texts):
    ## Call the API key under your account (in a secure way)

    openai.api_key = os.environ['OPENAI_API_SECRET_KEY']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt =  texts,
        temperature = 0.6,
        top_p = 1,
        max_tokens = 1000,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    return print(response.choices[0].text)

prompt = ''' 

Write blog sections
Blog Topic: Commuincations Plan for NonProfitss
Blog Section: Every good story has an obvious story question to keep people engaged
'''
GPT_Completion(prompt)
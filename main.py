import os
import openai
import config 


openai.api_key = config.API_KEY
while True:
    ask=input("Abdo : ")
    if(ask=="exit"):
        exit()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    text=response['choices'][0]['text']
    print("ChatGPT : "+text)
    # print("ChatGPT : "+response)
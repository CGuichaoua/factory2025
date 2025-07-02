import os
from sys import api_version
from openai import AzureOpenAI

def main():
    azure_client=create_azure_client()
    response = azure_client.chat.completions.create(
        model=os.environ['MODEL'],  # this is the Azure "deployment name"
        messages=[
            {"role": "system", "content": "You are a helpful assistant, here to help us brainstorm in Haguenau for the GenCity hackathon."},
            {"role": "user", "content": "Give me a cool idea to use generative AI in cities. Include some simple steps to start prototyping. Keep it simple so that it is possible to achieve a minimal version in 3 hours."}
        ]
    )   
    print(response.choices[0].message.content)
    

def create_azure_client():
    return AzureOpenAI(
        api_key=os.environ["API_KEY"],
        azure_endpoint=os.environ["ENDPOINT"],
        api_version="2024-10-21"
    )


if __name__ == "__main__":
    main()

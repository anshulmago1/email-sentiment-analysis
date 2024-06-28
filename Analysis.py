import openai

openai.api_key = "your-api-key-here" #change it to whatever api key u have

def analyze_sentiment(text):

    prompt=f"Analyze the sentiment of the following text and return the result as Angry, Happy, Sad:\n\n{text}\n\nSentiment:"

    response = openai.Completion.create(
        model="gpt-3.5-turbo", # changed the model because this one is cheaper per token
        messages=[{"role": "user", "content": prompt}],
        temperature=0, # changed it to 0 to make the outputs less random
        max_tokens = 10 # i just set it to 10 for no we can change it later
    )

    sentiment = response.choices[0].message['content'].strip()
    return sentiment

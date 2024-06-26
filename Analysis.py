import openai

openai.api_key = "your-api-key-here" #change it to whatever api key u have

def analyze_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text and return the result as Angry, Happy, Sad:\n\n{text}\n\nSentiment:",
        temperature=0.5
        max_tokens = 10 # i just set it to 10 for no we can change it later
    )

    sentiment = response.choices[0].text.strip()
    return sentiment

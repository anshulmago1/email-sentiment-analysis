import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") #change it to whatever api key u have

def analyze_sentiment(text):

    msgs = [
        {"role": "system", "content": "You are a sentiment analysis tool."},
        {"role": "user", "content": f"Analyze the sentiment of the following text and return the result as Positive, Negative, or Neutral:\n\n{text}\n\nSentiment:"}
    ]

    response = openai.Completion.create(
        model="gpt-3.5-turbo", # changed the model because this one is cheaper per token
        messages=msgs,
        temperature=0, # changed it to 0 to make the outputs less random
        max_tokens = 10 # i just set it to 10 for no we can change it later
    )

    sentiment = response.choices[0].message['content'].strip()
    return sentiment

if __name__ == "__main__":
    # loop through each email in text file and output sentiment by calling the above function
    with open("content.txt", "r") as f:
        for line in f:
            if "Content:" in line:
                nextLine = f.readline().strip()
                sentiment = analyze_sentiment(nextLine)
                print("Sentiment: " + sentiment)
                

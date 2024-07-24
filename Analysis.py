import openai

openai.api_key = "sk-None-owpUdxtcdb58wMtmeT1iT3BlbkFJFNwhP61z0TGL31Brh3lA"

def analyze_sentiment(text):

    msgs = [
        {"role": "system", "content": "You are a sentiment analysis tool."},
        {"role": "user", "content": f"Analyze the sentiment of the following text and return the result as Positive, Negative, or Neutral:\n\n{text}\n\nSentiment:"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # changed the model because this one is cheaper per token
        messages=msgs,
        temperature=0, # changed it to 0 to make the outputs less random
        max_tokens = 10 # i just set it to 10 for no we can change it later
    )

    sentiment = response.choices[0].message['content'].strip()
    return sentiment

if __name__ == "__main__":
    # loop through each email in text file and output sentiment by calling the above function
    with open("content.txt", "r") as file:

        emails = []
        email = []
        empty_line_count = 0

        for line in file:
            if line.strip() == '':
                empty_line_count += 1
            else:
                empty_line_count = 0

            if empty_line_count == 2:
                if email:
                    emails.append(email)
                    email = []
                empty_line_count = 0
            else:
                if line.strip() != '':
                    email.append(line.strip())
    
        if email:
            emails.append(email)

    with open("sentiment.txt", "a") as file:
        for email in emails:
            sentiment = analyze_sentiment(email)
            file.write(f"Sentiment: " + sentiment + "\n")
            
    
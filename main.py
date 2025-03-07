import openai

# تعيين مفتاح API الخاص بك
openai.api_key = 'YOUR_API_KEY'

def summarize_text(text, max_words=150):
    prompt = f"Summarize the following text in {max_words} words:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("📝 Text Summarizer")
    user_text = input("Enter the text you want to summarize: \n")
    
    summary = summarize_text(user_text)
    print("\n📌 Summary:\n", summary)
 

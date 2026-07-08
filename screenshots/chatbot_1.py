import ollama

with open("transcript.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

print("=" * 50)
print("Smartbridge Salesforce AI Assistant")
print("=" * 50)

while True:

    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() == "exit":
        break

    prompt = f"""
You are a Smartbridge Salesforce AI Assistant.

Answer ONLY using the transcript below.

If the answer is not found in the transcript, say:
'I could not find that information in the transcript.'

Transcript:
{transcript}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\nAnswer:")
    print(response["message"]["content"])
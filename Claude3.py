import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.2,
    system="You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
    messages=[
        {"role": "user", "content": "Nature reserves in current view with a note matching the regular expression \"Schild\" from 2016-07-01 12:00:00. --> Chinese"}
    ]
)
print(message.content)
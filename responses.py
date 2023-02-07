import openai


def handle_response(message) -> str:
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response.choices[0].text
    return text

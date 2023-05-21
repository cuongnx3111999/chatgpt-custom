import openai

openai.api_key = "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"

messages=[]
def get_response_from_chatgpt(messages):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    return response['choices'][0]['message']['content']

def main():
    messages.append({"role": "user", "content": "adpater pattern là gì ."}, )
    response_text = get_response_from_chatgpt(messages)
    messages.append({"role": "assistant", "content": response_text}, )
    print(messages)

    messages.append({"role": "user", "content": "lấy ví dụ"}, )
    response_text = get_response_from_chatgpt(messages)
    messages.append({"role": "assistant", "content": response_text}, )
    print(messages)

if __name__ == '__main__':
    main()
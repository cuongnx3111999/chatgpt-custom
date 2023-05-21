import streamlit as st
import openai

st.title("Tích hợp ChatGPT vào ứng dụng Python")

# Cài đặt thông tin model
model = "gpt-3.5-turbo"#"text-davinci-003"
openai.api_key = "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"
messages = []

# Hàm để gọi đến OpenAPI / Phần ChatGPT
def get_response_from_chatgpt(messages):
    response = openai.ChatCompletion.create(
        model= model,
        # prompt = user_question,
        max_tokens = 2000,
        messages=messages,
        temperature = 0.5
    )

    response_text = response['choices'][0]['message']['content']
    return response_text


# Điều khiển giao diện
def main():
    st.button("Chat với tôi")

    user_question = st.text_input("Nhập câu hỏi vào đây:")
    if st.button("Chat với tôi"):
        messages.append({"role": "user", "content": user_question},)
        response_text = get_response_from_chatgpt(messages)
        messages.append({"role": "assistant", "content": response_text},)

        st.write(messages)

    return st.write(messages)

main()
import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a therapist that specializes in psychology"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital therapist")

demo.launch(share=True)
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

def main():
    """main function"""
    st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    )

    st.write("# Welcome to my Chatbot! 🤖")


    with st.sidebar:
        st.title('Login HugChat')
        hf_email = st.text_input('Enter E-mail:')
        hf_pass = st.text_input('Enter Password:', type='password')
        if not (hf_email and hf_pass):
            st.warning('Please enter your account!')
        else:
            st.success('Proceed to entering your prompt message!')
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response(prompt, hf_email, hf_pass)
                    st.write(response)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)
    print(st.session_state)
if __name__ == "__main__":
    main()
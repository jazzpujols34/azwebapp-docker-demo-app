import streamlit as st

st.title("IDK! 🤷‍♂️")

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

def chat_with_user():
	st.session_state.messages.append({"role": "user", "content": st.session_state.prompt})
	st.session_state.messages.append({"role": "assistant", "content": "I don't know 😵"})

prompt = st.chat_input("Ask me anything", on_submit=chat_with_user, key='prompt')
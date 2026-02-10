from dotenv import load_dotenv 
import streamlit as st
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model = "meta-llama/llama-4-scout-17b-16e-instruct"
)
st.title("👳‍♂️ AskMe: Your Personal QnA Assistant")
st.markdown("Welcome to AskMe! This is your personal QnA assistant powered by Groq. let's get started! 😊")

query = st.chat_input("ask anything...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    llm_response = llm.invoke(query).content
    st.chat_message("assistant").markdown(llm_response)
    st.session_state.messages.append({"role": "assistant", "content": llm_response})

# while True:
#     query = st.text_input("User: ")

#     if query.lower() in ["exit", "quit", "bye"]:
#         st.write("Assistant: ","good bye!👋 see you in next day.")
#         break
#     llm_response = llm.invoke(query).content
#     st.write("Assistant:", llm_response)
# res = llm.invoke("What is the capital of France?").content
# print(res)
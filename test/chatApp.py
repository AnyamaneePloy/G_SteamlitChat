import streamlit as st #all streamlit commands will be available through the “st" alias
from KBSearch import KBSearch

st.set_page_config(page_title="MBK Chatbot") #HTML title

st.title("BK Chatbot") #page title

# Select your BedRock KM ID

kmID = '8DPQ14YSHO'

# Select your BedRock FM ARN

modelArn = "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2" #replace only modelID
searcher = KBSearch(kmID, modelArn) # function?

if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history

for message in st.session_state.chat_history: #loop through the chat history
    with st.chat_message(message["role"]): #renders a chat line for the given role, containing everything in
        st.markdown(message["text"]) #display the chat content
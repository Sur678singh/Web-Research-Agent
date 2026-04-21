import streamlit as st
from webresearchagent import agent_executor

# make a title 
st.title('🧠 Smart Research Agent')

# generate a query
user_input=st.text_input('Ask Something..')

if st.button('research'):
    response=agent_executor.invoke({'input':user_input})
    st.write(response['output'])
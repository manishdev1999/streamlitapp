
import streamlit as st 
import pandas as pd
import os

from pandasai import Agent

os.environ["PANDASAI_API_KEY"] = "$2a$10$0k8REntSiRs6uUvxPgKSGufomqZTFZoWfRlHbuLKhPY7ltDPaLQJe"

st.title("Log File Analyser")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

       # new code below...
    prompt = st.text_area("Enter your prompt:")
    agent = Agent(df)
    # Generate output
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(agent.chat(prompt))

        else:
            st.warning("Please enter a prompt.")
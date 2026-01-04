

```python
# LUCKY.AI Web Chat – READY TO RUN
import streamlit as st
import openai

# 🔑 Put your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="LUCKY.AI", page_icon="🤖")
st.title("LUCKY.AI 🤖 Web Chat")
st.write("Type a message and LUCKY.AI will reply!")

# Get user input
user_input = st.text_input("You:", "")

if user_input:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
    except:
        answer = "Sorry buddy, I can't answer right now."
    
    st.text_area("LUCKY.AI:", value=answer, height=100)

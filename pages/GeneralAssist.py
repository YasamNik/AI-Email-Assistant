from pathlib import Path
import time
import streamlit as st
import openai
import os

openai.api_key = os.getenv("openAI_key")
def ask_question(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
   stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message
#Variables  "💡"
prompt=""
PAGE_TITLE = "General Assistant"
PAGE_ICON = "images/AI_icon.png"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
previous_dir = os.path.dirname(current_dir)
#print(previous_dir)
css_file = previous_dir + "\styles" + "\main.css"

#Config Page
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#Load css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


st.image("images/email_assistant_circle.png", width=64)
# Title and header
st.title("General AI Assistant")
#st.header("Enter an email body text")


text_input = st.text_area("Enter your question here:")

# Display the text that the user entered
#st.write(f"You entered: {text_input}")

# Add a button to run some logic
if st.button(f"Process"):
    # Do something with the text
    #prompt = f"Please generate a {email_size}, {email_style} style email {notes} from the following text with professional look and paragraph formatting: "
    prompt = text_input
    print(prompt)
    result = ask_question(prompt)
    #st.write(f"Result: {result}")
    #For testing
    st.write("---")
    #text_output = st.text_area("Result is here :", prompt)
    st.code(result, None)


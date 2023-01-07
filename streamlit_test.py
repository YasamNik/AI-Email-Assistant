from pathlib import Path
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
#Variables  
prompt=""
PAGE_TITLE = "Email Assistant"
PAGE_ICON = "💡"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

#Config Page
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#Load css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Sidebar
# Using object notation
email_style = st.sidebar.selectbox(
    "Select Email Format Type",
    ("Business", "Friendly", "Standard")
)

# Using "with" notation
with st.sidebar:
    email_size = st.radio(
        "Choose an email size",
        ("Short", "Long")
    )

# Title and header
st.title("AI Email Assistant")
st.header("Enter an email body text")

# Create a text input field
text_input = st.text_area("Enter email text here :")

# Display the text that the user entered
#st.write(f"You entered: {text_input}")

# Add a button to run some logic
if st.button(f"Process"):
    # Do something with the text
    prompt = f"Please generate a {email_size}, {email_style} style email from the following text: "
    prompt += text_input
    result = ask_question(prompt)
    #st.write(f"Result: {result}")
    #For testing
    st.write("---")
    #text_output = st.text_area("Result is here :", prompt)
    st.code(result, None)


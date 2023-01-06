import streamlit as st
import openai
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

# Title and header
st.title("AI Email Assistant")
st.header("Enter row email body text")

# Create a text input field
text_input = st.text_area("Enter email text here :")
popp = "askdjhbkf"
# Display the text that the user entered
#st.write(f"You entered: {text_input}")

# Add a button to run some logic
if st.button(f"Process"):
    # Do something with the text
    prompt = "Please generate a long polite style email from following text: "
    prompt += text_input
    result = ask_question(prompt)
    st.write(f"Result: {result}")

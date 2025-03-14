import streamlit as st
import google.generativeai as genai

# Configure the Gemini AI API
api_key = "AIzaSyDDTtr126VOgcUW9y6xPlKV26mz4Q8i_K4"
genai.configure(api_key=api_key)

# Define the AI function
def generate_design_idea(style, size, rooms):
    context = f"""
    Generate a home design plan based on:
    - Style: {style}
    - Size: {size} sqft
    - Number of Rooms: {rooms}

    Include layout suggestions, color schemes, and furniture recommendations.
    Return response in Markdown format.
    """
    model = genai.GenerativeModel("gemini-1.5-pro")
    chat = model.start_chat(history=[{"role": "user", "parts": [context]}])
    response = chat.send_message(context)
    return response.text if isinstance(response.text, str) else response.text[0]

# Streamlit UI
st.title("Custom Home Design Assistant")

style = st.text_input("Enter Home Style (e.g., Modern, Rustic)")
size = st.text_input("Enter Home Size (sq ft)")
rooms = st.text_input("Enter Number of Rooms")

if st.button("Generate Design"):
    if style and size and rooms:
        design_idea = generate_design_idea(style, size, rooms)
        st.markdown(design_idea)
    else:
        st.warning("Please fill in all fields.")

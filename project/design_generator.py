import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env 
load_dotenv()
API_KEY = os.getenv("AIzaSyDDTtr126VOgcUW9y6xPlKV26mz4Q8i_K4")

# Configure Generative AI
genai.configure(api_key=API_KEY)

# Function to generate home design ideas
def generate_design_idea(style, size, rooms):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Create a custom home design plan for a {style} home, {size} sq ft, with {rooms} rooms."
    
    response = model.generate_content(prompt)
    
    return response.text if response else "No response generated."
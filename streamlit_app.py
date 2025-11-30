import streamlit as st
from demos import saas_sim, math_quiz, story_writer

# Page Config
st.set_page_config(
    page_title="Antigravity Demo Suite",
    page_icon="🚀",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("🚀 Antigravity")
st.sidebar.markdown("---")
st.sidebar.markdown("### Select a Demo")

demo_selection = st.sidebar.radio(
    "Choose an App:",
    ["Math Whiz 🧮", "SaaS Simulator 📈", "Storyteller AI 🦁"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Antigravity Showcase**
    
    Demonstrating the power of rapid app development.
    """
)

# Main Content Router
if demo_selection == "Math Whiz 🧮":
    math_quiz.run()
elif demo_selection == "SaaS Simulator 📈":
    saas_sim.run()
elif demo_selection == "Storyteller AI 🦁":
    story_writer.run()

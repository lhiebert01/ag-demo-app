import streamlit as st
import random
from gtts import gTTS
import os
import time

def run():
    st.markdown("## 🦁 Storyteller AI")
    st.markdown("### Create your own Aesop-style fable with audio and visuals.")

    # Sidebar Inputs
    st.sidebar.header("📖 Story Settings")
    
    theme = st.sidebar.selectbox(
        "Choose a Theme",
        ["Honesty", "Bravery", "Kindness", "Greed", "Wisdom", "Friendship"]
    )
    
    characters = st.sidebar.multiselect(
        "Choose Characters (Max 3)",
        ["Lion", "Mouse", "Fox", "Crow", "Tortoise", "Hare", "Wolf", "Sheep", "Ant", "Grasshopper"],
        default=["Lion", "Mouse"],
        max_selections=3
    )
    
    if len(characters) < 2:
        st.sidebar.warning("Please select at least 2 characters.")
        return

    if st.sidebar.button("✨ Write My Story", type="primary"):
        with st.spinner("Weaving your tale..."):
            # Simulate AI generation delay
            time.sleep(1.5)
            
            # Simple template-based story generation (Mock AI)
            story_templates = [
                f"Once upon a time, a {characters[0]} and a {characters[1]} were walking through the forest. The {characters[0]} boasted about their strength, but the {characters[1]} remained humble. Suddenly, a storm approached. The {characters[0]} was scared, but the {characters[1]} showed great {theme.lower()} and helped them find shelter. In the end, they learned that true power comes from within.",
                f"In a sunny meadow, a {characters[0]} found a golden coin. A {characters[1]} saw this and felt jealous. They argued over who should keep it. Just then, a wise owl appeared and told them a story about {theme.lower()}. Realizing their mistake, they decided to share the coin and buy food for the hungry. They became the best of friends.",
                f"A {characters[0]} was trapped in a net. A tiny {characters[1]} passed by. 'Please help me!' cried the {characters[0]}. The {characters[1]} hesitated but remembered the value of {theme.lower()}. With great effort, the {characters[1]} freed the {characters[0]}. 'Thank you,' said the {characters[0]}, 'I will never forget your kindness.'"
            ]
            
            story_text = random.choice(story_templates)
            
            # Display Story
            st.markdown("### 📜 The Fable")
            st.write(story_text)
            
            # Display Image (Unsplash)
            keywords = f"{theme} {characters[0]} {characters[1]} forest illustration"
            image_url = f"https://source.unsplash.com/800x400/?{keywords.replace(' ', ',')}"
            # Fallback to a reliable image source if unsplash source is deprecated or slow, 
            # but for demo source.unsplash is usually okay. 
            # Actually source.unsplash is deprecated/unreliable. Let's use a placeholder or generic nature image.
            # Better: Use a reliable placeholder service with text or just generic nature.
            # Let's try to use a specific ID or just generic nature for reliability.
            st.image(f"https://picsum.photos/800/400?grayscale&blur=2", caption=f"The {characters[0]} and the {characters[1]}")
            
            # Generate Audio
            try:
                tts = gTTS(text=story_text, lang='en', slow=False)
                audio_file = "story.mp3"
                tts.save(audio_file)
                
                st.markdown("### 🎧 Listen to the Story")
                st.audio(audio_file)
            except Exception as e:
                st.error(f"Could not generate audio: {e}")

            st.success(f"**Moral of the story:** {theme} is a virtue to be cherished.")


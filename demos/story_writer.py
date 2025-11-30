import streamlit as st
import random
from gtts import gTTS
import os
import time
import urllib.parse

def run():
    st.markdown("## 🦁 Storyteller AI")
    st.markdown("### Create your own Aesop-style fable with audio and visuals.")

    # Theme Definitions
    theme_definitions = {
        "Honesty": "Honesty means telling the truth, even when it is hard or you might get in trouble.",
        "Bravery": "Bravery is not about having no fear, but doing the right thing even when you are scared.",
        "Kindness": "Kindness is being friendly, generous, and considerate to others without expecting anything in return.",
        "Greed": "Greed is a selfish desire to have more of something (like food or money) than you need.",
        "Wisdom": "Wisdom is using your knowledge and experience to make good decisions.",
        "Friendship": "Friendship is a relationship of mutual affection and trust between two or more people.",
        "Perseverance": "Perseverance means to keep trying and not giving up, even when things are difficult.",
        "Humility": "Humility is not thinking you are better than others, and being willing to learn."
    }

    # Sidebar Inputs
    st.sidebar.header("📖 Story Settings")
    
    theme = st.sidebar.selectbox(
        "Choose a Theme",
        list(theme_definitions.keys())
    )
    
    # Expanded Character List
    animals = [
        "Lion", "Mouse", "Fox", "Crow", "Tortoise", "Hare", "Wolf", "Sheep", "Ant", "Grasshopper",
        "Elephant", "Giraffe", "Monkey", "Crocodile", "Owl", "Eagle", "Bear", "Rabbit", "Tiger", "Zebra"
    ]
    
    characters = st.sidebar.multiselect(
        "Choose Characters (Max 3)",
        animals,
        default=["Lion", "Mouse"],
        max_selections=3
    )
    
    if len(characters) < 2:
        st.sidebar.warning("Please select at least 2 characters.")
        return

    if st.sidebar.button("✨ Write My Story", type="primary"):
        with st.spinner("Weaving your tale..."):
            # Simulate AI generation delay
            time.sleep(2.0)
            
            # --- Dynamic Plot Engine ---
            
            c1 = characters[0]
            c2 = characters[1]
            c3 = characters[2] if len(characters) > 2 else "wise old Owl"
            
            # 1. Setting
            settings = [
                "in the heart of the Whispering Woods",
                "on the dusty plains of the Golden Savannah",
                "near the bubbling banks of the Crystal River",
                "high atop the Misty Mountains",
                "in a sun-dappled meadow filled with wildflowers"
            ]
            setting = random.choice(settings)
            
            # 2. Inciting Incident (The "Spark")
            incidents = [
                f"found a mysterious, glowing object hidden beneath a rock",
                f"heard a cry for help echoing from a deep ravine",
                f"decided to hold a contest to see who was the best at everything",
                f"realized that the winter supplies were dangerously low",
                f"stumbled upon a path they had never seen before"
            ]
            incident = random.choice(incidents)
            
            # 3. Conflict (Based on Theme if possible, or generic)
            if theme == "Honesty":
                conflict = f"The {c1} wanted to keep the discovery a secret to gain an advantage, while the {c2} felt they should tell the others."
            elif theme == "Bravery":
                conflict = f"A terrifying storm rolled in. The {c1} wanted to hide, but the {c2} knew they had to warn the village."
            elif theme == "Greed":
                conflict = f"The {c1} tried to take everything for themselves, leaving nothing for the {c2}."
            elif theme == "Kindness":
                conflict = f"The {c1} laughed at a smaller animal who was struggling, but the {c2} felt a tug at their heart."
            else:
                conflict = f"The {c1} and the {c2} argued about the best way to solve the problem, neither willing to listen to the other."

            # 4. Climax (The Turning Point)
            climax_actions = [
                f"Suddenly, the ground beneath them gave way!",
                f"Just then, a fierce eagle swooped down from the sky!",
                f"Without warning, the river burst its banks!",
                f"The mysterious object began to hum with a strange energy!",
                f"They realized they were hopelessly lost as the sun began to set."
            ]
            climax = random.choice(climax_actions)
            
            # 5. Resolution (The Lesson)
            resolution = f"In that moment of danger, the {c1} looked at the {c2}. They realized that {theme.lower()} was the only way forward. Working together, they overcame the obstacle. The {c1} apologized for their earlier behavior, and the {c2} forgave them."

            # Assemble Story
            story_text = (
                f"Once upon a time, {setting}, lived a {c1} and a {c2}. They were very different, but their paths were destined to cross.\n\n"
                f"One day, they {incident}. {conflict}\n\n"
                f"{climax} The {c1} was frozen with fear/uncertainty. But the {c2} remembered the importance of {theme.lower()}.\n\n"
                f"{resolution} From that day on, everyone in the land knew that {theme_definitions[theme].lower()}"
            )
            
            # Display Definition
            st.info(f"**Theme:** {theme}\n\n💡 *{theme_definitions[theme]}*")
            
            # Display Story
            st.markdown("### 📜 The Fable")
            st.write(story_text)
            
            # Generate Dynamic Image Prompt
            # Include specific action and characters
            action_desc = f"{c1} and {c2} in {setting}, {theme} theme"
            image_prompt = f"A children's book illustration of a {action_desc}, colorful, detailed, soft lighting"
            encoded_prompt = urllib.parse.quote(image_prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            st.image(image_url, caption=f"Featuring: {c1}, {c2} (and {c3} if present)")
            
            # Generate Audio
            try:
                tts = gTTS(text=story_text, lang='en', slow=False)
                audio_file = "story.mp3"
                tts.save(audio_file)
                
                st.markdown("### 🎧 Listen to the Story")
                st.audio(audio_file)
            except Exception as e:
                st.error(f"Could not generate audio: {e}")

            st.success(f"**Moral:** {theme_definitions[theme]}")

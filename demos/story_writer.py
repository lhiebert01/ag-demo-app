import streamlit as st
import random
from gtts import gTTS
import os
import time
import urllib.parse

def run():
    st.markdown("## 🦁 Storyteller AI")
    st.markdown("### Create your own Aesop-style fable with audio and visuals.")

    # Sidebar Inputs
    st.sidebar.header("📖 Story Settings")
    
    theme = st.sidebar.selectbox(
        "Choose a Theme",
        ["Honesty", "Bravery", "Kindness", "Greed", "Wisdom", "Friendship", "Perseverance", "Humility"]
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
            
            # Enhanced Story Generation Logic
            c1 = characters[0]
            c2 = characters[1]
            c3 = characters[2] if len(characters) > 2 else "wise old Owl"
            
            intro_templates = [
                f"Deep in the heart of the Whispering Woods, where the trees touched the sky and the rivers sang songs of old, lived a {c1} and a {c2}. The {c1} was known far and wide for their strength and pride, while the {c2} was quiet, observant, and often overlooked by the other animals.",
                f"On the edge of the Golden Savannah, under the watchful eye of the midday sun, a {c1} and a {c2} crossed paths. The {c1} was busy collecting food for the winter, always anxious about the future. The {c2}, on the other hand, lived for the moment, enjoying the warmth of the sun and the scent of the blooming flowers.",
                f"High up in the Misty Mountains, a {c1} made their home in a cozy cave. Not far away, a {c2} lived in a burrow beneath an ancient oak tree. Despite their differences, they were neighbors in this rugged land. The {c1} often boasted of their adventures, while the {c2} preferred the safety of their home."
            ]
            
            conflict_templates = [
                f"One day, a great drought fell upon the land. The rivers dried up, and the green grass turned to dust. The animals grew hungry and thirsty. The {c1}, relying on their strength, tried to hoard the remaining water, refusing to share with the smaller animals. 'I am the strongest,' the {c1} declared, 'I deserve to survive.' The {c2} watched in sadness, knowing that selfishness would only lead to ruin.",
                f"A rumor spread through the forest that a hunter was approaching. Panic seized the animals. The {c1} decided to run and hide, thinking only of their own safety. 'Every animal for themselves!' shouted the {c1} as they fled. The {c2}, however, saw that the younger animals were too slow to escape and knew they needed help.",
                f"The {c1} found a shiny, magical gemstone that was said to grant one wish. Overcome by greed, the {c1} wanted to wish for eternal power. 'With this, I shall rule the forest!' the {c1} proclaimed. The {c2} warned, 'Power without wisdom is dangerous. We should use it to heal the forest.' But the {c1} would not listen."
            ]
            
            climax_templates = [
                f"Suddenly, a fierce storm broke the silence. Lightning struck a nearby tree, setting it ablaze. The fire spread rapidly, trapping the {c1}. The {c1} roared for help, but the other animals were too afraid. Just then, the {c2} remembered the virtue of {theme.lower()}. Despite the danger, the {c2} rallied the other animals. 'We must help, for we are all part of this forest!' cried the {c2}.",
                f"The hunter's trap snapped shut, capturing the {c1}. The {c1} struggled and roared, but the ropes only tightened. All hope seemed lost. The {c2} approached carefully. 'Why help me?' asked the {c1}, ashamed of their earlier selfishness. 'Because {theme.lower()} is what binds us,' replied the {c2}. The {c2} began to gnaw at the ropes.",
                f"As the {c1} held the gemstone, the ground began to shake. The magic was too unstable! The {c1} was paralyzed with fear. The {c3} appeared and shouted, 'Drop it! Only a selfless heart can control the magic!' The {c1} looked at the {c2}, who nodded encouragingly. With a trembling hand, the {c1} tossed the stone to the {c2}."
            ]
            
            resolution_templates = [
                f"Working together, the animals extinguished the fire and saved the {c1}. The {c1} looked at the {c2} with new respect. 'I was wrong,' admitted the {c1}. 'Strength is not just about muscles, but about the heart.' From that day on, the {c1} and the {c2} worked together to protect the forest, teaching everyone that {theme.lower()} conquers all.",
                f"The ropes gave way, and the {c1} was free. The {c1} hugged the {c2}, tears in their eyes. 'You saved me, even after I abandoned you,' said the {c1}. 'That is the true meaning of {theme.lower()},' smiled the {c2}. They returned to the clearing, where the {c1} apologized to the others and vowed to always help those in need.",
                f"The {c2} caught the stone and wished for rain to heal the land. Gentle rain began to fall, and the flowers bloomed instantly. The {c1} felt a weight lift from their shoulders. 'Thank you,' whispered the {c1}. 'You showed me that {theme.lower()} is the greatest treasure of all.' The {c3} smiled, knowing the lesson had been learned."
            ]
            
            # Assemble Story
            part1 = random.choice(intro_templates)
            part2 = random.choice(conflict_templates)
            part3 = random.choice(climax_templates)
            part4 = random.choice(resolution_templates)
            
            story_text = f"{part1}\n\n{part2}\n\n{part3}\n\n{part4}"
            
            # Display Story
            st.markdown("### 📜 The Fable")
            st.write(story_text)
            
            # Generate Dynamic Image Prompt
            image_prompt = f"A storybook illustration of a {c1} and a {c2} in a forest, theme of {theme}, digital art, warm colors, detailed, 4k"
            encoded_prompt = urllib.parse.quote(image_prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            st.image(image_url, caption=f"The {c1} and the {c2} - A Tale of {theme}")
            
            # Generate Audio
            try:
                tts = gTTS(text=story_text, lang='en', slow=False)
                audio_file = "story.mp3"
                tts.save(audio_file)
                
                st.markdown("### 🎧 Listen to the Story")
                st.audio(audio_file)
            except Exception as e:
                st.error(f"Could not generate audio: {e}")

            st.success(f"**Moral of the story:** True {theme.lower()} is shown not in words, but in deeds.")

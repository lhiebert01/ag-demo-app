import streamlit as st
import random
from gtts import gTTS
import os
import time
import urllib.parse

def run():
    st.markdown("## 🦁 Storyteller AI")
    st.markdown("### Create your own Aesop-style fable with audio and visuals.")

    # Theme Definitions (Expanded)
    theme_definitions = {
        "Honesty": "Honesty means telling the truth, even when it is hard or you might get in trouble.",
        "Bravery": "Bravery is not about having no fear, but doing the right thing even when you are scared.",
        "Kindness": "Kindness is being friendly, generous, and considerate to others without expecting anything in return.",
        "Greed": "Greed is a selfish desire to have more of something than you need. The way to overcome it is Generosity.",
        "Wisdom": "Wisdom is using your knowledge and experience to make good decisions.",
        "Friendship": "Friendship is a relationship of mutual affection and trust between two or more people.",
        "Perseverance": "Perseverance means to keep trying and not giving up, even when things are difficult.",
        "Humility": "Humility is not thinking you are better than others, and being willing to learn.",
        "Patience": "Patience is the ability to wait calmly without getting annoyed or upset.",
        "Responsibility": "Responsibility means doing what you are supposed to do and accepting the results of your actions.",
        "Forgiveness": "Forgiveness is letting go of anger towards someone who has hurt you.",
        "Gratitude": "Gratitude is being thankful for what you have and showing appreciation.",
        "Teamwork": "Teamwork is working together with others to achieve a common goal.",
        "Respect": "Respect is treating others with courtesy and consideration."
    }

    # Map Vices to their Antidotes (Virtues)
    antidotes = {
        "Greed": "Generosity",
        "Pride": "Humility",
        "Selfishness": "Kindness",
        "Impatience": "Patience"
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

    # User-Selectable Traits
    st.sidebar.subheader("🎭 Character Traits")
    available_traits = ["Brave", "Cautious", "Wise", "Curious", "Proud", "Gentle", "Quick", "Strong", "Jolly", "Grumpy", "Shy", "Boastful", "Patient", "Energetic"]
    
    char_objs = []
    for char_name in characters:
        trait = st.sidebar.selectbox(
            f"Trait for {char_name}",
            available_traits,
            key=f"trait_{char_name}",
            index=random.randint(0, len(available_traits)-1) # Random default
        )
        char_objs.append({
            "name": char_name,
            "trait": trait
        })

    if st.sidebar.button("✨ Write My Story", type="primary"):
        with st.spinner("Weaving a deeper tale..."):
            # Simulate AI generation delay
            time.sleep(2.5)
            
            # --- Dynamic Plot Engine v4 (Deep Story + Smooth Transition) ---
            
            # Helper to format list of characters
            def format_chars(chars):
                names = [f"the {c['trait']} {c['name']}" for c in chars]
                if len(names) == 2:
                    return f"{names[0]} and {names[1]}"
                else:
                    return f"{', '.join(names[:-1])}, and {names[-1]}"

            group_name = format_chars(char_objs)
            c1 = char_objs[0]
            c2 = char_objs[1]
            c3 = char_objs[2] if len(char_objs) > 2 else None
            
            # Determine the Solution Virtue (Antidote)
            solution_virtue = antidotes.get(theme, theme)

            # 1. Setting (Detailed)
            settings = [
                "in the heart of the Whispering Woods, where the ancient trees hummed with secrets and the sunlight danced through the emerald leaves",
                "on the vast, sun-baked plains of the Golden Savannah, stretching as far as the eye could see under a limitless blue sky",
                "near the bubbling banks of the Crystal River, whose waters were so clear you could count every pebble on the bottom",
                "high atop the Misty Mountains, where the air was crisp and cold, and the clouds drifted like silent ships below",
                "in a lush, sun-dappled meadow filled with wildflowers of every color, buzzing with the busy work of bees"
            ]
            setting = random.choice(settings)
            
            # 2. The Journey (Bonding/Setup)
            journeys = [
                f"They had been traveling for many days, seeking the legendary Fruit of Knowledge. The journey had been long, but their spirits were high.",
                f"It was a season of plenty, and they spent their days gathering food and sharing stories of their ancestors.",
                f"They were an unlikely group of friends, brought together by a shared love of exploring the unknown corners of their world.",
                f"The summer sun was hot, and they were searching for a cool, shaded grove to rest their weary paws and wings."
            ]
            journey = random.choice(journeys)

            # 3. Dialogue (Character Interaction)
            dialogue_intro = ""
            if c3:
                dialogue_intro = f'"I wonder what we will find today," mused the {c1["name"]}. "Hopefully something safe," replied the {c2["name"]} nervously. The {c3["name"]} just laughed, "Adventure awaits those who seek it!"'
            else:
                dialogue_intro = f'"Do you think we are lost?" asked the {c1["name"]}. "Not as long as we have each other," smiled the {c2["name"]}.'

            # 4. Inciting Incident (The "Spark")
            incidents = [
                f"stumbled upon a mysterious, glowing object half-buried in the earth",
                f"heard a faint, desperate cry for help echoing from a deep, dark ravine",
                f"found a single, perfect path that seemed to lead to nowhere and everywhere at once",
                f"realized that their precious supply of water had mysteriously vanished",
                f"saw a strange, shimmering portal open up right in front of them"
            ]
            incident = random.choice(incidents)
            
            # 5. Conflict (Deepened based on Theme)
            conflict = ""
            if theme == "Honesty":
                conflict = (f"The {c1['name']} recognized the object. It was valuable, but it belonged to the River Spirit. "
                           f'"We should keep it," they whispered, eyes gleaming. "No one will know." '
                           f'The {c2["name"]} frowned. "But that would be stealing. We must return it." '
                           f'Tension filled the air as they argued, the object pulsing with a strange light.')
            elif theme == "Bravery":
                conflict = (f"Suddenly, a terrifying storm rolled in, turning the sky black. Thunder shook the ground. "
                           f'"Run! Hide!" cried the {c1["name"]}, cowering behind a rock. '
                           f'But the {c2["name"]} saw a small bird trapped in a thorn bush nearby. '
                           f'"We cannot leave it!" they shouted over the wind. The fear was palpable, gripping their hearts.')
            elif theme == "Greed":
                conflict = (f"It was a treasure trove of delicious berries, more than they could eat in a lifetime. "
                           f'The {c1["name"]}\'s eyes went wide. "It is mine! All mine!" they roared, blocking the others. '
                           f'"But there is enough for everyone," pleaded the {c2["name"]}. '
                           f'The {c1["name"]} would not listen, consumed by a selfish desire to hoard everything.')
            elif theme == "Kindness":
                conflict = (f"They met an old, weary traveler who asked for a share of their food. "
                           f'"Go away, old one," scoffed the {c1["name"]}. "We have barely enough for ourselves." '
                           f'The traveler slumped in defeat. The {c2["name"]} felt a sharp pang of guilt. '
                           f'"How can we turn them away?" they whispered. "It is not right."')
            else:
                conflict = f"They faced a great obstacle that blocked their path. They argued bitterly about how to proceed, each thinking their way was the only way, refusing to listen to reason."

            # 6. Climax (High Stakes)
            climax = ""
            if theme == "Greed":
                climax = (f"Suddenly, the ground beneath the berries began to crumble! The weight of the hoard was too much. "
                         f'The {c1["name"]} slipped, sliding towards a dark pit, clutching the berries tight. '
                         f'"Help me!" they cried, but their hands were full of treasure.')
            else:
                climax = (f"The situation grew dire. The storm worsened, the danger closed in, and it seemed all hope was lost. "
                         f'The {c1["name"]} froze, unable to move. The {c2["name"]} reached out, but the gap was too wide.')

            # 7. Realization (The Turn)
            realization = ""
            if theme == "Greed":
                realization = (f"In that terrifying moment, the {c1['name']} looked at their friends. They realized the berries were heavy, useless stones dragging them down. "
                              f'"Take my hand!" shouted the {c2["name"]}. "Drop the berries!" '
                              f'With a cry of frustration, the {c1["name"]} let go of the treasure. They reached out, empty-handed but free.')
            else:
                realization = (f"They looked into each other's eyes. They realized that their fear and selfishness were the real enemies. "
                              f'"We must work together," shouted the {c2["name"]}. "It is the only way!" '
                              f'They nodded, a new resolve hardening in their hearts. They chose {solution_virtue.lower()}.')

            # 8. Transition (Reflection & Application) - NEW PHASE
            transition = (f"After the danger had passed, the group sat together in silence for a long moment, catching their breath. "
                         f"The {c1['name']} looked down, feeling a mix of relief and shame. "
                         f'"I almost let us down," they whispered. "I let my feelings get the better of me." '
                         f'The {c2["name"]} placed a comforting paw on their shoulder. "But you made the right choice in the end," they said gently. '
                         f'"That is what matters. We learned that {solution_virtue.lower()} is not just a word, but an action we must choose every day."')

            # 9. Resolution (The Lesson & Future)
            resolution = (f"With a mighty effort, and guided by {solution_virtue.lower()}, they pulled through. "
                         f"The {c1['name']} was safe, panting heavily. They looked at the {c2['name']} with gratitude. "
                         f'"I was wrong," they admitted softly. "Thank you for showing me the way." '
                         f"The group embraced, stronger than before. "
                         f"From that day on, whenever they faced a challenge, they remembered this moment. They taught the young ones in the forest that {solution_virtue.lower()} is the true key to a happy life. And so, they lived happily ever after, sharing their stories with all who would listen.")

            # Assemble Story
            story_text = (
                f"Once upon a time, {setting}, lived a unique group of friends: {group_name}. They were very different in size and shape, but their bond was strong.\n\n"
                f"{journey} {dialogue_intro}\n\n"
                f"One fateful day, as the sun climbed high in the sky, they {incident}. It was a moment that would test their friendship forever. {conflict}\n\n"
                f"{climax}\n\n"
                f"{realization}\n\n"
                f"{transition}\n\n"
                f"{resolution}"
            )
            
            # Display Definition
            st.info(f"**Theme:** {theme}\n\n💡 *{theme_definitions[theme]}*")
            
            # Display Story
            st.markdown("### 📜 The Fable")
            st.write(story_text)
            
            # Generate Dynamic Image Prompt (Improved Strategy)
            # Focus on distinct characters and style
            char_list_prompt = ", ".join([c['name'] for c in char_objs])
            
            # New Prompt Strategy: 3D Pixar Style, Distinct Characters
            image_prompt = (
                f"3D Disney Pixar style render of {char_list_prompt} standing together in {setting}. "
                f"Cute, expressive faces, distinct characters, high quality, 4k, masterpiece, soft cinematic lighting, detailed fur and textures."
            )
            encoded_prompt = urllib.parse.quote(image_prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            st.image(image_url, caption=f"Featuring: {char_list_prompt}")
            
            # Generate Audio
            try:
                tts = gTTS(text=story_text, lang='en', slow=False)
                audio_file = "story.mp3"
                tts.save(audio_file)
                
                st.markdown("### 🎧 Listen to the Story")
                st.audio(audio_file)
            except Exception as e:
                st.error(f"Could not generate audio: {e}")

            st.success(f"**Moral:** {solution_virtue} is a virtue to be cherished.")

import streamlit as st
import random
import time
import pandas as pd

def run():
    st.markdown("## 🧮 Math Whiz Challenge")
    st.markdown("### Test your mental math skills and climb the leaderboard!")

    # Sidebar Settings
    st.sidebar.header("⚙️ Game Settings")
    difficulty = st.sidebar.select_slider("Difficulty", options=["Easy", "Medium", "Hard"], value="Medium")
    num_questions = st.sidebar.selectbox("Number of Questions", [5, 10, 20], index=1)

    # Initialize Session State
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'current_q_index' not in st.session_state:
        st.session_state.current_q_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'start_time' not in st.session_state:
        st.session_state.start_time = 0
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Game Logic Functions
    def start_game():
        st.session_state.game_active = True
        st.session_state.current_q_index = 0
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.questions = []
        
        for _ in range(num_questions):
            if difficulty == "Easy":
                n1, n2 = random.randint(2, 9), random.randint(2, 9)
            elif difficulty == "Medium":
                n1, n2 = random.randint(5, 12), random.randint(5, 12)
            else:
                n1, n2 = random.randint(10, 20), random.randint(5, 15)
            
            correct = n1 * n2
            options = {correct}
            while len(options) < 4:
                offset = random.randint(-10, 10)
                if offset != 0:
                    options.add(correct + offset)
            
            st.session_state.questions.append({
                "q": f"{n1} × {n2}",
                "a": correct,
                "opts": list(options)
            })
            # Shuffle options
            random.shuffle(st.session_state.questions[-1]["opts"])

    def check_answer(selected, correct):
        if selected == correct:
            st.session_state.score += 1
            st.toast("Correct! 🎉", icon="✅")
        else:
            st.toast(f"Wrong! It was {correct}", icon="❌")
        
        st.session_state.current_q_index += 1
        
        if st.session_state.current_q_index >= num_questions:
            end_game()

    def end_game():
        st.session_state.game_active = False
        duration = time.time() - st.session_state.start_time
        st.session_state.history.append({
            "Score": f"{st.session_state.score}/{num_questions}",
            "Time": f"{duration:.1f}s",
            "Difficulty": difficulty
        })
        st.balloons()

    # UI Rendering
    if not st.session_state.game_active:
        if st.button("▶️ Start New Game", use_container_width=True, type="primary"):
            start_game()
            st.rerun()
        
        if st.session_state.history:
            st.markdown("### 🏆 Recent Games")
            st.dataframe(pd.DataFrame(st.session_state.history).iloc[::-1], use_container_width=True)

    else:
        # Progress Bar
        progress = st.session_state.current_q_index / num_questions
        st.progress(progress, text=f"Question {st.session_state.current_q_index + 1} of {num_questions}")
        
        q_data = st.session_state.questions[st.session_state.current_q_index]
        
        st.markdown(f"<h1 style='text-align: center; font-size: 4rem;'>{q_data['q']} = ?</h1>", unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, opt in enumerate(q_data['opts']):
            with cols[i % 2]:
                if st.button(str(opt), key=f"opt_{i}", use_container_width=True):
                    check_answer(opt, q_data['a'])
                    st.rerun()

        st.markdown(f"**Current Score:** {st.session_state.score}")

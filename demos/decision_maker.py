import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.markdown("## 🏗️ Decision Architect")
    st.markdown("### Visualize complex decisions and find the best path forward.")

    # Initialize Session State
    if 'options' not in st.session_state:
        st.session_state.options = ["Option A", "Option B"]
    if 'criteria' not in st.session_state:
        st.session_state.criteria = [{"name": "Cost", "weight": 50}, {"name": "Quality", "weight": 50}]

    # Sidebar Controls
    st.sidebar.header("📝 Setup Decision")
    
    # Manage Options
    st.sidebar.subheader("1. Define Options")
    new_option = st.sidebar.text_input("Add Option", placeholder="e.g., Hawaii")
    if st.sidebar.button("Add Option"):
        if new_option and new_option not in st.session_state.options:
            st.session_state.options.append(new_option)
    
    if st.sidebar.button("Clear All Options"):
        st.session_state.options = []

    st.sidebar.write("Current Options:", ", ".join(st.session_state.options))

    # Manage Criteria
    st.sidebar.subheader("2. Define Criteria")
    new_crit_name = st.sidebar.text_input("Criterion Name", placeholder="e.g., Price")
    new_crit_weight = st.sidebar.slider("Weight (%)", 0, 100, 50)
    
    if st.sidebar.button("Add Criterion"):
        if new_crit_name:
            st.session_state.criteria.append({"name": new_crit_name, "weight": new_crit_weight})

    if st.sidebar.button("Clear Criteria"):
        st.session_state.criteria = []

    # Main Area - Scoring Matrix
    if not st.session_state.options or not st.session_state.criteria:
        st.info("👈 Please add at least one Option and one Criterion in the sidebar to start.")
        return

    st.markdown("### 3. Rate Your Options")
    
    scores = {}
    
    # Create tabs for each option to rate them
    tabs = st.tabs(st.session_state.options)
    
    for i, option in enumerate(st.session_state.options):
        with tabs[i]:
            st.subheader(f"Rate {option}")
            option_scores = {}
            for criterion in st.session_state.criteria:
                val = st.slider(
                    f"{criterion['name']} (Weight: {criterion['weight']}%)", 
                    0, 10, 5, 
                    key=f"{option}_{criterion['name']}"
                )
                option_scores[criterion['name']] = val * (criterion['weight'] / 100)
            scores[option] = sum(option_scores.values())

    # Results
    st.markdown("---")
    st.markdown("### 🏆 The Verdict")
    
    results_df = pd.DataFrame(list(scores.items()), columns=["Option", "Total Score"])
    results_df = results_df.sort_values("Total Score", ascending=False)
    
    winner = results_df.iloc[0]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.success(f"**Winner:** {winner['Option']}")
        st.metric("Winning Score", f"{winner['Total Score']:.1f}")
        if st.button("Celebrate Winner! 🎉"):
            st.balloons()
            
    with col2:
        fig = px.bar(
            results_df, 
            x="Total Score", 
            y="Option", 
            orientation='h',
            title="Decision Matrix Results",
            color="Total Score",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig, use_container_width=True)

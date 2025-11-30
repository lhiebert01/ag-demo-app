# Antigravity Demo Suite - Project Objectives & Requirements

## 🎯 Objectives
The primary objective of this project is to create a compelling suite of demo applications that showcase the capabilities of the Antigravity platform (or the developer's rapid prototyping skills) to a broad audience.

The suite aims to:
1.  **Demonstrate Versatility:** Showcasing different types of apps (Gamified Education, Business Tools, Creative AI).
2.  **Engage Users:** providing interactive, "wow" moments through audio, visuals, and dynamic content.
3.  **Prove Value:** Solving real user problems (learning math, forecasting growth, creating stories).

## 🛠️ Technology Stack
- **Language:** Python 3.x
- **Framework:** Streamlit (for rapid web app development)
- **Libraries:**
    - `pandas`: Data manipulation (SaaS Simulator).
    - `plotly`: Interactive charts (SaaS Simulator).
    - `gTTS` (Google Text-to-Speech): Audio generation (Storyteller AI).
- **External APIs:**
    - `pollinations.ai`: Free, dynamic image generation.

## 📂 Project Structure
```
c:/src/ag-test1/
├── streamlit_app.py       # Main Launcher (Entry Point)
├── requirements.txt       # Python dependencies
├── README.md              # User-facing documentation
├── README-OBJECTIVES.md   # This file (Dev documentation)
├── README-future.md       # Future roadmap and hidden features
└── demos/                 # Application Modules
    ├── __init__.py
    ├── math_quiz.py       # Demo 1: Math Whiz
    ├── story_writer.py    # Demo 2: Storyteller AI
    └── saas_sim.py        # Hidden: SaaS Simulator
```

## ✅ Requirements

### 1. Main Launcher (`streamlit_app.py`)
- Must provide a sidebar navigation menu.
- Must allow switching between active demos.
- Must display branding ("Antigravity Demo Suite").

### 2. Math Whiz (`demos/math_quiz.py`)
- **Features:** Multiplication quiz, difficulty levels, score tracking.
- **UX:** Gamified feedback (balloons, toasts), history sidebar.

### 3. Storyteller AI (`demos/story_writer.py`)
- **Features:**
    - Aesop-style fable generation.
    - Multi-character support (2-3 characters).
    - Dynamic plot engine (Setting -> Incident -> Conflict -> Climax -> Resolution).
    - **Logic:** Must distinguish between Vices (e.g., Greed) and Virtues. Vices must be resolved by their Antidote (e.g., Generosity).
    - **Media:** Dynamic image generation listing all characters; Audio playback of the story.
- **UX:** clear definitions of themes/morals.

### 4. SaaS Simulator (`demos/saas_sim.py`)
- **Status:** Currently hidden from the main menu but code must be preserved.
- **Features:** MRR/ARR forecasting, interactive charts.

## 🚀 Deployment
- The app is designed to be deployed on **Streamlit Cloud** or **Render**.
- Requires `requirements.txt` for dependency installation.

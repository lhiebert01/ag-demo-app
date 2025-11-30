# 🚀 SaaS Growth Simulator

A powerful, interactive dashboard to forecast your startup's growth metrics. Built with [Streamlit](https://streamlit.io) and Python.

## Features

- **Interactive Modeling**: Adjust Growth Rate, Churn Rate, and ARPU in real-time.
- **Visual Forecasts**: Beautiful charts for MRR (Monthly Recurring Revenue) and User Growth.
- **Key Metrics**: Instant calculation of Projected ARR (Annual Recurring Revenue) and LTV.
- **Export Data**: Download your forecast as a CSV file for further analysis.

## How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lhiebert01/ag-demo-app.git
   cd ag-demo-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run streamlit_app.py
   ```

## Deployment

### Deploy to Streamlit Cloud (Recommended)

1. Push this code to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect your GitHub account and select your repository.
4. Click **Deploy**!

### Deploy to Render

1. Create a new **Web Service** on Render.
2. Connect your GitHub repository.
3. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0`

## Built With

- [Streamlit](https://streamlit.io) - The fastest way to build data apps in Python.
- [Plotly](https://plotly.com) - Interactive graphing library.
- [Pandas](https://pandas.pydata.org) - Data manipulation and analysis.

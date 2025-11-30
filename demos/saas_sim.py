import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.markdown("## 🚀 SaaS Growth Simulator")
    st.markdown("### Forecast your recurring revenue and visualize your startup's trajectory.")

    # Sidebar Controls (Local to this function/page)
    st.sidebar.header("⚙️ Simulation Settings")

    current_mrr = st.sidebar.number_input("Current MRR ($)", value=5000, step=100)
    growth_rate = st.sidebar.slider("Monthly Growth Rate (%)", 0.0, 20.0, 5.0, 0.1)
    churn_rate = st.sidebar.slider("Monthly Churn Rate (%)", 0.0, 10.0, 2.0, 0.1)
    arpu = st.sidebar.number_input("Average Revenue Per User (ARPU) ($)", value=50, step=5, min_value=1)
    months_to_simulate = st.sidebar.slider("Forecast Period (Months)", 6, 36, 12)

    # Simulation Logic
    months = []
    revenues = []
    users = []

    current_revenue = current_mrr
    current_users = int(current_mrr / arpu)

    for month in range(months_to_simulate + 1):
        months.append(month)
        revenues.append(current_revenue)
        users.append(current_users)
        
        # Calculate next month
        new_users = int(current_users * (growth_rate / 100))
        churned_users = int(current_users * (churn_rate / 100))
        net_users = current_users + new_users - churned_users
        
        current_users = net_users
        current_revenue = current_users * arpu

    # Create DataFrame
    df = pd.DataFrame({
        "Month": months,
        "MRR": revenues,
        "Users": users
    })

    # Key Metrics (Projected)
    final_mrr = revenues[-1]
    final_arr = final_mrr * 12
    total_growth = ((final_mrr - current_mrr) / current_mrr) * 100

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Current MRR", value=f"${current_mrr:,.0f}")
    with col2:
        st.metric(label="Projected MRR", value=f"${final_mrr:,.0f}", delta=f"{total_growth:.1f}%")
    with col3:
        st.metric(label="Projected ARR", value=f"${final_arr:,.0f}")
    with col4:
        st.metric(label="Projected Users", value=f"{users[-1]:,.0f}")

    # Visualizations
    st.markdown("---")

    tab1, tab2 = st.tabs(["📈 Revenue Forecast", "👥 User Growth"])

    with tab1:
        fig_revenue = px.area(
            df, 
            x="Month", 
            y="MRR", 
            title="Projected Monthly Recurring Revenue (MRR)",
            labels={"MRR": "Revenue ($)"},
            color_discrete_sequence=["#3b82f6"]
        )
        fig_revenue.update_layout(plot_bgcolor="white", hovermode="x unified")
        st.plotly_chart(fig_revenue, use_container_width=True)

    with tab2:
        fig_users = px.line(
            df, 
            x="Month", 
            y="Users", 
            title="Projected User Base",
            markers=True,
            color_discrete_sequence=["#10b981"]
        )
        fig_users.update_layout(plot_bgcolor="white", hovermode="x unified")
        st.plotly_chart(fig_users, use_container_width=True)

    # Data Table
    st.markdown("### 📊 Detailed Breakdown")
    st.dataframe(df.style.format({"MRR": "${:,.2f}", "Users": "{:,.0f}"}), use_container_width=True)

"""
GIST Internship - Data Science Domain
Task 4 (Mandatory): Interactive Data Dashboard
Dataset: Superstore Sales Dataset (8,399 orders)

An interactive Streamlit dashboard with filters, KPIs, and trend visualizations.
Run with: streamlit run app.py
"""

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="wide",
)

# ------------------------------------------------------------------
# LOAD & PREPARE DATA
# ------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("superstore_raw.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    return df

df = load_data()

# ------------------------------------------------------------------
# SIDEBAR FILTERS
# ------------------------------------------------------------------
st.sidebar.header("🔎 Filters")

years = sorted(df["Year"].unique())
selected_years = st.sidebar.multiselect("Year", years, default=years)

regions = sorted(df["Region"].dropna().unique())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)

categories = sorted(df["Product Category"].dropna().unique())
selected_categories = st.sidebar.multiselect("Product Category", categories, default=categories)

segments = sorted(df["Customer Segment"].dropna().unique())
selected_segments = st.sidebar.multiselect("Customer Segment", segments, default=segments)

# Apply filters
filtered = df[
    df["Year"].isin(selected_years)
    & df["Region"].isin(selected_regions)
    & df["Product Category"].isin(selected_categories)
    & df["Customer Segment"].isin(selected_segments)
]

st.sidebar.markdown("---")
st.sidebar.caption(f"Showing **{len(filtered):,}** of {len(df):,} total orders")

# ------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------
st.title("📊 Superstore Sales Dashboard")
st.markdown("An interactive dashboard exploring sales performance, profitability, and trends across regions and product categories.")

# ------------------------------------------------------------------
# KPI CARDS
# ------------------------------------------------------------------
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
total_orders = filtered["Order ID"].nunique()
avg_margin = filtered["Profit Margin"].mean() * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("🧾 Total Orders", f"{total_orders:,}")
col4.metric("📊 Avg Profit Margin", f"{avg_margin:.1f}%")

st.markdown("---")

# ------------------------------------------------------------------
# ROW 1: TREND OVER TIME + REGION BREAKDOWN
# ------------------------------------------------------------------
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Sales & Profit Trend Over Time")
    monthly = filtered.groupby("Month")[["Sales", "Profit"]].sum().reset_index()
    fig = px.line(monthly, x="Month", y=["Sales", "Profit"], markers=True)
    fig.update_layout(legend_title_text="", xaxis_title="", yaxis_title="USD")
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("Sales by Region")
    region_sales = filtered.groupby("Region")["Sales"].sum().reset_index()
    fig2 = px.pie(region_sales, names="Region", values="Sales", hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------------
# ROW 2: CATEGORY PERFORMANCE + DISCOUNT VS PROFIT
# ------------------------------------------------------------------
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("Sales & Profit by Product Category")
    cat_data = filtered.groupby("Product Category")[["Sales", "Profit"]].sum().reset_index()
    fig3 = px.bar(cat_data, x="Product Category", y=["Sales", "Profit"], barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

with col_right2:
    st.subheader("Discount vs Profit Margin")
    sample = filtered.sample(min(1500, len(filtered)), random_state=42) if len(filtered) > 0 else filtered
    fig4 = px.scatter(
        sample, x="Discount", y="Profit Margin", color="Product Category",
        opacity=0.6, hover_data=["Sales"],
    )
    st.plotly_chart(fig4, use_container_width=True)

# ------------------------------------------------------------------
# ROW 3: TOP PRODUCTS + CUSTOMER SEGMENT
# ------------------------------------------------------------------
col_left3, col_right3 = st.columns(2)

with col_left3:
    st.subheader("Top 10 Sub-Categories by Sales")
    top_sub = (
        filtered.groupby("Product Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig5 = px.bar(top_sub, x="Sales", y="Product Sub-Category", orientation="h")
    fig5.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig5, use_container_width=True)

with col_right3:
    st.subheader("Sales by Customer Segment")
    seg_data = filtered.groupby("Customer Segment")["Sales"].sum().reset_index()
    fig6 = px.bar(seg_data, x="Customer Segment", y="Sales", color="Customer Segment")
    st.plotly_chart(fig6, use_container_width=True)

# ------------------------------------------------------------------
# INSIGHTS SECTION
# ------------------------------------------------------------------
st.markdown("---")
st.subheader("💡 Key Insights")

if len(filtered) > 0:
    best_region = filtered.groupby("Region")["Sales"].sum().idxmax()
    best_category = filtered.groupby("Product Category")["Profit"].sum().idxmax()
    worst_margin_cat = filtered.groupby("Product Category")["Profit Margin"].mean().idxmin()

    st.markdown(f"""
    - **{best_region}** is the top-performing region by total sales in the current filter selection.
    - **{best_category}** generates the highest total profit among product categories.
    - **{worst_margin_cat}** has the lowest average profit margin — a good candidate to review pricing or discount strategy.
    - Higher discount levels are visibly associated with lower (and sometimes negative) profit margins — see the Discount vs Profit Margin chart above.
    """)
else:
    st.info("No data matches the current filters. Try adjusting your selections in the sidebar.")

# ------------------------------------------------------------------
# RAW DATA TABLE (EXPANDABLE)
# ------------------------------------------------------------------
with st.expander("🔍 View Filtered Raw Data"):
    st.dataframe(filtered)

st.markdown("---")
st.caption("Built for the GIST 4-Week Remote Internship Program — Data Science Domain — Task 4")

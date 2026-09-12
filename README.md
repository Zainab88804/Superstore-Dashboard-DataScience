# Superstore Sales — Interactive Data Dashboard

**GIST Internship Program 2026 — Data Science Domain — Task 4 (Mandatory, Advanced+)**

🔗 **Live Demo:** [Add your Streamlit Cloud link here after deploying]

## 📌 Project Description
An interactive, filterable business intelligence dashboard built on 8,399 real sales orders from a fictional superstore. The dashboard lets a user explore sales performance, profitability, and trends across regions, product categories, customer segments, and time — the kind of tool a real business analyst would use to make data-driven decisions.

## What This Project Covers
- **4 interactive filters**: Year, Region, Product Category, Customer Segment (all combinable)
- **4 real-time KPI cards**: Total Sales, Total Profit, Total Orders, Average Profit Margin
- **6 interactive visualizations**: sales/profit trend over time, sales by region, category performance, discount-vs-profit-margin relationship, top sub-categories, and sales by customer segment
- **Auto-generated insights** that update live based on whatever filters are applied
- An expandable raw data table for full transparency

## Technologies / Tools Used
- Python 3
- **Streamlit** — the dashboard framework (turns a Python script into a full interactive web app)
- **Plotly** — interactive charts (hover, zoom, and pan built in, unlike static matplotlib charts)
- pandas, numpy — data processing

## Repository Structure
```
sales-dashboard/
├── app.py                 # Main Streamlit dashboard application
├── superstore_raw.csv     # Dataset (8,399 sales orders)
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation / Setup Instructions
1. Clone this repository and navigate into it
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run app.py
   ```
4. It will automatically open in your browser at `http://localhost:8501`

## How to Get a Live Public Link (Streamlit Community Cloud — free)
1. Push this repository to GitHub (already done if you're reading this on GitHub)
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account
3. Click "New app", select this repository, set the main file to `app.py`, and click "Deploy"
4. In a minute or two, you'll get a public URL like `https://your-app-name.streamlit.app` that anyone can open — no installation needed
5. Add that link to the top of this README and to your submission form

## Key Insights the Dashboard Reveals
- Sales and profit show clear seasonal patterns across months, useful for planning inventory and staffing
- Some regions consistently outperform others in total sales, highlighting where the business is strongest
- Higher discount percentages are associated with lower (and sometimes negative) profit margins — a direct, actionable signal that discounting strategy needs review in certain categories
- Product category performance varies significantly in profit even when sales volumes are similar, showing that revenue and profitability are not always the same story

## What I Learned
- How to move from static charts (Tasks 1-3) to a fully **interactive** dashboard that responds live to user input
- How Streamlit turns a plain Python script into a deployable web application with almost no front-end code
- How to design KPIs that summarize a dataset at a glance, and filters that let a user drill into exactly what they care about
- How to use Plotly for interactive charts (hover tooltips, zoom) instead of static images
- How to deploy a data app publicly so anyone — not just someone with the code — can use it
- That a good dashboard doesn't just show data, it should highlight the *"so what"* — which is why I added an auto-generated insights section that responds to the active filters
- Dataset: Superstore Sales dataset (a widely used public dataset for business intelligence and dashboard practice)


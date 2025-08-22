import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from matplotlib.lines import Line2D
import numpy as np

# --- Part 1: Define the CEO Cohort & Data ---
ceo_cohort = [
    {'name': 'Satya Nadella', 'ticker': 'MSFT', 'start_date': '2014-02-04'},
    {'name': 'Sundar Pichai', 'ticker': 'GOOGL', 'start_date': '2015-10-02'},
    {'name': 'Shantanu Narayen', 'ticker': 'ADBE', 'start_date': '2007-12-01'},
    {'name': 'Arvind Krishna', 'ticker': 'IBM', 'start_date': '2020-04-06'},
    {'name': 'Sanjay Mehrotra', 'ticker': 'MU', 'start_date': '2017-05-08'},
    {'name': 'Nikesh Arora', 'ticker': 'PANW', 'start_date': '2018-06-06'},
    {'name': 'Anirudh Devgan', 'ticker': 'CDNS', 'start_date': '2021-12-15'},
    {'name': 'Reshma Kewalramani', 'ticker': 'VRTX', 'start_date': '2020-04-01'},
    {'name': 'Raj Subramaniam', 'ticker': 'FDX', 'start_date': '2022-06-01'},
    {'name': 'Vimal Kapur', 'ticker': 'HON', 'start_date': '2023-06-01'},
    {'name': 'Laxman Narasimhan', 'ticker': 'SBUX', 'start_date': '2023-03-20'}
]
market_ticker = '^GSPC'

# --- Part 2: Calculate Performance for Each CEO ---
print("Analyzing CEO performance...")
performance_results = []

for ceo in ceo_cohort:
    try:
        start_date_dt = datetime.strptime(ceo['start_date'], '%Y-%m-%d')
        tenure_years = (datetime.now() - start_date_dt).days / 365.25

        if tenure_years < 1:
            continue

        company_data = yf.download(ceo['ticker'], start=ceo['start_date'], progress=False, auto_adjust=False)
        market_data = yf.download(market_ticker, start=ceo['start_date'], progress=False, auto_adjust=False)

        if company_data.empty or market_data.empty:
            continue

        # DEFINITIVE FIX: Use .item() to extract the single number from the data cell
        start_price_company = company_data['Adj Close'].iloc[0].item()
        end_price_company = company_data['Adj Close'].iloc[-1].item()
        start_price_market = market_data['Adj Close'].iloc[0].item()
        end_price_market = market_data['Adj Close'].iloc[-1].item()

        cagr_company = ((end_price_company / start_price_company) ** (1 / tenure_years) - 1) * 100
        cagr_market = ((end_price_market / start_price_market) ** (1 / tenure_years) - 1) * 100

        performance_results.append({
            'CEO': f"{ceo['name']} ({ceo['ticker']})",
            'Company CAGR (%)': cagr_company,
            'Market CAGR (%)': cagr_market,
            'Outperformance': cagr_company - cagr_market
        })
    except Exception as e:
        print(f"Could not process data for {ceo['name']}: {e}")

# --- Part 3: Prepare Data and Visualize ---
perf_df = pd.DataFrame(performance_results)
perf_df.dropna(subset=['Outperformance'], inplace=True)

if perf_df.empty:
    print("\nCould not generate plot because no valid CEO performance data was calculated.")
else:
    # Use the simple pandas sort_values, which will now work correctly
    perf_df = perf_df.sort_values('Outperformance', ascending=True)

    print("Generating dumbbell plot...")
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 10))

    for i in range(len(perf_df)):
        row = perf_df.iloc[i]
        ax.plot([row['Market CAGR (%)'], row['Company CAGR (%)']], [i, i], color='grey', zorder=1, linewidth=2)
        ax.scatter(row['Market CAGR (%)'], i, color='#cccccc', s=150, zorder=2)
        ax.scatter(row['Company CAGR (%)'], i, color='#4c00b0', s=150, zorder=2)

    ax.set_yticks(range(len(perf_df)))
    ax.set_yticklabels(perf_df['CEO'], fontsize=12)
    ax.set_xlabel('Compound Annual Growth Rate (%)', fontsize=12)
    ax.set_title('CEO Performance: Company CAGR vs. S&P 500 Benchmark', fontsize=18, weight='bold', pad=20)

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Company CAGR', markerfacecolor='#4c00b0', markersize=12),
        Line2D([0], [0], marker='o', color='w', label='S&P 500 CAGR', markerfacecolor='#cccccc', markersize=12)
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=12)

    ax.axvline(x=0, color='grey', linestyle='--')
    plt.tight_layout()
    plt.show()

print("\nProcess finished.")
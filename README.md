The CEO Alpha Test - Performance of Indian-Origin Leaders 📈

Inspired by a *Newsweek* cover story, this project moves beyond qualitative traits to quantitatively measure the impact of the rising cohort of Indian-origin CEOs in the Fortune 500.

### Key Question Answered ❓
Do companies led by Indian-origin CEOs actually outperform the market?

### Methodology 📝
To ensure a fair, "apples-to-apples" comparison, this analysis uses two key financial metrics:
1.  **Compound Annual Growth Rate (CAGR):** To measure the average annual stock performance, normalizing for different CEO tenure lengths.
2.  **Dynamic S&P 500 Benchmark:** Each CEO is compared against the S&P 500's performance *only during their specific time in the role*.

### Tools and Libraries 🛠️
* **Python:** pandas, Matplotlib, Seaborn
* **Financial Data:** `yfinance` library to automatically fetch historical stock market data.

### Key Insight: A Clear Pattern of Outperformance 💡
The analysis revealed a significant and consistent trend of market outperformance. The dumbbell plot below visualizes this "CEO Alpha." The purple dot (Company CAGR) is consistently to the right of the grey dot (Market CAGR), indicating superior shareholder value creation.

The data shows that **7 out of the 11 leaders** in the cohort beat the market benchmark, with many in the tech sector more than doubling the market's return.

![CEO Performance Dumbbell Plot](https://i.imgur.com/your_image_link_here_2.png)  
*(Note: You will need to upload your "CEO PERFORMANCE.png" image to a service like Imgur and paste the link here)*

### How to Run This Project 🚀
1.  Ensure you have Python installed.
2.  Install the necessary libraries:
    ```bash
    pip install pandas matplotlib seaborn yfinance
    ```
3.  Run the Python script (`ceo_performance_analysis.py`). The script will automatically download the latest financial data and generate the chart.

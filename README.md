# PortfoliX

PortfoliX is a web-based portfolio optimization tool that implements Modern Portfolio Theory (MPT) to help investors create efficient portfolios. Using historical stock data, the application calculates optimal asset allocations to maximize returns while minimizing risk.

## Features

- Interactive web interface built with Streamlit
- Real-time stock data fetching using Yahoo Finance API
- Portfolio optimization using Modern Portfolio Theory
- Monte Carlo simulation for efficient frontier calculation
- Dynamic visualization of the efficient frontier
- Sharpe ratio optimization for optimal portfolio selection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolix.git
cd portfolix
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Dependencies

- numpy
- pandas
- yfinance
- matplotlib
- streamlit

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application through your web browser (typically at `http://localhost:8501`)

3. Enter your portfolio parameters:
   - Input stock tickers separated by commas (e.g., AAPL, MSFT, GOOGL)
   - Select the date range for historical data analysis
   - Click "Optimize Portfolio" to run the analysis

## How It Works

1. **Data Collection**: The application fetches historical stock data from Yahoo Finance for the specified tickers and date range.

2. **Portfolio Optimization**:
   - Calculates daily returns and constructs a covariance matrix
   - Performs Monte Carlo simulation to generate random portfolio weights
   - Computes expected returns, risks, and Sharpe ratios for each portfolio

3. **Visualization**:
   - Plots the efficient frontier showing the risk-return tradeoff
   - Highlights the optimal portfolio with the highest Sharpe ratio
   - Displays detailed statistics and optimal asset allocation

## Output

The application provides:
- Stock price data overview
- Annual returns for each asset
- Covariance matrix
- Optimal portfolio weights
- Expected return, risk, and Sharpe ratio for the optimal portfolio
- Interactive efficient frontier visualization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU v3.0 License.

## Disclaimer

This tool is for educational purposes only. Always conduct thorough research and consult with financial advisors before making investment decisions.

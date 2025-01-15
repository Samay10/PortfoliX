import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit Application Setup
st.title('Portfolio Optimization using Modern Portfolio Theory')
st.write('This app optimizes a portfolio to maximize the Sharpe Ratio and visualizes the Efficient Frontier.')

# Step 1: User Inputs
assets = st.text_input('Enter stock tickers separated by commas (e.g., AAPL, MSFT, GOOGL):')
start_date = st.date_input('Start Date:', value=pd.to_datetime('2020-01-01'))
end_date = st.date_input('End Date:', value=pd.to_datetime('2023-12-31'))

def run_portfolio_optimization():
    # Step 2: Data Collection and Preprocessing
    tickers = [ticker.strip() for ticker in assets.split(',')]
    try:
        # Download stock data from Yahoo Finance
        data = yf.download(tickers, start=start_date, end=end_date)
        
        # Check the available columns
        st.write("Available columns: ", data.columns)
        
        # Check for the 'Close' column and use it
        if 'Close' not in data.columns:
            st.error("Error: 'Close' data is not available for the tickers provided.")
            return

        data = data['Close']  # Use 'Close' prices for portfolio optimization
        st.write('Stock Price Data:')
        st.dataframe(data.head())

        # Calculate daily returns, annual returns, and covariance matrix
        daily_returns = data.pct_change().dropna()
        annual_returns = daily_returns.mean() * 252  # Annualize the returns
        cov_matrix = daily_returns.cov() * 252  # Annualize the covariance matrix

        st.write('Annual Returns:')
        st.write(annual_returns)
        st.write('Covariance Matrix:')
        st.write(cov_matrix)

        # Step 3: Monte Carlo Simulation for Portfolio Optimization
        num_portfolios = 10000
        np.random.seed(42)

        portfolio_returns = []
        portfolio_risks = []
        portfolio_sharpe_ratios = []
        portfolio_weights = []

        for _ in range(num_portfolios):
            weights = np.random.random(len(tickers))
            weights /= np.sum(weights)  # Normalize to sum to 1

            expected_return = np.dot(weights, annual_returns)
            risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            sharpe_ratio = expected_return / risk

            portfolio_returns.append(expected_return)
            portfolio_risks.append(risk)
            portfolio_sharpe_ratios.append(sharpe_ratio)
            portfolio_weights.append(weights)

        # Convert to DataFrame
        portfolios = pd.DataFrame({
            'Return': portfolio_returns,
            'Risk': portfolio_risks,
            'Sharpe Ratio': portfolio_sharpe_ratios
        })

        portfolios['Weights'] = portfolio_weights

        # Identify the Optimal Portfolio
        max_sharpe_idx = portfolios['Sharpe Ratio'].idxmax()
        optimal_portfolio = portfolios.loc[max_sharpe_idx]

        st.write('Optimal Portfolio:')
        st.write(f"Expected Return: {optimal_portfolio['Return']:.2f}")
        st.write(f"Risk (Standard Deviation): {optimal_portfolio['Risk']:.2f}")
        st.write(f"Sharpe Ratio: {optimal_portfolio['Sharpe Ratio']:.2f}")
        st.write('Weights:')
        for ticker, weight in zip(tickers, optimal_portfolio['Weights']):
            st.write(f'{ticker}: {weight:.2%}')

        # Step 4: Visualization
        plt.figure(figsize=(10, 7))
        plt.scatter(portfolios['Risk'], portfolios['Return'], c=portfolios['Sharpe Ratio'], cmap='viridis', alpha=0.7)
        plt.colorbar(label='Sharpe Ratio')
        plt.scatter(optimal_portfolio['Risk'], optimal_portfolio['Return'], color='red', label='Optimal Portfolio', s=100)
        plt.title('Efficient Frontier')
        plt.xlabel('Risk (Standard Deviation)')
        plt.ylabel('Expected Return')
        plt.legend()
        st.pyplot(plt)

        st.write('Efficient Frontier visualization complete.')
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if st.button('Optimize Portfolio'):
    run_portfolio_optimization()

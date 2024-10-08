from strategies.mean_reversion_with_oil import mean_reversion_strategy_with_oil
from utils.data_fetch_with_oil import get_data


# Backtesting function
def backtest():
    stock_data, oil_data = get_data()  # Fetch stock and oil data
    stock_data.reset_index(inplace=True)
    results = mean_reversion_strategy_with_oil(stock_data, oil_data)

    # Calculate the returns based on signals
    results['Returns'] = results['Signal'].shift(1) * results['Close'].pct_change(fill_method=None)
    results['Cumulative Returns'] = (1 + results['Returns']).cumprod()

    # Save backtest results to a file (optional)
    results.to_csv('backtest_results_with_oil.csv', index=False)

    print(results[['Date', 'Close', 'SMA', 'Signal', 'Returns', 'Cumulative Returns']])
    return results

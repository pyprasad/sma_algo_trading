import pandas as pd

def mean_reversion_strategy_with_oil(data, oil_data, window=20, position_size=0.10):
    data['SMA'] = data['Close'].rolling(window=window).mean()
    data['Signal'] = 0

    oil_data['Oil_Change'] = oil_data['Close'].pct_change()

    for i in range(window, len(data)):
        if data['Close'].iloc[i] < data['SMA'].iloc[i] and oil_data['Oil_Change'].iloc[i] > 0:
            data.at[i, 'Signal'] = position_size
        elif data['Close'].iloc[i] > data['SMA'].iloc[i] and oil_data['Oil_Change'].iloc[i] < 0:
            data.at[i, 'Signal'] = -position_size
    return data
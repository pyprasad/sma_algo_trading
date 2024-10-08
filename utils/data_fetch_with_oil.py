import yfinance as yf
import pandas as pd

def get_data():
    stock_data = yf.download("SHEL.L", period='1y', interval='1d')

    oil_data = yf.download('BZ=F', period='1y', interval='1d')

    oil_data = oil_data.ffill()
    return stock_data, oil_data
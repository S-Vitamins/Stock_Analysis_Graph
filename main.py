import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

stock_name = input("Enter a stock: ")   #Enter any ticker/stock name

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=1000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2
data = yf.download(stock_name,
                      start=start_date,
                      end=end_date,
                      progress=False)

#
data['MA50'] = data['Close'].rolling(window=50).mean()  #Moving average with 50 days
data['MA20'] = data['Close'].rolling(window=20).mean()  #Moving average with 20 days

#
import plotly.graph_objects as go

figure = go.Figure(data = [go.Candlestick(x = data.index,
                                        open = data["Open"],
                                        high = data["High"],
                                        low = data["Low"],
                                        close = data["Close"],
                                        showlegend=False)])

figure.add_trace(go.Scatter(x=data.index,
                            y=data['MA50'],
                            opacity=0.6,
                            line=dict(color='blue', width=3),
                            name='Moving Average 50'))
figure.add_trace(go.Scatter(x=data.index,
                            y=data['MA20'],
                            opacity=0.6,
                            line=dict(color='orange', width=3),
                            name='Moving Average 20'))

figure.update_layout(title = "Stock Analysis of " +f'{stock_name}'.upper())
figure.update_layout(title_font_family="Times New Roman")

#
figure.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
            dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
            dict(step = "all")
        ])
    )
)
figure.show()
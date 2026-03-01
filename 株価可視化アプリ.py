import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

days = 20
tickers = {
    'apple': 'AAPL',
    'facebook': 'FB',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():

        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period = f'{days}d')
        hist.index = hist.index.strftime('%Y-%m-%d')
        temp_df = hist[['Close']]
        temp_df.columns = [company]
        df = pd.concat([df, temp_df], axis=1)
        df_pivot = df.T
        df_pivot.index.name ='Name'
    return df, df_pivot

df, df_pivot = get_data(days, tickers)

import altair as alt

# df
companies = ['apple', 'facebook']
# data = df[companies]
# data.sort_index()
# data = data.T.reset_index
# data = data.head()
# data = data.reset_index()
# pd.melt(data, id_vars = ['Date']).rename(
#     columns={'value': 'Stock Prices(USD)'}
# )
# data

# data = df[companies]
# data = data.sort_index()
# data = data.reset_index()
# data = pd.melt(data, id_vars=['Date']).rename(
#     columns={'value': 'Stock Prices(USD)'}
# )

# 45行目〜50行目あたりをこのように修正
data = df[companies]
data = data.sort_index()
data = data.reset_index() 

data = pd.melt(data, id_vars=['Date'], var_name='Name', value_name='Stock Prices(USD)')

st.write(data)

ymin, ymax = 250, 300

chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8, clip=True)
    .encode(
        x="Date:T",
        y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
        color='Name:N'
    )
)

st.altair_chart(chart, use_container_width=True)



# # Altairを使って、もっと細かくグラフをカスタマイズ！
# chart = (
#     alt.Chart(df.reset_index()) # df_pivot ではなく、元の df を使います
#     .mark_line()
#     .encode(
#         x='Date:T',             # 横軸を「時間（Time）」として認識させます
#         y='apple:Q'             # 縦軸を「数値（Quantitative）」として認識させます
#     )
# )
# st.altair_chart(chart, use_container_width=700)


st.write(df_pivot)
st.line_chart(df)



# hist.head(3)

# hist.index = hist.index.strftime('%d %B %Y')
# hist = hist[['Close']]
# hist.columns = ['apple']
# hist.head()

# st.write(hist)
# st.line_chart(hist['Close'])
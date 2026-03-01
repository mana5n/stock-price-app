import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt

st.title('米国株価可視化アプリ')

st.sidebar.write("""
# GAFA株価
こちらは株価可視化ツールです。以下のオプションから表示日数を指定できます。    
""")

st.sidebar.write("""
## 表示日数選択
""")

days = st.sidebar.slider('日数', 1, 50, 20)

st.write (f"""
### 過去 **{days}日間** のGAFA株価
""")

@st.cache_data
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

st.sidebar.write("""
## 株価の範囲指定
""")
ymin, ymax = st.sidebar.slider(
    '範囲を指定してください。',
    0.0, 1000.0, (0.0, 1000.0)
)

tickers = {
    'apple': 'AAPL',
    'meta': 'META',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN',
    'ibm': 'IBM'
}

df, df_pivot = get_data(days, tickers)

companies = st.multiselect(
    '会社名を選択してください。',
    list(df.columns), 
    ['google', 'apple', 'meta', 'amazon']
)

if not companies:
    st.error('少なくとも一社は選んでください')
else:
    data = df[companies]
    st.write("### 株価（USD）", data.sort_index())
    data = data.reset_index() 
    data = pd.melt(data, id_vars=['Date'], var_name='Name', value_name='Stock Prices(USD)')
    chart = (
        alt.Chart(data)
        .mark_line(opacity=0.8, clip=True)
        .encode(
            x="Date:T",
            y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
            color='Name:N'
        )
    )
    st.altair_chart(chart, width='stretch')
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write ('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text, 'です。'

# 'コンディション：', condition 

# st.write('Display Image')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたの数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('Endo_Manami_335-0084のコピー.jpg')
#     st.image(img, caption='Manami Endo', use_container_width=True)


# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70], 
#     columns=['lat', 'lon']
# )
# st.map(df)


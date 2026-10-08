# exapp.py
# Streamlit 앱 제작 및 배포

# python -m streamlit run ./webservice/day31/exapp/exapp.py

import os
import streamlit as st
import random
from dotenv import load_dotenv

DEFAULT_DATA = '치킨'
APP_DATA = os.getenv('APP_GREETING', DEFAULT_DATA)

load_dotenv()

if 'menu' not in st.session_state:
    st.session_state.menu = [DEFAULT_DATA]

st.set_page_config(
    '메뉴 랜덤 뽑기',
    '🍚',
    layout='centered'
)

st.title('🍚메뉴 랜덤 뽑기')
st.subheader('밥을 무엇을 먹을까요?')

with st.form('메뉴입력'):
    menu = st.text_input(
        '메뉴 이름',
        placeholder='저장할 메뉴를 입력하세요'
    )
    if st.form_submit_button('메뉴 저장'):
        if not menu.strip():
            st.error('메뉴를 입력 하세요')
        else:
            st.session_state.menu.append(menu)
            st.success('메뉴를 저장했습니다')


st.subheader('메뉴 랜덤 뽑기')
st.write('버튼을 누르세요')
if st.button('랜덤뽑기'):
    data = st.session_state.menu
    result = random.choice(data)
    st.write(''.join(result))

st.divider()


st.subheader('저장된 메뉴')
st.markdown(','.join(st.session_state.menu))























































































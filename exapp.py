# exapp.py
# Streamlit 앱 제작 및 배포

# python -m streamlit run ./webservice/day31/exapp/exapp.py

import os
import streamlit as st
import random
from dotenv import load_dotenv

DEFAULT_DATA = '돈까스'
APP_DATA = os.getenv('APP_DATA', DEFAULT_DATA)

load_dotenv()

if 'menu' not in st.session_state:
    st.session_state.menu = [DEFAULT_DATA]

st.set_page_config(
    '메뉴 랜덤 뽑기',
    '🍚',
    layout='centered'
)

st.title('🍚오늘의 밥은?')

tab1, tab2 = st.columns(2)

with tab1:
    st.subheader('메뉴 저장')

    menu = st.text_input(
        '메뉴 이름',
        placeholder='저장할 메뉴를 입력하세요'
    )
    if st.button('메뉴 저장'):
        if not menu.strip():
            st.error('메뉴를 입력 하세요')
        else:
            st.session_state.menu.append(menu)
            st.success('메뉴를 저장했습니다')

with tab2:
    st.subheader('메뉴 삭제')

    delete = st.text_input(
        '메뉴 삭제',
        placeholder='삭제할 메뉴를 입력하세요'
    )
    if st.button('메뉴삭제'):
        if delete.strip() in st.session_state.menu:
            st.session_state.menu.remove(delete)
            st.success('메뉴를 삭제했습니다')
        elif delete.strip() not in st.session_state.menu:
            st.error('해당 메뉴가 없습니다')

st.divider()

st.subheader('메뉴 랜덤 뽑기')
st.write('버튼을 누르세요')
if st.button('랜덤뽑기'):
    if len(st.session_state.menu) > 0:
        data = st.session_state.menu
        result = random.choice(data)
        st.balloons()
        st.write(f'오늘의 메뉴: **{''.join(result)}**')
    elif len(st.session_state.menu) <= 0:
        st.warning('메뉴를 먼저 저장하세요')


st.divider()

st.subheader('저장된 메뉴')
st.markdown(','.join(st.session_state.menu))























































































import streamlit as st
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']=key


if 'msg' not in st.session_state: 
	st.session_state.msg = []
st.title("チャットアプリ　by Bard API")
st.write("大規模言語モデルBardのAPIを使用したチャットアプリです。")

with st.form("form", clear_on_submit=False):
    you = st.text_area("**チャットフォーム**")
    submitted = st.form_submit_button("発言")

if submitted:
    result = Bard().get_answer(you)['content']
    st.session_state.msg.append(you)
    st.session_state.msg.append(result)
    st.info("**You :**\n\n"+you+"\n\n**Bard :**\n\n"+result)

    t = 0

    st.title("チャット履歴")

    for ms in st.session_state.msg:
        if t == 0:
            st.warning("**You :**\n\n"+ms)
            t = 1
        elif t == 1:
            st.success("**Bard :**\n\n"+ms)
            t = 0

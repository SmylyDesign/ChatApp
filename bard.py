import streamlit as st
from bardapi import Bard
import os
import requests

os.environ['_BARD_API_KEY']="YQjwnpshqJiWsojbrLKeDWf_6CBdhri2wUIItVfkwAzPRVcfAAWlqDM15r5EkNmSYV8Vaw."
token = "YQjwnpshqJiWsojbrLKeDWf_6CBdhri2wUIItVfkwAzPRVcfAAWlqDM15r5EkNmSYV8Vaw."

session = requests.Session()

 
session.headers = {
"Host": "bard.google.com",
"X-Same-Domain": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
"Origin": "https://bard.google.com",
"Referer": "https://bard.google.com/",
}

session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
 
bard = Bard(token=token, session=session, timeout=30)


if 'msg' not in st.session_state: 
	st.session_state.msg = []
st.title("チャットアプリ　by Bard API")
st.write("大規模言語モデルBardのAPIを使用したチャットアプリです。")

with st.form("form", clear_on_submit=False):
    you = st.text_area("**チャットフォーム**")
    submitted = st.form_submit_button("発言")

if submitted:
    result = bard.get_answer(you)['content']
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

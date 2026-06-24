import time

import streamlit as st
from agent.react_agent import ReactAgent

# 标题
st.title("向楠扫地机器人智能客服")
st.divider()

if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

if "message" not in st.session_state:
    st.session_state["message"] = []


for message in st.session_state["message"]:  #历史读取消息
    st.chat_message(message["role"]).write(message["content"])
# 用户输入提示词
prompt = st.chat_input()

if prompt:
    st.chat_message("user").write(prompt) # 加载用户消息气泡
    st.session_state["message"].append({"role": "user", "content" : prompt})  #保存到历史

    response_messages = []
    with st.spinner("智能客服思考中...."):
        res_stream = st.session_state["agent"].execute_stream(prompt)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:
                    time.sleep(0.01)
                    yield char

        st.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        st.session_state["message"].append({"role": "assistant", "content" : response_messages[-1]})
        st.rerun()

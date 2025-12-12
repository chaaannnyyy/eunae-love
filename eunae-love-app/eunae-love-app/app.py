import streamlit as st
import random

st.set_page_config(page_title="은애 사랑 측정기 💖", page_icon="💘", layout="centered")

st.title("💝 은애를 얼마나 사랑하나요?")
st.write("👇 버튼을 눌러 오늘의 사랑 지수를 확인해보세요!")

if st.button("사랑 측정하기 💌"):
    level = random.choice([f"{random.randint(101, 300)}%", "∞"])
    st.markdown(f"## 💖 당신은 은애를 **{level}** 만큼 사랑합니다!")

    if level == "∞":
        st.success("세상 끝까지 사랑하는 중입니다. 💘")
    else:
        st.balloons()
        st.info("매일 더 사랑하게 되는 중이에요 💕")

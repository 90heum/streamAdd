import streamlit as st


st.set_page_config(page_title="더하기 / 빼기", page_icon="T", layout="wide")

st.title("간단한 더하기 / 빼기")
st.write("두 숫자를 입력하고 연산을 선택하세요.")

st.sidebar.header("info")
st.sidebar.write("내가만든 앱을 다른 스트림릿템플릿으로 옮긴버전.")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("입력")
    number_a = st.number_input("숫자 A", value=0, step=1)
    number_b = st.number_input("숫자 B", value=0, step=1)
    operation = st.radio(
        "연산",
        options=["add", "sub"],
        format_func=lambda value: "더하기 (+)" if value == "add" else "빼기 (-)",
    )
    calculate = st.button("계산하기", use_container_width=True)

with col_right:
    st.subheader("결과")
    if calculate:
        if operation == "add":
            result = number_a + number_b
        else:
            result = number_a - number_b
        st.success(f"결과: {result}")
    else:
        st.write("아직 결과가 없습니다.")

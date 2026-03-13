import streamlit as st


st.set_page_config(page_title="Add / Subtract", page_icon="T", layout="wide")

st.title("간단한 더하기 빼기 앱")
st.write("Enter two numbers and choose an operation.")

st.sidebar.header("About")
st.sidebar.write("This is the Streamlit version of your console app.")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("입력")
    number_a = st.number_input("숫자입력 A", value=0.0, step=1.0)
    number_b = st.number_input("숫자입력 B", value=0.0, step=1.0)
    operation = st.radio("선택", ("더하기 (+)", "빼기 (-)"))
    calculate = st.button("실행", use_container_width=True)

with col_right:
    st.subheader("결과")
    if calculate:
        if operation.startswith("Add"):
            result = number_a + number_b
        else:
            result = number_a - number_b
        st.success(f"Result: {result}")
    else:
        st.write("No result yet.")

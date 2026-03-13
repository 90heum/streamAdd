import streamlit as st


st.set_page_config(page_title="Add / Subtract", page_icon="T", layout="wide")

st.title("Simple Add / Subtract")
st.write("Enter two numbers and choose an operation.")

st.sidebar.header("About")
st.sidebar.write("This is the Streamlit version of your console app.")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Inputs")
    number_a = st.number_input("Number A", value=0.0, step=1.0)
    number_b = st.number_input("Number B", value=0.0, step=1.0)
    operation = st.radio("Operation", ("Add (+)", "Subtract (-)"))
    calculate = st.button("Calculate", use_container_width=True)

with col_right:
    st.subheader("Result")
    if calculate:
        if operation.startswith("Add"):
            result = number_a + number_b
        else:
            result = number_a - number_b
        st.success(f"Result: {result}")
    else:
        st.write("No result yet.")

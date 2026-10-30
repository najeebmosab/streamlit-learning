import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("اكتب اسمك")

if st.button("اعرض الترحيب"):
    if name:
        st.success(f"أهلًا {name}")
    else:
        st.warning("اكتب اسمك أولًا")

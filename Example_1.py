import streamlit as st

st.title("My First Streamlit App")

age = st.slider("اختَر عمرك", min_value=0, max_value=100, value=25)
st.write("العمر الذي اخترته:", age)

city = st.selectbox(
    "اختَر مدينتك",
    ["القدس", "رام الله", "نابلس"]
)
st.write("المدينة التي اخترتها:", city)

name = st.text_input("اكتب اسمك")
if st.button("اعرض الترحيب"):
    if name:
        st.success(f"أهلًا {name}")
    else:
        st.warning("اكتب اسمك أولًا")

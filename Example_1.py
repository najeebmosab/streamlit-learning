import streamlit as st
from PIL import Image
st.title("My First Streamlit App")

age = st.slider("اختَر عمرك", min_value=0, max_value=100, value=25)
st.write("العمر الذي اخترته:", age)

city = st.selectbox(
    "اختَر مدينتك",
    ["القدس", "رام الله", "نابلس"]
)
st.write("المدينة التي اخترتها:", city)


st.header("رفع صورة")

uploaded_file = st.file_uploader(
    "اختَر صورة",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="الصورة المرفوعة")

    st.write("العرض:", image.width)
    st.write("الارتفاع:", image.height)
    st.write("نمط الألوان:", image.mode)

    st.subheader("تغيير أبعاد الصورة")

    new_width = st.slider("العرض الجديد", 50, 500, 200)
    new_height = st.slider("الارتفاع الجديد", 50, 500, 200)

    resized_image = image.resize((new_width, new_height))

    st.image(resized_image, caption="الصورة بعد تغيير الأبعاد")

    st.write("الأبعاد الجديدة — عرض، ارتفاع:", resized_image.size)
    
name = st.text_input("اكتب اسمك")
if st.button("اعرض الترحيب"):
    if name:
        st.success(f"أهلًا {name}")
    else:
        st.warning("اكتب اسمك أولًا")

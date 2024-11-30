#import streamlit as st

# NO 1
# st.write("Hello World")

# NO 2
# st.header("st.button")

# if st.button("Say Hello"):
#     st.write("Why Hello there")
# else:
#     st.write("Goodbye")


# NO 3
# st.title("This is the app title")
# st.header("This is the markdown")
# st.markdown("This is the header")
# st.subheader("This is the subheader")
# st.caption("this is the caption")

# st.code("x=233")

# NO 4
# st.checkbox("yes")
# st.button("Click")
# gender = st.radio("Pick your gender", options=["Male", "Female"])
# gender_select = st.selectbox("Pick your gender", options=["Male", "Female"])
# planet = st.selectbox("choose a planet", options=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
# mark = st.slider("Pick a mark", min_value=0, max_value=100, value=50)
# st.write("Bad", " " * 50, "Good", " " * 50, "Excellent") 
# number = st.slider("Pick a number", min_value=0, max_value=50, value=10)

# NO 5
# st.number_input('Pick a number', 0, 10)
# st.text_input('Email adress')
# st.date_input('Travelling date')
# st.time_input('School time')
# st.text_area('Description')
# st.file_uploader('Upload a photo')
# st.color_picker('Choose your favourite color')

# NO 6
# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('st.write')
# st.write('Hello, *World !* :sunglasses:')
# st.write(1234)

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

# st.write(df)

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# df2 = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a' , 'b' , 'c'])   
# st.write(c)

# NO 7
# import streamlit as st
# import pandas as pd
# import numpy as np

# df= pd.DataFrame(
# np.random.randn(10, 2),
# columns=['x', 'y'])

# # Line Chart
# st.write("### Line Chart")
# st.line_chart(df)

# # Bar Chart
# st.write("### Bar Chart")
# st.bar_chart(df)

# # Area Chart
# st.write("### Area Chart")
# st.area_chart(df)

# NO 8
# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle
# import base64

# @st.cache(suppress_st_warning=True)
# def get_fvalue(val):
#     feature_dict = {"No":1,"Yes":2}
#     for key, value in feature_dict.items():
#         if val == key:
#             return value

# def get_value(val,my_dict):
#     for key,value in my_dict.items():
#         if val == key:
#          return value

# app_mode = st.sidebar.selectbox('Select Page', ['Home','Prediction'])
# if app_mode == 'Home':
#     st.title('LOAN PREDICTION :')
#     st.write('App realised by : Nadia Mhadhbi')
#     st.image('loan_image.jpeg')
#     st.markdown('Dataset :')
#     data=pd.read_csv('loan_dataset.csv')
#     st.write(data.head())
#     st.markdown('Applicant Income VS Loan Amount ')
#     st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))


# NO 9
# import pickle
# filename = "CarPrice_Assignment.csv"
# pickle.dump(model_regresi, open(filename, "wb"))

# NO 10
# import pickle
# import streamlit as st
# import pandas as pd
# import numpy as np
# import altair as alt

# # Load model yang sudah disimpan
# model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

# # Judul aplikasi
# st.title('Prediksi Harga Mobil')

# # Bagian 1: Menampilkan Dataset
# st.header("Dataset")
# # Membuka file CSV
# df1 = pd.read_csv('CarPrice.csv')
# st.dataframe(df1)

# # Reset index untuk grafik jika diperlukan
# df1.reset_index(inplace=True)

# # Bagian 2: Menampilkan Grafik
# st.write("Grafik Highway-mpg")
# chart_highwaympg = alt.Chart(df1).mark_line().encode(
#     x='index:Q',  
#     y='highwaympg:Q'
# )
# st.altair_chart(chart_highwaympg, use_container_width=True)

# st.write("Grafik Curbweight")
# chart_curbweight = alt.Chart(df1).mark_line().encode(
#     x='index:Q',
#     y='curbweight:Q'
# )
# st.altair_chart(chart_curbweight, use_container_width=True)

# st.write("Grafik Horsepower")
# chart_horsepower = alt.Chart(df1).mark_line().encode(
#     x='index:Q',
#     y='horsepower:Q'
# )
# st.altair_chart(chart_horsepower, use_container_width=True)

# # Bagian 3: Input untuk Prediksi
# st.header("Input Nilai untuk Prediksi")
# # Input variabel independent
# highwaympg = st.number_input("Highway-mpg", min_value=0, max_value=100, step=1, value=30)
# curbweight = st.number_input("Curbweight", min_value=0, max_value=5000, step=10, value=2000)
# horsepower = st.number_input("Horsepower", min_value=0, max_value=1000, step=10, value=150)

# # Bagian 4: Tombol Prediksi
# if st.button('Prediksi'):
#     try:
#         # Prediksi variabel yang telah diinputkan
#         car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
        
#         # Konversi hasil prediksi ke format string
#         harga_mobil_float = float(car_prediction[0])
#         harga_mobil_formatted = f"Rp {harga_mobil_float:,.2f}"  # Format dalam bentuk mata uang
        
#         # Tampilkan hasil prediksi
#         st.success(f"Harga Mobil yang Diprediksi: {harga_mobil_formatted}")
#     except Exception as e:
#         st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")


# NO 11
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import base64

# Load model yang sudah disimpan
model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

# Sidebar untuk navigasi
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Dataset", "Visualisasi", "Prediksi"])

# Home Page
if menu == "Home":
    st.title("Aplikasi Prediksi Harga Mobil")
    st.image("mobil_example.jpg", caption="Contoh Mobil", use_column_width=True)
    st.markdown("""
    ### Tentang Aplikasi
    Aplikasi ini menggunakan model Machine Learning untuk memprediksi harga mobil berdasarkan beberapa fitur penting:
    - **Highway-mpg**: Efisiensi bahan bakar di jalan raya.
    - **Curbweight**: Berat kendaraan.
    - **Horsepower**: Tenaga mesin kendaraan.
    
    ### Cara Menggunakan
    1. Navigasikan ke menu **Dataset** untuk melihat data.
    2. Lihat grafik di menu **Visualisasi**.
    3. Gunakan menu **Prediksi** untuk melakukan prediksi harga mobil.
    """)
    st.success("Aplikasi siap digunakan!")

# Dataset Page
if menu == "Dataset":
    st.title("Dataset Harga Mobil")
    # Load dataset
    df1 = pd.read_csv('CarPrice.csv')
    
    # Opsi untuk memilih kolom yang ditampilkan
    selected_columns = st.multiselect("Pilih Kolom untuk Ditampilkan", df1.columns.tolist(), default=df1.columns.tolist())
    st.dataframe(df1[selected_columns])

    # Filter dataset
    st.subheader("Filter Dataset")
    min_price = st.slider("Minimum Price", int(df1["price"].min()), int(df1["price"].max()), int(df1["price"].min()))
    filtered_data = df1[df1["price"] >= min_price]
    st.write(f"Menampilkan data dengan harga di atas Rp {min_price:,}")
    st.dataframe(filtered_data)

# Visualisasi Page
if menu == "Visualisasi":
    st.title("Visualisasi Data")
    df1 = pd.read_csv('CarPrice.csv')

    # Pilihan grafik
    st.write("Pilih jenis grafik untuk ditampilkan:")
    chart_type = st.radio(
        "Pilih Grafik",
        ["Line Chart", "Bar Chart", "Scatter Plot"]
    )

    if chart_type == "Line Chart":
        st.line_chart(df1[['highwaympg', 'curbweight', 'horsepower']])
    elif chart_type == "Bar Chart":
        st.bar_chart(df1[['highwaympg', 'curbweight', 'horsepower']])
    elif chart_type == "Scatter Plot":
        scatter_chart = alt.Chart(df1).mark_circle(size=60).encode(
            x='horsepower:Q',
            y='price:Q',
            color='fueltype:N',
            tooltip=['horsepower', 'price', 'fueltype']
        ).interactive()
        st.altair_chart(scatter_chart, use_container_width=True)

# Prediksi Page
if menu == "Prediksi":
    st.title("Prediksi Harga Mobil")
    st.write("Masukkan nilai untuk fitur berikut:")

    # Input untuk prediksi
    highwaympg = st.slider("Highway-mpg", min_value=0, max_value=100, value=30)
    curbweight = st.slider("Curbweight", min_value=0, max_value=5000, value=2000)
    horsepower = st.slider("Horsepower", min_value=0, max_value=1000, value=150)

    # Prediksi berdasarkan input
    if st.button("Prediksi"):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
        harga_mobil_float = float(car_prediction[0])
        harga_mobil_formatted = f"Rp {harga_mobil_float:,.2f}"  # Format mata uang
        st.success(f"Harga Mobil yang Diprediksi: {harga_mobil_formatted}")

        # Opsi untuk mengunduh hasil prediksi
        hasil_prediksi = pd.DataFrame({
            "Highway-mpg": [highwaympg],
            "Curbweight": [curbweight],
            "Horsepower": [horsepower],
            "Predicted Price": [harga_mobil_float]
        })
        csv = hasil_prediksi.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # encode to base64
        href = f'<a href="data:file/csv;base64,{b64}" download="hasil_prediksi.csv">Klik di sini untuk mengunduh hasil prediksi</a>'
        st.markdown(href, unsafe_allow_html=True)

import pickle #untuk model
import streamlit as st

#membaca model (load model)
kelayakan_model = pickle.load(open('kelayakan_model.sav','rb'))

#Judul web
st.title("Water Quality Classification")

ph = st.text_input('Masukkan nilai pH')

Hardness = st.text_input('Masukkan nilai Hardness')

Solids = st.text_input('Masukkan nilai Solids')

Chloramines = st.text_input('Masukkan nilai Chloramines')

Sulfate = st.text_input('Masukkan nilai Sulfate')

Conductivity = st.text_input('Masukkan nilai Conductivity')

Organic_carbon = st.text_input('Masukkan nilai Organic carbon')

Trihalomethanes = st.text_input('Masukkan nilai Trihalomethanes')

Turbidity = st.text_input('Masukkan nilai Turbidity')

#code untuk prediksi kelayakan
layak_kah = ""

#membuat button untuk prediksi
if st.button('Test Kelayakan Air Minum') :
    layak_prediction = kelayakan_model.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    
    if(layak_prediction[0] == 1):
        layak_kah = "Air Layak Minum"
    else :
        layak_kah = "Air Tidak Layak Minum"
    st.success(layak_kah)
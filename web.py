import streamlit as st
import pickle
import time

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Rainfall Prediction App",
    page_icon="🌧",
    layout="centered"
)

# ---------------- LOADING ANIMATION ----------------
with st.spinner("Loading Rainfall Prediction Model..."):
    time.sleep(2)
    model = pickle.load(open("rainfall_model.pkl", "rb"))

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'>🌧 Rainfall Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Enter weather details to predict rainfall</p>",
    unsafe_allow_html=True
)

st.write("")

# ---------------- INPUT FORM ----------------
with st.form("rain_form"):

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=38.0,
        value=None,
        placeholder="Enter temperature"
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=90.0,
        value=None,
        placeholder="Enter humidity"
    )

    windspeed = st.number_input(
        "Wind Speed",
        min_value=0.0,
        max_value=29.0,
        value=None,
        placeholder="Enter wind speed"
    )

    pressure = st.number_input(
        "Pressure",
        min_value=900.0,
        max_value=1024.0,
        value=None,
        placeholder="Enter pressure"
    )

    submit = st.form_submit_button("🔍 Predict Rainfall")

# ---------------- PREDICTION ----------------
if submit:

    if None in (temperature, humidity, windspeed, pressure):
        st.warning("⚠ Please enter all values")
    else:
        with st.spinner("Analyzing weather data..."):
            time.sleep(1.5)
            prediction = model.predict(
                [[temperature, humidity, windspeed, pressure]]
            )

        # RESULT DISPLAY
        if prediction[0] == 1 or prediction[0] == "Yes":
            st.success("🌧 Rain Expected")
        else:
            st.info("☀ No Rain Expected")
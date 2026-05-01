import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('crop_model.pk1', 'rb'))


st.set_page_config(page_title="AgriSmart Predictor", page_icon="🌱")


st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


st.title("🌱 Smart Agriculture Advisor")
st.markdown("---")


col1, col2, col3 = st.columns(3)

with col1:
    n = st.number_input("Nitrogen (N)", min_value=0, help="Amount of Nitrogen in soil")
    temp = st.number_input("Temperature (°C)", format="%.2f")

with col2:
    p = st.number_input("Phosphorus (P)", min_value=0, help="Amount of Phosphorus in soil")
    hum = st.number_input("Humidity (%)", format="%.2f")

with col3:
    k = st.number_input("Potassium (K)", min_value=0, help="Amount of Potassium in soil")
    ph = st.number_input("Soil pH", format="%.2f", value=6.5)

rain = st.slider("Rainfall (mm)", 0.0, 500.0, 100.0)


crop_info = {
    "RICE": "High water requirement. Best grown in clayey soil with good water retention.",
    "MAIZE": "Requires well-drained fertile soil. Ensure proper spacing between rows.",
    "CHICKPEA": "Grows best in cool climates with moderate rainfall. Avoid waterlogging.",
    "KIDNEYBEANS": "Prefers warm weather and regular watering during the flowering stage.",
    "PIGEONPEAS": "Drought-tolerant crop. Thrives in tropical and subtropical climates.",
    "COTTON": "Requires high temperature and moderate rainfall. Pick during dry weather."
}

st.markdown("---")
if st.button("Analyze Soil & Recommend"):
    features = np.array([[n, p, k, temp, hum, ph, rain]])
    prediction = model.predict(features)[0].upper()
    
    
    st.balloons()
    st.success(f"### Recommended Crop: {prediction}")
    

    advice = crop_info.get(prediction, "Great choice! Follow standard agricultural practices for your region.")
    st.info(f"**Expert Advice:** {advice}")
    
    
    if ph < 5.5:
        st.warning("⚠️ Your soil is quite acidic. Consider adding lime to balance the pH.")
    elif ph > 7.5:
        st.warning("⚠️ Your soil is alkaline. Consider adding organic matter or sulfur.")
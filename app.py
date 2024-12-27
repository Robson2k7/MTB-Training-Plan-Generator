import streamlit as st
from tweaks import generate_tweaks
from api import run_flow

# Tytuł aplikacji
st.title("MTB Training Plan Generator")
st.write("Wprowadź swoje preferencje, aby wygenerować plan treningowy MTB.")

# Dane wejściowe od użytkownika
level = st.selectbox("Poziom trudności", ["Początkujący", "Średniozaawansowany", "Zaawansowany"])
days = st.slider("Liczba dni treningowych w tygodniu", min_value=1, max_value=7, value=3)
distance = st.number_input("Tygodniowy dystans (km)", min_value=10, value=50)
terrain = st.selectbox("Rodzaj terenu", ["Górzysty", "Leśny", "Miejski", "Mieszany"])

# Przyciski
if st.button("Generuj Plan"):
    try:
        tweaks = generate_tweaks(level, days, distance, terrain)
        result = run_flow(message="Generuj plan treningowy MTB", tweaks=tweaks)
        
        st.subheader("Wygenerowany plan treningowy:")
        st.markdown(result["response"])

    except Exception as e:
        st.error(f"Błąd: {e}")

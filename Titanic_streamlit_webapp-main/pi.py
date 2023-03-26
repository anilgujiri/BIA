
import streamlit as st

def input_value():
    st.title("Titanic Survival Prediction")
    st.write(""" Would you have survived the Titanic Disaster?""")

    st.write("""How it's working:""")

    st.title("--- Check Your Survival Chances ---")

    age = st.slider("Enter Age :", 1, 75, 30)

    input = {"Age": age,}

    return age


# def predict(df):
data = input_value()
st.write(data)
import streamlit as st

st.title("BMI Calculator")

st.write("Enter your height and weight  to calculater your BMI")

height = st.number_input("Enter your height in cm", min_value=0.5, max_value=3.0, value=1.5)

weight = st.number_input("Enter your weight in kg", min_value=10, max_value=90, value=70)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0 :
       bmi = weight / (height ** 2)
       st.success(f"Your BMI is {bmi:.2f}")

       if bmi < 18.5:
           st.warning("you are underweight.")
       elif bmi < 24.9:
           st.success("you have a normal weight")
       elif bmi < 29.9:
           st.warning("you are overweight.")
       else:
           st.error("you are obese ")
           


    else:
        st.error("Please enter valid height and weight")
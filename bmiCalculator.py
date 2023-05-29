import streamlit as st

st.markdown("<h1 style="
            "'text-align: center;'>BMI CALCULATOR"
            "</h1>",
            unsafe_allow_html=True)

st.write("---")

# BMI formula => kg / m^2

weight = st.number_input("Enter your weight: ")
st.write("Your weight: ", weight, "kg")

st.write("")
st.write("")
st.write("")

height = st.number_input("Enter your height: ")
heightUnit = st.radio("Height unit", ('cm', 'm', 'ft'))
st.write("Your height: ", height, heightUnit)

st.write("---")

if heightUnit == 'cm':
    height = height / 100
    # conversion from cm => m

    if st.button("Calculate BMI"):

        bmi = weight / height ** 2
        formatted_string = "{:.2f}".format(bmi)
        # format to two decimal places

        float_bmi = float(formatted_string)
        st.write("Your BMI index: ", float_bmi)

        if bmi < 18.5:
            st.error("Underweight :heavy_exclamation_mark:")
        elif bmi < 25:
            st.success("Normal :100:")
        elif bmi < 30:
            st.warning("Overweight :grey_exclamation:")
        else:
            st.error("Obese :heavy_exclamation_mark:")

elif heightUnit == 'm':

    if st.button("Calculate BMI"):

        bmi = weight / height ** 2
        formatted_string = "{:.2f}".format(bmi)
        # format to two decimal places

        float_bmi = float(formatted_string)
        st.write("Your BMI index: ", float_bmi)

        if bmi < 18.5:
            st.error("Underweight :heavy_exclamation_mark:")
        elif bmi < 25:
            st.success("Normal :100:")
        elif bmi < 30:
            st.warning("Overweight :grey_exclamation:")
        else:
            st.error("Obese :heavy_exclamation_mark:")

elif heightUnit == 'ft':
    height = height / 3.28
    # conversion from ft => m

    if st.button("Calculate BMI"):

        bmi = weight / height ** 2
        formatted_string = "{:.2f}".format(bmi)
        # format to two decimal places

        float_bmi = float(formatted_string)
        st.write("Your BMI index: ", float_bmi)

        if bmi < 18.5:
            st.error("Underweight :heavy_exclamation_mark:")
        elif bmi < 25:
            st.success("Normal :white_check_mark:")
        elif bmi < 30:
            st.warning("Overweight :grey_exclamation:")
        else:
            st.error("Obese :heavy_exclamation_mark:")

st.write("---")

st.markdown(
    """
    <style>
    
    .edgvbvh10{
        background-color: lightcoral;
        display: flex;
        margin: auto;
        color: white;
    }
    
    code {
        font-size: 16px;
        color: red;
    }    
    </style>
    """,
    unsafe_allow_html=True
)

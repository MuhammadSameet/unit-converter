import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp{
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    }
   
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #32fe9d, #00c9ff);
        color: white;
    }
    .result-box{
        font-size: 20px;
        text-align: center;
        font-weight: bold;
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center;
        margin-top: 20px;
        color: black;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True

)
# Title and subheader

st.markdown("<h1> unit converter using Python and streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between diffrent units of length, weight, temperature, and more.")


#sidebar manu
conversion_type = st.sidebar.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", min_value=0.0, value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters" ,  "Centimeters" , "Milimeters" , "Miles" , "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters" ,  "Centimeters" , "Milimeters" , "Miles" , "Yards", "Inches", "Feet"] )        

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["kilogram", "Gram", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["kilogram", "Gram", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From" , ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#converted function

def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'kilometers': 0.001, 'centimeters':100, 'Millimeters': 1000,
        'Miles':0.000621371, 'Yards': 1.09636, 'Feet': 3.28, 'Inches': 39.37
    }
    return(value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value , from_unit, to_unit):
    weight_units = {
        'kilogram':1 , 'Gram': 1000, 'Milligrams': 1000000, 'Pounds': 2.2046, 'Ounces':35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def tem_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return(value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value




    # button for conversion 
if st.button("Convert"):
    result = None
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = tem_converter(value, from_unit, to_unit)
    if result is not None:
        st.markdown(f"<div class='result-box'> {value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)



st.markdown("<div class='footer'>Developed by <a href='https://www.linkedin.com/in/muhammad-sameet-shahid/'>@SameetShahid</a></div>", unsafe_allow_html=True)

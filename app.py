import streamlit as st
import math
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="Gann & Fibonacci Calculator", layout="wide")

st.title("📈 Trading Calculator: Gann & Fibonacci")
st.write("Dhaval, yeh aapka customized trading tool hai.")

# --- SIDEBAR: Input Fields ---
st.sidebar.header("User Inputs")
calculation_type = st.sidebar.selectbox("Choose Calculator", ["Gann Degrees", "Gann Date", "Fibonacci Levels"])

# --- FUNCTIONALITY 1: Gann Degrees ---
if calculation_type == "Gann Degrees":
    st.header("🎯 Gann Square of 9 (Degrees)")
    price = st.number_input("Enter Current Price", min_value=1.0, value=18000.0, step=1.0)
    
    if st.button("Calculate Gann Levels"):
        degrees = [45, 90, 180, 270, 360]
        root = math.sqrt(price)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Resistance (Upper)")
            for d in degrees:
                res = (root + (d/180))**2
                st.success(f"{d}° Resistance: {res:.2f}")
                
        with col2:
            st.subheader("Support (Lower)")
            for d in degrees:
                sup = (root - (d/180))**2
                st.error(f"{d}° Support: {sup:.2f}")

# --- FUNCTIONALITY 2: Gann Date Calculator ---
elif calculation_type == "Gann Date":
    st.header("📅 Gann Time Cycle Calculator")
    base_date = st.date_input("Select Important Pivot Date (High/Low Date)", datetime.now())
    
    if st.button("Calculate Gann Dates"):
        # Gann's key degree cycles converted to days
        cycles = {"45°": 45, "90°": 90, "180°": 180


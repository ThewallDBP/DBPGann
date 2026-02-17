import streamlit as st
import math
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="Gann & Fibonacci Calculator", layout="wide")

st.title("📈 Trading Calculator: Gann & Fibonacci")
st.write("Dhaval, yeh aapka updated aur fixed trading tool hai.")

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
        # Fixed: Bracket properly closed here
        cycles = {
            "45° Cycle": 45, 
            "90° Cycle": 90, 
            "180° Cycle": 180, 
            "270° Cycle": 270, 
            "360° Cycle (1 Year)": 365
        }
        
        st.write("Upcoming Trend Change Dates:")
        for label, days in cycles.items():
            future_date = base_date + timedelta(days=days)
            st.info(f"**{label}:** {future_date.strftime('%d-%b-%Y')}")

# --- FUNCTIONALITY 3: Fibonacci Levels ---
elif calculation_type == "Fibonacci Levels":
    st.header("🔢 Fibonacci Retracement")
    col_f1, col_f2 = st.columns(2)
    high_p = col_f1.number_input("Recent High", value=18500.0)
    low_p = col_f2.number_input("Recent Low", value=17500.0)
    
    if st.button("Calculate Fibonacci"):
        diff = high_p - low_p
        # Standard Fibonacci Ratios
        levels = {
            "0.0% (High)": high_p,
            "23.6%": high_p - (diff * 0.236),
            "38.2%": high_p - (diff * 0.382),
            "50.0% (Pivot)": high_p - (diff * 0.5),
            "61.8% (Golden Pocket)": high_p - (diff * 0.618),
            "78.6%": high_p - (diff * 0.786),
            "100.0% (Low)": low_p
        }
        
        for level, val in levels.items():
            st.write(f"**{level}:** {val:.2f}")

st.markdown("---")
st.caption("Developed for personal trading analysis.")


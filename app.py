import streamlit as st
import math
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="Gann & Fibonacci Tool", layout="wide")

st.title("📈 Advanced Trading")
st.write("Dhaval")

# --- SIDEBAR: Navigation ---
st.sidebar.header("Select Tool")
tool = st.sidebar.radio("Navigate to:", ["Gann Degrees", "Gann Date Pro", "Fibonacci Retracement & Extension"])

# --- 1. GANN DEGREES ---
if tool == "Gann Degrees":
    st.header("🎯 Gann Degree Levels (Support & Resistance)")
    price = st.number_input("Enter LTP (Last Traded Price)", min_value=1.0, value=22000.0)
    
    if st.button("Calculate Gann"):
        degrees = [45, 90, 180, 270, 360]
        root = math.sqrt(price)
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Resistance (Upper)")
            for d in degrees:
                res = (root + (d/180))**2
                st.success(f"{d}° Resistance: {res:.2f}")
        with c2:
            st.subheader("Support (Lower)")
            for d in degrees:
                sup = (root - (d/180))**2
                st.error(f"{d}° Support: {sup:.2f}")

# --- 2. GANN DATE PRO ---
elif tool == "Gann Date Pro":
    st.header("📅 Gann Time Cycle (Trend Change Dates)")
    base_date = st.date_input("Select Trend Pivot Date", datetime.now())
    
    if st.button("Generate Dates"):
        cycles = {"45 Days": 45, "90 Days": 90, "144 Days (Fib/Gann)": 144, "180 Days": 180, "365 Days": 365}
        for label, days in cycles.items():
            dt = base_date + timedelta(days=days)
            st.info(f"**{label}:** {dt.strftime('%d-%b-%Y')}")

# --- 3. FIBONACCI RETRACEMENT & EXTENSION ---
elif tool == "Fibonacci Retracement & Extension":
    st.header("🔢 Fibonacci Levels")
    col_a, col_b = st.columns(2)
    high = col_a.number_input("Swing High", value=22500.0)
    low = col_b.number_input("Swing Low", value=21500.0)
    
    if st.button("Calculate Fibonacci"):
        diff = high - low
        # Levels dictionary
        fib_levels = {
            "0.0% (High)": high,
            "23.6%": high - (diff * 0.236),
            "38.2%": high - (diff * 0.382),
            "50.0% (Median)": high - (diff * 0.5),
            "61.8% (Golden Ratio)": high - (diff * 0.618),
            "78.6%": high - (diff * 0.786),
            "100.0% (Low)": low,
            "161.8% (Extension)": high + (diff * 0.618)
        }
        
        
        
        for k, v in fib_levels.items():
            if "Golden" in k or "161.8%" in k:
                st.warning(f"**{k}: {v:.2f}**")
            else:
                st.write(f"{k}: {v:.2f}")

st.markdown("---")
st.caption("Custom built for Dhaval | Indian Market Analysis")




import streamlit as st
import math

# UI Header
st.set_page_config(page_title="Gann Square Calculator", page_icon="📈")
st.title("🏹 Gann Square of 9")
st.subheader("Support & Resistance Calculator")

# User Input
price = st.number_input("Enter Stock Price (e.g., ITC 313.75)", min_value=1.0, value=313.75)

if price:
    sqrt_price = math.sqrt(price)
    degrees = {"90°": 0.5, "180°": 1.0, "270°": 1.5, "360°": 2.0}
    
    st.write("---")
    
    # Columns for clean layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🟢 Resistance")
        for label, factor in degrees.items():
            res = (sqrt_price + factor) ** 2
            st.metric(label, f"₹{res:.2f}")

    with col2:
        st.write("### 🔴 Support")
        for label, factor in degrees.items():
            sup = (sqrt_price - factor) ** 2
            st.metric(label, f"₹{sup:.2f}")

st.info("Pro Tip: 180° and 360° are the strongest reversal points.")
import streamlit as st
import math
from datetime import timedelta, date

st.title("🏹 Dhaval's Gann Date & Price Pro")

# --- SECTION 1: PRICE CALCULATOR ---
price = st.number_input("Enter Current Price", min_value=1.0, value=313.75)
if price:
    sqrt_p = math.sqrt(price)
    # Price targets
    res_180 = (sqrt_p + 1.0)**2
    sup_180 = (sqrt_p - 1.0)**2
    st.write(f"**180° Price Resistance:** ₹{res_180:.2f}")
    st.write(f"**180° Price Support:** ₹{sup_180:.2f}")

st.write("---")

# --- SECTION 2: GANN DATE CALCULATOR ---
st.subheader("📅 Gann Time Cycle (Reversal Dates)")
pivot_date = st.date_input("Select a Major High/Low Date", date(2024, 6, 4)) # Example: Election Result Low

if pivot_date:
    # We look for dates that are 90, 180, and 360 degrees in "Time"
    time_degrees = {"90° (Minor)": 0.5, "180° (Major)": 1.0, "360° (Cycle)": 2.0}
    
    # Simple Gann Time Cycle: Based on 1 day = 1 unit
    days_from_pivot = (date.today() - pivot_date).days
    sqrt_t = math.sqrt(days_from_pivot) if days_from_pivot > 0 else 1
    
    st.write(f"Days passed since pivot: **{days_from_pivot}**")
    
    for label, val in time_degrees.items():
        # Calculate next "Time Square"
        next_days = (sqrt_t + val)**2
        reversal_date = pivot_date + timedelta(days=int(next_days))
        st.info(f"**{label} Reversal Date:** {reversal_date.strftime('%d %b %Y')}")

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

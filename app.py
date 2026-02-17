import streamlit as st
import math

st.set_page_config(page_title="Dhaval's Gann Calc", page_icon="📈")
st.title("🏹 Dhaval's Gann Calculator")

# Input for stock price
price = st.number_input("Enter Stock Price", min_value=1.0, value=302, step=0.05)

if price:
    sqrt_p = math.sqrt(price)
    # Degrees: 90 (0.5), 180 (1.0), 360 (2.0)
    levels = {"90°": 0.5, "180°": 1.0, "360°": 2.0}
    
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🟢 Resistance")
        for deg, val in levels.items():
            res = (sqrt_p + val)**2
            st.success(f"{deg}: ₹{res:.2f}")

    with col2:
        st.subheader("🔴 Support")
        for deg, val in levels.items():
            sup = (sqrt_p - val)**2
            st.error(f"{deg}: ₹{sup:.2f}")




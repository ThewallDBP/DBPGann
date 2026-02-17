import streamlit as st
import math
import yfinance as yf
from datetime import timedelta, date

# 1. Page Configuration
st.set_page_config(page_title="Dhaval's Gann Pro", page_icon="🏹", layout="wide")

# 2. Live Nifty 50 Tracker Header
st.title("🏹 Dhaval's Gann Date & Price Pro")

try:
    nifty = yf.Ticker("^NSEI")
    nifty_price = nifty.fast_info.last_price
    nifty_change = nifty_price - nifty.fast_info.previous_close
    st.metric(label="NIFTY 50 LIVE", value=f"₹{nifty_price:.2f}", delta=f"{nifty_change:.2f}")
except:
    st.error("Live data currently unavailable. Using manual entry below.")

# 3. Sidebar for Quick Stock Selection
st.sidebar.header("💎 Watchlist")
ticker_symbol = st.sidebar.selectbox("Select Ticker", ["Manual Entry", "TCS.NS", "ITC.NS", "DIXON.NS", "IDBI.NS"])

if ticker_symbol == "Manual Entry":
    price = st.number_input("Enter Manual Price", min_value=1.0, value=313.75)
else:
    stock_data = yf.Ticker(ticker_symbol)
    price = stock_data.fast_info.last_price
    st.sidebar.write(f"**Current {ticker_symbol}:** ₹{price:.2f}")

# 4. Gann Price Calculator
if price:
    sqrt_p = math.sqrt(price)
    levels = {"90°": 0.5, "180°": 1.0, "360°": 2.0}
    
    st.subheader(f"📈 Gann Levels for Price: ₹{price:.2f}")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 🟢 Resistance")
        for deg, val in levels.items():
            st.success(f"{deg} Target: ₹{(sqrt_p + val)**2:.2f}")
    with col2:
        st.write("### 🔴 Support")
        for deg, val in levels.items():
            st.error(f"{deg} Floor: ₹{(sqrt_p - val)**2:.2f}")

st.divider()

# 5. Gann Date Calculator (Sharad Jhunjhunwala Method)
st.subheader("📅 Gann Time Cycle (Reversal Dates)")
pivot_date = st.date_input("Select a Major High/Low Date", date(2024, 6, 4))

if pivot_date:
    days_from_pivot = (date.today() - pivot_date).days
    sqrt_t = math.sqrt(days_from_pivot) if days_from_pivot > 0 else 1
    
    time_degrees = {"90° (Minor)": 0.5, "180° (Major)": 1.0, "360° (Cycle)": 2.0}
    for label, val in time_degrees.items():
        reversal_date = pivot_date + timedelta(days=int((sqrt_t + val)**2))
        st.info(f"**{label} Reversal Date:** {reversal_date.strftime('%d %b %Y')}")

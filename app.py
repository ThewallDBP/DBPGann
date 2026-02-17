import math

def calculate_gann_levels(price):
    degrees = [45, 90, 135, 180, 270, 360]
    results = {"Resistance": {}, "Support": {}}
    
    root = math.sqrt(price)
    
    for d in degrees:
        # Factor is Degree / 180
        factor = d / 180
        results["Resistance"][f"{d}°"] = round((root + factor)**2, 2)
        results["Support"][f"{d}°"] = round((root - factor)**2, 2)
    
    return results

def calculate_fibonacci(high, low):
    diff = high - low
    levels = {
        "0.0%": high,
        "23.6%": round(high - 0.236 * diff, 2),
        "38.2%": round(high - 0.382 * diff, 2),
        "50.0%": round(high - 0.5 * diff, 2),
        "61.8%": round(high - 0.618 * diff, 2),
        "100.0%": low
    }
    return levels

# Current Nifty 50 Data (Feb 18, 2026)
nifty_price = 25725
nifty_high = 26173
nifty_low = 25570

gann = calculate_gann_levels(nifty_price)
fib = calculate_fibonacci(nifty_high, nifty_low)

print(f"--- Nifty 50 Gann Levels (Base: {nifty_price}) ---")
for deg, val in gann["Resistance"].items():
    print(f"Resistance {deg}: {val} | Support {deg}: {gann['Support'][deg]}")

print(f"\n--- Fibonacci Retracement (Range: {nifty_low} - {nifty_high}) ---")
for lvl, val in fib.items():
    print(f"{lvl}: {val}")

# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "requests"]
# ///

"""
Draw a custom rainfall visualization from Open-Meteo data.

Run:
    uv run plot.py
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = HERE / "out"
CACHE = DATA / "rainfall.json"

PAPER = "#f4f4f0"
INK = "#222222"
RAIN = "#2a6f97"

def load_data():
    """Load and parse the JSON file from Open-Meteo."""
    if not CACHE.is_file():
        import fetch
        fetch.fetch()
    
    raw = json.loads(CACHE.read_text(encoding="utf-8"))
    daily = raw.get("daily", {})
    dates = daily.get("time", [])
    rain_amounts = daily.get("precipitation_sum", [])
    
    return dates, rain_amounts

def summarize_rainfall(amounts):
    """A custom function to calculate basic statistics (Total and Max)."""
    valid_amounts = [a for a in amounts if a is not None]
    total = sum(valid_amounts)
    maximum = max(valid_amounts) if valid_amounts else 0
    return total, maximum

def main():
    dates, rain_amounts = load_data()
    total, maximum = summarize_rainfall(rain_amounts)
    
    print(f"Processed {len(dates)} days. Total rainfall: {total:.1f} mm, Max in a day: {maximum} mm.")
    
    # Drawing the plot
    fig, axes = plt.subplots(figsize=(12, 5), facecolor=PAPER)
    axes.set_facecolor(PAPER)
    
    # Clean up None values for plotting
    cleaned_rain = [a if a is not None else 0.0 for a in rain_amounts]
    
    # Bar plot for rainfall
    axes.bar(range(len(cleaned_rain)), cleaned_rain, color=RAIN, width=1.0, edgecolor="none")
    
    axes.set_title(f"Daily Rainfall in Hong Kong 2025 (Total: {total:.1f} mm)", color=INK, fontsize=12, pad=15)
    axes.set_xlabel("Day of the Year (Jan - Dec)", color=INK, fontsize=10)
    axes.set_ylabel("Rainfall (mm)", color=INK, fontsize=10)
    
    axes.tick_params(colors=INK, labelsize=8)
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.spines['left'].set_color(INK)
    axes.spines['bottom'].set_color(INK)
    
    OUT.mkdir(exist_ok=True)
    target = OUT / "rainfall-year.png"
    fig.tight_layout()
    fig.savefig(target, dpi=150, facecolor=PAPER)
    print(f"Wrote picture to {target.relative_to(HERE)}")
    plt.show()

if __name__ == "__main__":
    main()


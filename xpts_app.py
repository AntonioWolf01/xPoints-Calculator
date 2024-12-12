import streamlit as st
import numpy as np

import streamlit as st
import numpy as np

st.title("🏆 xPTS Calculator")

st.write("""
Find out xPTS for your teams in seconds. Just pop in the numbers below ⚽
""")

# User inputs
xG_home = st.number_input("xG for home team", min_value=0.00, step=0.01, format="%.2f")
xG_away = st.number_input("xG for away team", min_value=0.00, step=0.01, format="%.2f")
shots_home = st.number_input("Shots for home team", min_value=0, step=1)
shots_away = st.number_input("Shots for away team", min_value=0, step=1)

# Function to simulate xPTS calculation
def calculate_xpts(xG_home, xG_away, shots_home, shots_away, simulations=10000):
    home_goals = np.random.binomial(shots_home, xG_home / shots_home, simulations)
    away_goals = np.random.binomial(shots_away, xG_away / shots_away, simulations)

    home_wins = np.sum(home_goals > away_goals)
    draws = np.sum(home_goals == away_goals)
    away_wins = np.sum(home_goals < away_goals)

    xPTS_home = (home_wins / simulations) * 3 + (draws / simulations) * 1
    xPTS_away = (away_wins / simulations) * 3 + (draws / simulations) * 1

    return xPTS_home, xPTS_away

# Calculate xPTS on button click
if st.button("Calculate xPTS"):
    if shots_home > 0 and shots_away > 0:
        xPTS_home, xPTS_away = calculate_xpts(xG_home, xG_away, shots_home, shots_away)
        st.success(f"xPTS for home team: {xPTS_home:.2f}")
        st.success(f"xPTS for away team: {xPTS_away:.2f}")
    else:
        st.error("The number of shots must be greater than 0 for both teams.")

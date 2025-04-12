import random
import streamlit as st
import time

# Leaderboard dictionary
leaderboard = {}

# 🎨 Custom CSS for Styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
        }
        .stGameBox, .stLeaderboard, .stMessage, .stCongrats {
            background: white;
            color: black;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            margin-bottom: 15px;
        }
        .stButton > button {
            background: #ff6b6b;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton > button:hover {
            background: #ff4d4d;
            color: white
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("🎯 Guess the Number Game!")

# Difficulty selection
difficulty = st.selectbox("Choose Difficulty:", ["Easy (1-10)", "Medium (1-50)", "Hard (1-100)"])
levels = {"Easy (1-10)": 10, "Medium (1-50)": 50, "Hard (1-100)": 100}
max_number = levels[difficulty]

# Start game button
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.number = None
    st.session_state.attempts = 0
    st.session_state.start_time = None

if st.button("🚀 Start Game"):
    st.session_state.number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.start_time = time.time()
    st.session_state.game_started = True
    st.markdown(f'<div class="stGameBox">I have chosen a number between 1 and {max_number}. Try to guess! 😊</div>', unsafe_allow_html=True)

# Game logic
if st.session_state.game_started:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=max_number, step=1, key="guess")

    if st.button("🎯 Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.markdown('<div class="stMessage" style="color: red; font-weight: bold;">📉 Too low! Try again.</div>', unsafe_allow_html=True)
        elif guess > st.session_state.number:
            st.markdown('<div class="stMessage" style="color: red; font-weight: bold;">📈 Too high! Try again.</div>', unsafe_allow_html=True)
        else:
            total_time = round(time.time() - st.session_state.start_time, 2)
            st.markdown(f'<div class="stCongrats" style="color: green; font-weight: bold;">🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts and {total_time} seconds. 🏆</div>', unsafe_allow_html=True)

            # Save to leaderboard
            name = st.text_input("Enter your name for the leaderboard:")
            if st.button("💾 Save Score"):
                if name:
                    leaderboard[name] = {"attempts": st.session_state.attempts, "time": total_time}
                    st.session_state.game_started = False  # Reset game
                else:
                    st.warning("❌ Please enter your name!")

# Display Leaderboard
if leaderboard:
    st.markdown('<div class="stLeaderboard"><h3>🏆 Leaderboard</h3></div>', unsafe_allow_html=True)
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: (x[1]["attempts"], x[1]["time"]))
    for rank, (player, data) in enumerate(sorted_leaderboard, 1):
        st.write(f"{rank}. **{player}** - {data['attempts']} attempts, {data['time']} sec")

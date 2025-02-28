import streamlit as st
import datetime
import random
import json

# Load or initialize user progress
def load_progress():
    try:
        with open("progress.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_progress(progress):
    with open("progress.json", "w") as file:
        json.dump(progress, file)

# Growth Mindset Challenges
challenges = [
    "Embrace a difficult task today and write down what you learned.",
    "Seek feedback from someone and reflect on how it helps you grow.",
    "Try something new outside your comfort zone and journal about it.",
    "Reframe a past failure as a learning experience and write about it.",
    "Encourage someone else to adopt a growth mindset.",
]

st.title("🌱 Growth Mindset Challenge")

today = str(datetime.date.today())
progress = load_progress()

# Select or generate today's challenge
if today not in progress:
    progress[today] = {"challenge": random.choice(challenges), "reflection": ""}
    save_progress(progress)

today_challenge = progress[today]["challenge"]
st.subheader("Today's Challenge:")
st.write(today_challenge)

# Reflection input
reflection = st.text_area("Reflect on today's challenge:", value=progress[today]["reflection"])
if st.button("Save Reflection"):
    progress[today]["reflection"] = reflection
    save_progress(progress)
    st.success("Reflection saved!")

# Display past reflections
st.subheader("📅 Your Past Entries")
for date, entry in sorted(progress.items(), reverse=True):
    with st.expander(f"{date}"):
        st.write(f"**Challenge:** {entry['challenge']}")
        st.write(f"**Reflection:** {entry['reflection']}")

# Progress visualization
st.subheader("📊 Your Progress Over Time")
dates = list(progress.keys())
num_entries = len(dates)
st.write(f"You've completed **{num_entries}** challenges so far! Keep going! 🚀")

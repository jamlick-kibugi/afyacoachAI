import streamlit as st
import datetime
from Homepage import set_sidebar_visibility

# Title
st.title("Weekly Exercises Recommendation (Demo)")

# Placeholder for results
result_container = st.empty()

# User inputs (for demonstration only)
user_height = st.text_input("Enter your height (cm):", "", key="height")
user_weight = st.text_input("Enter your weight (kg):", "", key="weight")
push_up = st.text_input("How many push ups can you do in a row:", "", key="push_up")
user_days = st.text_input("How many days a week do you want to go to the gym (1-7):", "", key="days")
goal = st.radio("Select your fitness goal:", ["Lose weight", "Bulk up", "Cut"], key="goal")
experience = st.radio("Select your fitness experience:", ["Beginner", "Intermediate", "Advanced"], key="experience")

# Generate fictional data (dummy weekly plan)
def generate_dummy_plan():
    today = datetime.datetime.now().date()
    # Six example exercises
    dummy_events = []
    focuses = ['Chest', 'Back', 'Legs', 'Shoulders', 'Arms', 'Core']
    colors = ['#FADADD', '#DDEBF7', '#D5E8D4', '#FFF2CC', '#F8CECC', '#E1D5E7']
    for i in range(int(user_days) if user_days.isdigit() else 3):
        day = today + datetime.timedelta(days=i)
        focus = focuses[i % len(focuses)]
        event = {
            "title": f"{focus} Workout - 3 Sets x 12 Reps x 50kg",
            "color": colors[i % len(colors)],
            "start": day.isoformat(),
            "end": day.isoformat(),
            "resourceId": chr(ord('a') + i)
        }
        dummy_events.append(event)
    return dummy_events

# On button click, generate and display dummy data
if st.button("Submit"):
    dummy_data = generate_dummy_plan()
    # Store in session for later use
    st.session_state['transferred_variable'] = dummy_data
    # Display the generated plan
    result_container.write("**Here is your fictional weekly plan:**")
    for evt in dummy_data:
        result_container.json(evt)

# Optionally, show the stored data
if 'transferred_variable' in st.session_state:
    st.write("---")
    st.write("Stored Session Data:")
    st.json(st.session_state['transferred_variable'])

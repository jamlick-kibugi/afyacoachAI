import streamlit as st
import pandas as pd
from PIL import Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# --- Functions for import ---

def set_sidebar_visibility(authentication_status):
    if authentication_status:
        st.sidebar.visible = True
    else:
        st.sidebar.visible = False

def initial_state():
    for key in [
        'df', 'X_train', 'X_test', 'y_train', 'y_test',
        'X_val', 'y_val', 'model', 'trained_model',
        'trained_model_bool', 'problem_type', 'metrics_df',
        'is_train', 'is_test', 'is_val', 'show_eval',
        'all_the_process', 'all_the_process_predictions',
        'y_pred_train', 'y_pred_test', 'y_pred_val',
        'uploading_way', 'lst_models', 'lst_models_predctions',
        'models_with_eval', 'reset_1'
    ]:
        if key not in st.session_state:
            st.session_state[key] = None if "lst" not in key else []
    if "metrics_df" not in st.session_state:
        st.session_state['metrics_df'] = pd.DataFrame()
    if "models_with_eval" not in st.session_state:
        st.session_state["models_with_eval"] = dict()

def new_line(n=1):
    for _ in range(n):
        st.write("\n")


# --- Page config and authentication ---

page_icon = Image.open("cover.png")
st.set_page_config(layout="centered", page_title="Gym Posture Correction", page_icon=page_icon)

names = ["Moc", "Thaocute"]
usernames = ["mocmeo", "thaocute"]
passwords = ["Mocmeo1809", "Mociuthao0"]

file_path = Path(__file__).parent / "hashed.pkl"
with open(file_path, "rb") as f:
    hashed_passwords = pickle.load(f)

credentials = {
    "usernames": {
        usernames[i]: {"name": names[i], "password": hashed_passwords[i]}
        for i in range(len(usernames))
    }
}

authenticator = stauth.Authenticate(
    credentials,
    cookie_name="gym_posture_app",
    key="abcdef",
    cookie_expiry_days=30
)

auth_result = authenticator.login(location="main")

if auth_result:
    name = auth_result['name']
    authentication_status = auth_result['authentication_status']
    username = auth_result['username']
else:
    name = None
    authentication_status = None
    username = None


# --- Main app logic ---

if authentication_status is False:
    st.error("Username/password is incorrect.")
elif authentication_status is None:
    st.warning("Please enter your username and password.")
elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name}!")

    set_sidebar_visibility(authentication_status)
    initial_state()

    col1, col2, col3 = st.columns([0.25, 1, 0.25])
    col2.image("d2t.png", use_column_width=True)
    new_line(2)

    st.markdown("""
    Welcome to the Gym Posture Correction App, the easy-to-use platform for your gym posture correction! This app helps you improve your posture during gym workouts.
    Please select a page from the navigation sidebar to get started.
    """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h2 align='center'> <b> Getting Started", unsafe_allow_html=True)
    new_line(1)
    st.write("""
    The first step is to "submit" your data. You can do that in two ways: **Live stream your video through the web cam**, or **Upload your file**. In all ways the data should be a video or image file and should not exceed 200 MB.
    """)


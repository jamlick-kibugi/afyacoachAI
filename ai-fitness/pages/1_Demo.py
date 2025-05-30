import streamlit as st
from Homepage import set_sidebar_visibility  
from pathlib import Path

st.title('AI Fitness Trainer: Squats Analysis')

current_dir = Path(__file__).parent
recorded_file = current_dir / "output_sample.mp4"

#recorded_file = r'C:\Users\Admin\OneDrive\Desktop\Projects\ai-fitness\ai-fitness\output_sample.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)

    
    
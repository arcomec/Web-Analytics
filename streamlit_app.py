import streamlit as st
import streamlit_analytics

# Initialize the analytics tracker
tracker = streamlit_analytics.AnalyticsTracker()

# Start tracking
with tracker.track():
    st.text_input("Write your name")
    st.selectbox("Select your favorite", ["guvi", "data", "science"])
    st.button("Click me")

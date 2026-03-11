import streamlit as st
import pandas as pd
import datetime

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Diary", "Planner", "About"])

# ---------------- Diary Page ----------------
if page == "Diary":
    st.title("📖 Daily Diary")
    st.text_input("Diary Title")
    st.date_input("Entry Date", datetime.date.today())
    st.text_area("Write your diary entry here:")
    st.checkbox("Mark as private")
    st.button("Save Entry")

    # Example table of diary entries
    diary_data = pd.DataFrame({
        "Date": ["2026-03-10", "2026-03-11"],
        "Title": ["Math Review", "Group Meeting"],
        "Entry": ["Studied probability", "Prepared slides"]
    })
    st.subheader("Past Entries")
    st.dataframe(diary_data)

# ---------------- Planner Page ----------------
elif page == "Planner":
    st.title("📅 Student Planner")

    # Tabs for planner features
    tab1, tab2, tab3 = st.tabs(["Add Task", "View Progress", "Notes"])

    with tab1:
        st.header("Add a New Task")
        st.text_input("Task name")
        st.date_input("Deadline")
        st.time_input("Time")
        st.text_area("Notes")
        st.radio("Priority", ["Low", "Medium", "High"])
        st.slider("Estimated hours", 0, 10, 1)
        st.checkbox("Mark as important")
        st.button("Save Task")

    with tab2:
        st.header("Progress Overview")
        st.progress(40)
        st.metric("Tasks Completed", 3, delta=+1)
        st.metric("Pending Tasks", 5, delta=-2)
        st.table({"Task": ["Essay", "Lab Report"], "Status": ["Done", "Pending"]})

    with tab3:
        st.header("Notes Section")
        st.text_area("Write your planner notes here:")
        st.multiselect("Tag notes with subjects", ["Math", "English", "Science"])
        st.number_input("Daily study goal (hours)", min_value=0, max_value=24, value=2)
        st.color_picker("Highlight Color", "#00f900")

# ---------------- About Page ----------------
elif page == "About":
    st.title("ℹ️ About this App")
    st.write("""
    Mahalaga 'to kasi bakit hindi  
    """)
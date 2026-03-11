import streamlit as st
import pandas as pd
import datetime

# Sidebar navigation
st.sidebar.title("Planner Navigation")
page = st.sidebar.radio("Go to:", ["Diary", "Planner", "About"])

# ---------------- Diary Page ----------------
if page == "Diary":
    st.title("📖 Daily Diary")
    st.text_input("Diary Title")
    st.date_input("Entry Date", datetime.date.today())
    st.text_area("Write your entry here:")
    st.file_uploader("Attach a photo", type=["jpg", "png"])
    st.audio("sample.mp3")  # demo audio
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # demo video
    st.button("Save Entry")

# ---------------- Planner Page ----------------
elif page == "Planner":
    st.title("📅 Student Planner")

    # Tabs for planner features
    tab1, tab2, tab3 = st.tabs(["Add Task", "View Progress", "Settings"])

    with tab1:
        st.header("Add a New Task")
        st.text_input("Task name")
        st.date_input("Deadline")
        st.time_input("Time")
        st.text_area("Notes")
        st.checkbox("Mark as important")
        st.radio("Priority", ["Low", "Medium", "High"])
        st.slider("Estimated hours", 0, 10, 1)
        st.button("Save Task")

    with tab2:
        st.header("Progress Overview")
        st.progress(50)
        st.metric("Tasks Completed", 5, delta=+2)
        st.metric("Pending Tasks", 3, delta=-1)
        st.table({"Task": ["Math HW", "Essay"], "Status": ["Done", "Pending"]})
        st.dataframe(pd.DataFrame({
            "Subject": ["Math", "English", "Science"],
            "Deadline": ["2026-03-15", "2026-03-20", "2026-03-25"],
            "Status": ["Done", "Pending", "Pending"]
        }))
        st.download_button("Download Planner Data", "Sample data", "planner.csv")

    with tab3:
        st.header("Settings")
        st.selectbox("Theme", ["Light", "Dark", "Colorful"])
        st.multiselect("Notifications", ["Email", "SMS", "App"])
        st.number_input("Daily Goal (hours)", min_value=0, max_value=24, value=2)
        st.color_picker("Highlight Color", "#00f900")

# ---------------- About Page ----------------
elif page == "About":
    st.title("ℹ️ About this App")
    st.write("""
    **Use-case:** Student planner/diary for organizing tasks and reflections.  
    **Target users:** Students managing academics and personal notes.  
    **Inputs:** Tasks, deadlines, diary entries, notes, settings.  
    **Outputs:** Progress bars, tables, metrics, and summaries.  
    """)
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
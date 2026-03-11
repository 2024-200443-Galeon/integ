import streamlit as st
import pandas as pd
import datetime
import random

# -- Sidebar navigation --
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("MENU")
st.session_state.page = st.sidebar.radio(
    "Go to:", ["Home","Diary", "Planner", "About"], 
    index=["Home","Diary","Planner","About"].index(st.session_state.page)
)

# -- Home Page --
if st.session_state.page == "Home":
    st.title("🎓 Welcome to the Student Planner App 🎓")
    st.subheader("✨ Every entry is a step forward ✨")

    st.divider()  # separator line

    quotes = [
        '"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle." - Christian D. Larson',
        '"It does not matter how slowly you go, as long as you do not stop." - Confucius',
        '"Study while others are sleeping; work while others are loafing; prepare while others are playing; and dream while others are wishing." - William Arthur Ward',
        '"You do not have to be great to start, but you have to start to be great." - Zig Ziglar',
        '"The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack of will." - Vince Lombardi',
        '"You are never too old to set another goal or to dream a new dream." - C.S. Lewis',
        '"Success is not the absence of failure; it is the persistence through failure." - Aisha Tyler',
        '"The best way to predict your future is to create it." - Abraham Lincoln',
        '"Efforts and courage are not enough without purpose and direction." - John F. Kennedy',
        '"Procrastination is the thief of time." - Edward Young',
        '"Real difficulties can be overcome; it is only the imaginary ones that are unconquerable." - Theodore N. Vail',
        '"Nothing is impossible. The word itself says \'I\'m Possible\'." - Audrey Hepburn',
        '"The greatest amount of wasted time is time not getting started." - Dawson Trotman',
        '"Work hard in silence. Let your success be your noise." - Frank Ocean',
        '"Education is the most powerful weapon which you can use to change the world." - Nelson Mandela'
    ]
    if st.button("✨ Inspire Me!"):
        st.markdown(f"> ✨ *{random.choice(quotes)}* ✨")

    st.divider()

    # Quick Links Section
    st.header("📌 Quick Links")
    st.caption("⚠️ Tip: Quick Links may need a second click to fully load the page.")
    col1, col2, col3 = st.columns(3)

    if col1.button("📖 Diary 📖"):
        st.session_state.page = "Diary"
    if col2.button("📅 Planner 📅"):
        st.session_state.page = "Planner"
    if col3.button("ℹ️ About ℹ️"):
        st.session_state.page = "About"


# -- Diary Page --
elif st.session_state.page == "Diary":
    st.title("📖 Daily Diary 📖")

    # Initialize diary storage
    if "diary_entries" not in st.session_state:
        st.session_state.diary_entries = []

    # Inputs (no manual value binding)
    st.text_input("Diary Title", key="diary_title")
    st.date_input("Entry Date", key="diary_date", value=datetime.date.today())
    st.text_area("Write your diary entry here:", key="diary_entry")

    # Save button
    if st.button("Save Entry"):
        new_entry = {
            "Date": str(st.session_state.diary_date),
            "Title": st.session_state.diary_title,
            "Entry": st.session_state.diary_entry
        }
        st.session_state.diary_entries.append(new_entry)
        st.success("✅ Entry saved!")

    # Create new entry button (safe reset)
    if st.button("➕ Create New Entry"):
        st.session_state.update({
            "diary_title": "",
            "diary_entry": "",
            "diary_date": datetime.date.today()
        })

    # Show past entries
    if st.session_state.diary_entries:
        st.subheader("Past Entries")
        diary_data = pd.DataFrame(st.session_state.diary_entries)
        st.dataframe(diary_data)
    else:
        st.info("No diary entries yet. Start writing! 😎")


# -- Planner Page --
elif st.session_state.page == "Planner":
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

# -- About Page --
elif st.session_state.page == "About":
    st.title("ℹ️ About this App")
    st.write("""
    Mahalaga 'to kasi bakit hindi  
    """)
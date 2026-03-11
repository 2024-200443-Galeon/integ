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

    # Inputs
    title = st.text_input("Diary Title")
    date = st.date_input("Entry Date", datetime.date.today())
    entry = st.text_area("Write your diary entry here:")

    # Note for users
    st.caption("⚠️ Tip: Erase the words above to add a new entry.")

    # Save button
    if st.button("Save Entry"):
        new_entry = {
            "Date": str(date),
            "Title": title,
            "Entry": entry
        }
        st.session_state.diary_entries.append(new_entry)
        st.success("✅ Entry saved!")

    # Show past entries
    if st.session_state.diary_entries:
        st.subheader("Past Entries")
        diary_data = pd.DataFrame(st.session_state.diary_entries)
        diary_data.index = diary_data.index + 1  # start numbering at 1
        st.dataframe(diary_data)
    else:
        st.info("No diary entries yet. Start writing! 😎")


# -- Planner Page --
elif st.session_state.page == "Planner":
    st.title("📅 Student Planner")

    # Initialize task storage
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Tabs for planner features
    tab1, tab2 = st.tabs(["Add Task", "View Progress"])

    with tab1:
        st.header("Add a New Task")
        task_name = st.text_input("Task name", key="task_name")
        deadline = st.date_input("Deadline", key="task_deadline")
        time = st.time_input("Time", key="task_time")
        notes = st.text_area("Notes", key="task_notes")
        priority = st.radio("Priority", ["Low", "Medium", "High"], key="task_priority")
        hours = st.slider("Estimated hours", 0, 10, 1, key="task_hours")
        important = st.checkbox("Mark as important", key="task_important")

        if st.button("Save Task"):
            new_task = {
                "Task": st.session_state.task_name,
                "Deadline": str(st.session_state.task_deadline),
                "Time": str(st.session_state.task_time),
                "Notes": st.session_state.task_notes,
                "Priority": st.session_state.task_priority,
                "Hours": st.session_state.task_hours,
                "Important": st.session_state.task_important,
                "Done": False  # default status
            }
            st.session_state.tasks.append(new_task)
            st.success("✅ Task saved!")

   with tab2:
    st.header("Progress Overview")
    if st.session_state.tasks:
        for i, task in enumerate(st.session_state.tasks, start=1):
            # make sure every task has a "Done" field
            if "Done" not in task:
                task["Done"] = False

            cols = st.columns([3, 2, 2, 2, 2])  # layout per row
            cols[0].write(f"{i}. {task['Task']}")
            cols[1].write(task["Deadline"])
            cols[2].write(task["Priority"])
            cols[3].write(f"{task['Hours']} hrs")

            # Checkbox to mark as done (safe access)
            done_key = f"done_{i}"
            checked = cols[4].checkbox("Done", value=task.get("Done", False), key=done_key)
            st.session_state.tasks[i-1]["Done"] = checked

        st.metric("Total Tasks", len(st.session_state.tasks))
        st.metric("Completed", sum(1 for t in st.session_state.tasks if t.get("Done", False)))
    else:
        st.info("No tasks yet. Add one in the 'Add Task' tab!")


# -- About Page --
elif st.session_state.page == "About":
    st.title("ℹ️ About this App")
    st.write("""
    Mahalaga 'to kasi bakit hindi  
    """)
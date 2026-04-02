import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="HIA - Health Insights AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: white;
    }
    h1, h2, h3 {
        color: #38bdf8;
    }
    .css-1d391kg {
        background-color: #020617;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🧠 Health Insights AI Agent")
st.markdown("### AI-powered Medical Report Analyzer 🚀")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")
st.sidebar.info("Analyze your health reports using AI")

option = st.sidebar.selectbox(
    "Choose Feature",
    ["Health Analysis", "Chat Assistant"]
)

# ---------------- HEALTH ANALYSIS ----------------
if option == "Health Analysis":
    st.subheader("📊 Enter Your Health Data")

    col1, col2, col3 = st.columns(3)

    with col1:
        hemoglobin = st.number_input("Hemoglobin", 0.0, 20.0, 13.0)
    with col2:
        tsh = st.number_input("TSH Level", 0.0, 10.0, 2.5)
    with col3:
        cholesterol = st.number_input("Cholesterol", 100, 300, 180)

    st.subheader("📤 Upload Medical Report (Optional)")
    uploaded_file = st.file_uploader("Upload file", type=["pdf", "txt"])

    if st.button("🔍 Analyze"):
        st.success("Report analyzed successfully ✅")

        st.subheader("📈 Results")

        c1, c2, c3 = st.columns(3)

        # Simple logic (safe, won't break anything)
        hb_status = "Normal" if hemoglobin >= 12 else "Low ⚠️"
        tsh_status = "High ⚠️" if tsh > 4.5 else "Normal"
        chol_status = "Good" if cholesterol < 200 else "High ⚠️"

        c1.metric("Hemoglobin", hemoglobin, hb_status)
        c2.metric("TSH", tsh, tsh_status)
        c3.metric("Cholesterol", cholesterol, chol_status)

        st.info("💡 Basic AI Insight:")
        st.write(f"TSH level suggests: {tsh_status}")

        st.info("🧬 Recommendation:")
        if tsh > 4.5:
            st.write("Consult a doctor, possible thyroid imbalance")
        else:
            st.write("Maintain a healthy lifestyle")

# ---------------- CHAT ----------------
elif option == "Chat Assistant":
    st.subheader("💬 AI Health Chat")

    user_input = st.text_input("Ask something about your health")

    if st.button("Ask AI"):
        if user_input:
            st.write("🤖 AI Response:")
            st.success("This is a demo response. Connect your AI model here.")
        else:
            st.warning("Please enter a question")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("👨‍💻 Developed by **James Khele** 🚀")
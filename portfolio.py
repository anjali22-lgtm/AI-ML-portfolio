import streamlit as st
from PIL import Image
import time

st.set_page_config(
    page_title="Anjali | AI/ML Portfolio",
    page_icon="🤖",
    layout="wide"
)

# ---------------- PROFESSIONAL CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(-45deg, #0b1220, #111827, #0f172a);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(10, 15, 25, 0.9);
}

/* Glass card */
.card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: 0.3s ease;
}

.card:hover {
    transform: scale(1.02);
    border: 1px solid #00ffd5;
}

/* Titles */
.hero {
    font-size: 46px;
    font-weight: 700;
    color: #00ffd5;
}

.subtext {
    font-size: 18px;
    color: #cbd5e1;
}

/* Buttons */
.stDownloadButton button {
    background: #00ffd5;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}

.stDownloadButton button:hover {
    background: #00bfa6;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TYPING EFFECT ----------------
def typing_effect(text):
    placeholder = st.empty()
    typed = ""
    for c in text:
        typed += c
        time.sleep(0.02)
        placeholder.markdown(f"### {typed}")

# ---------------- SIDEBAR ----------------
try:
    image = Image.open("profile.jpg")
    st.sidebar.image(image, width=150)
except:
    st.sidebar.warning("Add profile.jpg")

st.sidebar.title("Anjali Jamwal")
st.sidebar.write("AI/ML Engineer | LLMs | Data Science")

menu = st.sidebar.radio("Navigation", ["Home", "Projects", "Skills", "Contact"])

# ---------------- HOME ----------------
if menu == "Home":

    st.markdown("<div class='hero'>Hi 👋 I'm Anjali</div>", unsafe_allow_html=True)

    typing_effect("AI/ML Developer | LLMs | Machine Learning | Data Science")

    st.markdown("---")

    try:
        with open("resume.pdf", "rb") as file:
            st.download_button(
                "📄 Download Resume",
                file,
                file_name="Anjali_Resume.pdf"
            )
    except:
        st.warning("Add resume.pdf")

    st.markdown("### 🚀 About Me")
    st.write("""
    I am an aspiring AI/ML Engineer focused on building real-world intelligent systems 
    using Machine Learning, NLP, and Large Language Models.
    """)

# ---------------- PROJECTS ----------------
elif menu == "Projects":

    st.title("🚀 Projects")

    st.markdown("""
    <div class="card">
        <h3>AI Resume Analyzer</h3>
        <p>Gemini AI + LangChain resume screening system</p>
        <b>Tools:</b> Python | Streamlit | LangChain | Gemini AI
        <br><br>
        🔗 <a href="https://huggingface.co/spaces/anjali4ho/ai-resume-analyzer" target="_blank">Live Demo</a>
        <br>
        💻 <a href="https://github.com/anjali22-lgtm/AI-Resume-Analyzer" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>LangChain-Groq Chatbot</h3>
        <p>AI chatbot powered by Groq LLM API</p>
        <b>Tools:</b> Python | Streamlit | LangChain | Groq API
        <br><br>
        🔗 <a href="https://langchain-groq-chatbot-vntwrehc9y2jfggzszf5sa.streamlit.app/" target="_blank">Live Demo</a>
        <br>
        💻 <a href="https://github.com/anjali22-lgtm/LangChain-Groq-Chatbot" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Cancer Risk Prediction</h3>
        <p>Machine Learning classification system</p>
        <b>Tools:</b> Python | Scikit-learn | Pandas | NumPy
        <br><br>
        💻 <a href="https://github.com/anjali22-lgtm/cancer-risk-prediction" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif menu == "Skills":

    st.title("🛠 Skills")

    st.markdown("""
    <div class="card">
        <h3>AI/ML</h3>
        Machine Learning, NLP, LLMs, Data Science
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Tools</h3>
        Python, Streamlit, LangChain, Gemini AI, Groq API
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Libraries</h3>
        Pandas, NumPy, Scikit-learn, Matplotlib
    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif menu == "Contact":

    st.title("📫 Contact Me")

    st.markdown("""
    <div class="card">
        📧 Email: your-email@example.com <br>
        🔗 GitHub: https://github.com/anjali22-lgtm <br>
        💼 LinkedIn: add-your-link <br><br>
        ⭐ Open for AI/ML Internship Opportunities
    </div>
    """, unsafe_allow_html=True)
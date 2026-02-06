import streamlit as st
import google.generativeai as genai

# --- PAGE SETUP ---
st.set_page_config(page_title="AI Legal Dost IN", page_icon="🤖", layout="wide")

# Custom CSS to match the image styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        font-weight: bold;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: grey;
        font-size: 12px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.title("🤖 AI Legal Dost IN")
with col2:
    st.selectbox("Language", ["English", "Hindi", "Hinglish", "Bengali", "Marathi", "Tamil"], index=2)
with col3:
    st.write("👤 AI Legal Dost User")

# --- INTRO BOX ---
st.info("""
    Namaste, AI Legal Dost User! I am **AI Legal Dost**, your friendly and reliable guide 
    to simplifying **Indian law** and procedures. I use up-to-date, authoritative sources 
    for my answers. I will be responding in **Hinglish (Hindi in Roman script)**.
    
    Type your query directly, or select a quick option to start:
    1. **FIRs & Police Complaints**
    2. **RTI Filing Procedure**
    3. **Consumer Rights**
    4. **Rental/Landlord Disputes**
""")

# --- FEATURE BUTTONS (The Pill Buttons from your image) ---
btn_col1, btn_col2, btn_col3, btn_col4, btn_col5, btn_col6 = st.columns(6)
with btn_col1:
    if st.button("⚡ Document Genie", type="primary"):
        st.session_state.prompt = "Help me draft a legal document."
with btn_col2:
    if st.button("📖 Explain Law"):
        st.session_state.prompt = "Explain a specific Indian law for me."
with btn_col3:
    if st.button("📷 Legal Lens"):
        st.session_state.prompt = "Help me analyze a legal document image."
with btn_col4:
    if st.button("📝 Summarize"):
        st.session_state.prompt = "Summarize this legal research."
with btn_col5:
    if st.button("🗣️ Translator"):
        st.session_state.prompt = "Translate this legal text."
with btn_col6:
    if st.button("⚠️ Health Check"):
        st.session_state.prompt = "Check my legal compliance health."

# --- CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if "prompt" not in st.session_state:
    st.session_state.prompt = None

user_input = st.chat_input("Ask about your rights or procedures...")
current_prompt = user_input or st.session_state.prompt

if current_prompt:
    st.session_state.messages.append({"role": "user", "content": current_prompt})
    with st.chat_message("user"):
        st.markdown(current_prompt)
    
    # Placeholder for AI Response (Connect your API Key here)
    with st.chat_message("assistant"):
        response = "I am ready to help you as your AI Legal Dost. Please ensure your Gemini API key is configured to get live answers."
        st.markdown(response)
    
    st.session_state.prompt = None # Reset button prompt

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        **Disclaimer:** AI Legal Dost is for educational guidance only and is not a substitute for a certified lawyer.<br>
        Made with NetWhy Studios
    </div>
    """, unsafe_allow_html=True)

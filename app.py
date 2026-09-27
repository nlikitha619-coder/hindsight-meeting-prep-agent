import streamlit as st
from groq import Groq

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Hindsight Meeting Prep Agent", page_icon="🤝", layout="centered")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("⚙️ Configuration")
groq_key = st.sidebar.text_input("Enter Groq API Key:", type="password", value="")

if groq_key:
    client = Groq(api_key=groq_key)
else:
    st.sidebar.warning("Please enter your Groq API Key to power the AI.")

# --- APP FRONTEND ---
st.title("🤝 Hindsight Meeting Prep Agent")
st.markdown("*Empowering professionals by remembering every client detail, past objection, and preference over time.*")

if "mock_hindsight_db" not in st.session_state:
    st.session_state.mock_hindsight_db = {}

tab1, tab2 = st.tabs(["📝 Log Past Meeting", "💡 Generate Smart Briefing"])

with tab1:
    st.subheader("Record Interaction Details")
    client_name = st.text_input("Client/Company Name:", placeholder="e.g., Ananya (Tech Corp)")
    interaction_notes = st.text_area("What happened during this meeting?", placeholder="e.g., Ananya loves our tool but prefers clean API structures over complex dashboards.")
    
    if st.button("Save to Hindsight Memory"):
        if not client_name or not interaction_notes:
            st.error("Please fill in both fields!")
        else:
            st.session_state.mock_hindsight_db[client_name.lower().strip()] = interaction_notes
            st.success(f"Successfully committed context for '{client_name}' into Hindsight Memory Layer!")

with tab2:
    st.subheader("Prepare for Your Upcoming Call")
    search_client = st.text_input("Who are you meeting with next?", placeholder="e.g., Ananya (Tech Corp)")
    
    if st.button("Retrieve Context & Brief Me"):
        if not groq_key:
            st.error("Please provide a Groq API key in the sidebar first!")
        elif not search_client:
            st.warning("Please enter a client name to search.")
        else:
            client_key = search_client.lower().strip()
            if client_key in st.session_state.mock_hindsight_db:
                retrieved_memory = st.session_state.mock_hindsight_db[client_key]
                with st.spinner("Hindsight recalling context..."):
                    prompt = f"""
                    You are an elite corporate Sales Executive Assistant. 
                    Your user has an upcoming meeting with: {search_client}.
                    Here is the historical context retrieved from their Hindsight persistent memory layer:
                    "{retrieved_memory}"
                    
                    Provide a concise, high-impact briefing for the user. It MUST include:
                    1. 🎯 Core Goal: What the client cares about.
                    2. ⚠️ Critical Objections: What blocked them last time.
                    3. 🚀 Strategy: 2 short bullet points on how to pitch successfully today based on what was remembered.
                    """
                    completion = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.3
                    )
                    st.markdown("### 📋 Your AI Briefing")
                    st.info(completion.choices[0].message.content)
            else:
                st.error(f"No historical data found for '{search_client}' in memory. Without Hindsight, the agent is running stateless!")

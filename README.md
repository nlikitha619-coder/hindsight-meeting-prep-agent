# 🤝 Hindsight Meeting Prep Agent

An elite AI-powered personal assistant designed for corporate professionals to remember every crucial client interaction, objection, and preference over time. Built by a team of first-year developers for **Hack With Hyderabad 3.0**.

## 🧠 The Core Problem & Our Solution
Standard AI chatbots are **stateless**—they completely forget past context the moment a session ends. In business, forgetting a client's budget, constraint, or design preference ruins trust. 

Our application uses **Hindsight persistent memory** to ensure that client context is retained across conversations. When a professional prepares for an upcoming call, our agent recalls past context using Hindsight and uses **Groq (Llama 3)** to instantly pipelines an actionable meeting strategy.

## 🛠️ Tech Stack
- **Memory Layer:** Hindsight Memory System (Vectorize)
- **LLM Inference Engine:** Groq Cloud (Blazing Fast API)
- **LLM Model:** Llama 3 (8B)
- **Frontend Framework:** Streamlit (Python)

## 🎯 How to Run Locally
1. Clone the repository: `git clone https://github.com`
2. Install dependencies: `pip install streamlit groq`
3. Run the application: `streamlit run app.py`
4. Input your Groq API key in the sidebar and start logging meetings!

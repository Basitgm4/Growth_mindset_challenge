import streamlit as st
import random

# --- Load CSS ---
with open("style.css") :
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 class='title'>🌱 Cultivating a Growth Mindset 🌱</h1>", unsafe_allow_html=True)

# --- Introduction ---
st.markdown("<p class='info-box'>Welcome to the Growth Mindset Project! This application aims to help you understand and cultivate a growth mindset – the belief that your abilities and intelligence can be developed through dedication and hard work. Let's explore some key concepts and practice some helpful thinking.</p>", unsafe_allow_html=True)

# --- Section: Understanding Growth Mindset ---
st.markdown("<h2 class='section-header'>🧠 Understanding Growth Mindset</h2>", unsafe_allow_html=True)
st.markdown("<p>A growth mindset is about embracing challenges, persisting in the face of setbacks, seeing effort as the path to mastery, learning from criticism, and finding inspiration in the success of others.</p>", unsafe_allow_html=True)
st.markdown("<p>In contrast, a fixed mindset believes that intelligence and talent are static traits. People with a fixed mindset may avoid challenges and give up easily when faced with obstacles.</p>", unsafe_allow_html=True)

# --- Section: Growth Mindset Prompts ---
st.markdown("<h2 class='section-header'>💡 Growth Mindset Prompts</h2>", unsafe_allow_html=True)

prompts = [
    "When you face a challenge, what is your initial thought?",
    "Instead of saying 'I can't do this,' try saying 'I can't do this... yet.' What difference does that make?",
    "Think about a time you struggled with something. What did you learn from that experience?",
    "How can you reframe a perceived failure as an opportunity to learn and grow?",
    "What small step can you take today to move closer to a goal you have?",
    "How can you embrace the process of learning, even when it's difficult?",
    "What is one area where you can challenge yourself to try something new this week?",
]

selected_prompt = st.selectbox("Choose a prompt to reflect on:", prompts)

if st.button("Reflect"):
    st.markdown(f"<div class='prompt-container'><p class='prompt-text'><b>Prompt:</b> {selected_prompt}</p><p>Take a moment to think about this prompt and how it relates to your own experiences and beliefs.</p></div>", unsafe_allow_html=True)

# --- Section: Interactive Challenges ---
st.markdown("<h2 class='section-header'>🚀 Let's Embrace Challenges!</h2>", unsafe_allow_html=True)

challenges = [
    "Try learning a new word in a language you're interested in.",
    "Attempt a puzzle you haven't tried before.",
    "Spend 15 minutes practicing a new skill (e.g., coding, playing an instrument).",
    "Identify a small task you've been putting off and complete it.",
    "Reach out to someone you haven't spoken to in a while.",
    "Try a new recipe or cook something you've never made before.",
    "Take a short walk and observe your surroundings with fresh eyes.",
]

if 'current_challenge' not in st.session_state:
    st.session_state['current_challenge'] = None

if st.button("Get a Challenge"):
    st.session_state['current_challenge'] = random.choice(challenges)

if st.session_state['current_challenge']:
    st.markdown(f"<div class='prompt-container'><p class='prompt-text'><b>Your Challenge:</b> {st.session_state['current_challenge']}</p><p>Give this challenge a try and see what you learn!</p></div>", unsafe_allow_html=True)
    if st.button("Challenge Completed"):
        st.success("Great job! You've embraced a challenge. Remember to reflect on what you learned.")
        st.session_state['current_challenge'] = None # Reset the challenge

# --- Section: Tips for Cultivating a Growth Mindset ---
st.markdown("<h2 class='section-header'>🌟 Tips for Cultivating a Growth Mindset</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>Embrace challenges: See them as opportunities for growth.</li>
    <li>Persist in the face of setbacks: Use them as learning experiences.</li>
    <li>See effort as the path to mastery: Recognize that hard work leads to improvement.</li>
    <li>Learn from criticism: View feedback as a way to improve.</li>
    <li>Find inspiration in the success of others: Celebrate their achievements as motivation.</li>
</ul>
""", unsafe_allow_html=True)

# --- Section: Resources ---
st.markdown("<h2 class='section-header'>📚 Resources</h2>", unsafe_allow_html=True)
st.markdown("""
<p>Here are some resources to learn more about growth mindset:</p>
<ul>
    <li><a href="https://www.mindsetworks.com/" target="_blank">Mindset Works</a></li>
    <li><a href="https://www.ted.com/talks/carol_s_dweck_the_power_of_believing_that_you_can_improve" target="_blank">Carol Dweck: The Power of Believing That You Can Improve (TED Talk)</a></li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; margin-top: 30px; color: #777;'>Developed with Streamlit and Python</div>", unsafe_allow_html=True)

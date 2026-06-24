import streamlit as st
from youtubeAnalyzer import build_youtube_agent

st.set_page_config(
    page_title = "Youtube Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")

#cache - fast access, temp storage => most freq accessed
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

#input space
video_url  = st.text_input("Enter Youtube Video Link")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing Video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"  
        )
    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)
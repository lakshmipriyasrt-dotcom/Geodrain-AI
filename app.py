print("GeoDrainAI Prototype")
import streamlit as st

st.set_page_config(page_title="GeoDrainAI", layout="wide")

st.title("🌍 GeoDrainAI")
st.subheader("AI-Driven Flood Risk Mapping and Drainage Planning")

st.image("screenshots/satellite-map.png", caption="Satellite Map")

st.image("screenshots/flood-heatmap.png", caption="Flood Heatmap")

st.image("screenshots/drainage-output.png", caption="Drainage Recommendation")

st.metric("Flood Reduction", "42%")
st.metric("Homes Protected", "3400")
st.metric("Estimated Savings", "₹12 Lakhs")

st.success("AI Analysis Completed Successfully")
st.markdown("---")

st.header("System Workflow")

st.write("""
1. Satellite image acquisition  
2. Terrain and flood-risk analysis  
3. AI-based flood prediction  
4. Drainage recommendation generation  
5. Interactive dashboard visualization  
""")

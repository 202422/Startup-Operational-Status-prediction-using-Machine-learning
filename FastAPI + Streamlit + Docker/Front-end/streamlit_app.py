import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://backend:8000/api/predict"

st.set_page_config(page_title="Startup Status Prediction", layout="centered")

st.title("🚀 Startup Status Prediction")
st.markdown("Enter the startup information below to predict its current status.")

# Input fields
founded_at = st.number_input("Founded At (Year)", min_value=1900, max_value=2025, value=2010)
active_days = st.number_input("Active Days", min_value=1, max_value=20000, value=365)
first_funding_at = st.number_input("First Funding Year", min_value=1900, max_value=2025, value=2011)
last_funding_at = st.number_input("Last Funding Year", min_value=1900, max_value=2025, value=2012)
funding_total_usd = st.number_input("Total Funding (USD)", min_value=0.0, step=1000.0, value=1000000.0)
first_milestone_at = st.number_input("First Milestone Year", min_value=1900, max_value=2025, value=2011)
last_milestone_at = st.number_input("Last Milestone Year", min_value=1900, max_value=2025, value=2011)
milestones = st.number_input("Number of Milestones", min_value=0, step=1, value=1)
relationships = st.number_input("Relationships", min_value=0, step=1, value=3)
lng = st.number_input("Longitude", value=0.0)

# Dropdowns for category and country
category_code = st.selectbox(
    "Category Code",
    ["mobile", "web", "software", "ecommerce", "consulting",
     "advertising", "biotech", "games_video", "enterprise", "public_relations",
     "other"]
)
country_code = st.selectbox(
    "Country Code",
    ["USA", "FRA", "GBR", "CAN", "DEU", "AUS", "other", "ISR", "IND", "ESP",
     "NLD"]
)

# Predict button
if st.button("🔍 Predict Startup Status"):
    # Prepare payload
    payload = {
        "founded_at": founded_at,
        "active_days": active_days,
        "first_funding_at": first_funding_at,
        "last_funding_at": last_funding_at,
        "funding_total_usd": funding_total_usd,
        "first_milestone_at": first_milestone_at,
        "last_milestone_at": last_milestone_at,
        "milestones": milestones,
        "relationships": relationships,
        "lng": lng,
        "category_code": category_code,
        "country_code": country_code
    }

    try:
        # Send request to FastAPI
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            predicted_status = result.get("predicted_status", "Unknown")
            st.success(f"🎯 **Predicted Status:** {predicted_status}")
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"⚠️ Cannot connect to API: {e}")
import streamlit as st
import pandas as pd
from PIL import Image
from modules import vision, weather, market, translations

# Page Config
st.set_page_config(page_title="AgriThon", layout="wide", page_icon="🍅")

# Session State for Language
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

def t(key):
    return translations.get_text(key, st.session_state["lang"])

# Sidebar
with st.sidebar:
    st.header("Language / భాష / ಭಾಷೆ / भाषा / மொழி")
    lang_choice = st.radio("Choose Language", ["English", "Telugu (తెలుగు)", "Kannada (ಕನ್ನಡ)", "Marathi (मराठी)", "Tamil (தமிழ்)"], index=0)
    
    if lang_choice == "English": st.session_state["lang"] = "en"
    elif "Telugu" in lang_choice: st.session_state["lang"] = "te"
    elif "Kannada" in lang_choice: st.session_state["lang"] = "kn"
    elif "Marathi" in lang_choice: st.session_state["lang"] = "mr"
    elif "Tamil" in lang_choice: st.session_state["lang"] = "ta"
    
    st.markdown("---")
    st.header(t("settings"))
    region = st.selectbox(t("select_region"), ["Telangana", "Andhra Pradesh", "Karnataka", "Maharashtra", "Tamil Nadu"], index=0)

# Main Title
st.title(t("title"))
st.subheader(t("subheader"))

# --- MAIN LAYOUT ---
# --- CUSTOM CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

# --- MAIN LAYOUT (MOBILE OPTIMIZED) ---
# Use Tabs for better mobile navigation instead of wide columns
tab1, tab2, tab3 = st.tabs([f"📸 {t('upload_header')}", f"🌤️ {t('weather_header')}", f"💰 {t('market_prices')}"])

# --- TAB 1: CROP ANALYSIS ---
with tab1:
    st.caption("AI Post-Harvest Spoilage Forecaster")
    
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        
        with st.spinner(t("analyzing")):
            analysis_result = vision.analyze_image(image)
        
        if "error" in analysis_result:
            st.error(f"Error: {analysis_result['error']}")
        else:
            score = analysis_result.get("spoilage_score", 5)
            st.session_state["spoilage_score"] = score
            
            # NATIVE VISUALS: Progress Bar & Metrics
            st.divider()
            st.subheader(f"{t('crop_health')}")
            
            # Color logic
            if score < 4:
                st.success(f"🟢 Good / బాగుంది (Score: {score}/10)")
            elif score < 8:
                st.warning(f"🟡 Medium / ఫర్వాలేదు (Score: {score}/10)")
            else:
                st.error(f"🔴 Bad / పాడైంది (Score: {score}/10)")
            
            st.progress(score / 10)
            st.caption(analysis_result.get('analysis', ''))
            
            if "model_used" in analysis_result:
                st.caption(f"Model used: {analysis_result['model_used']}")
            
            # Recommendation
            st.divider()
            st.subheader(f"💡 {t('market_header')}")
            
            weather_data = weather.get_weather(region)
            rec = market.get_recommendation(score, weather_data)
            
            action_key = "hold"
            if "SELL IMMEDIATELY" in rec['action']: action_key = "sell_now"
            elif "SELL SOON" in rec['action']: action_key = "sell_soon"
            elif "MONITOR" in rec['action']: action_key = "monitor"
            
            display_action = t(action_key)
            
            # Native Container for Recommendation
            rec_container = st.container(border=True)
            if rec["urgency"] == "CRITICAL":
                rec_container.error(f"## {display_action}\n{rec['reason']}")
            elif rec["urgency"] == "HIGH":
                rec_container.warning(f"## {display_action}\n{rec['reason']}")
            else:
                rec_container.success(f"## {display_action}\n{rec['reason']}")

    else:
        st.info("👋 Upload an image to start analysis.")

# --- TAB 2: WEATHER ---
with tab2:
    with st.container(border=True):
        st.caption(f"📍 {region}")
        
        weather_data = weather.get_weather(region)
        
        # Native Metrics
        c1, c2 = st.columns(2)
        c1.metric(t("temp"), f"{weather_data['temperature']}°C")
        c2.metric(t("humidity"), f"{weather_data['humidity']}%")
        
        st.caption(f"Status: {weather_data['condition']}")
        
        if weather_data.get("is_live"):
            st.toast("🟢 Live Weather Updated")
        
        # Chart
        if not weather_data['hourly_data'].empty:
            st.line_chart(weather_data['hourly_data'].set_index("Time")['Humidity'], height=200)

# --- TAB 3: MARKET ---
with tab3:
    with st.container(border=True):
        market_df = market.get_market_data(region)
        st.dataframe(
            market_df, 
            hide_index=True, 
            use_container_width=True,
            column_config={
                "Market": st.column_config.TextColumn("Mandi"),
                "Tomato_Price": st.column_config.NumberColumn("🍅 Tomato", format="₹%d"),
                "Onion_Price": st.column_config.NumberColumn("🧅 Onion", format="₹%d"),
                "Potato_Price": st.column_config.NumberColumn("🥔 Potato", format="₹%d"),
                "Chilli_Price": st.column_config.NumberColumn("🌶️ Chilli", format="₹%d"),
                "Brinjal_Price": st.column_config.NumberColumn("🍆 Brinjal", format="₹%d"),
            }
        )

# Footer
st.divider()
st.caption("AgriThon 2026 Prototype | Powered by Google Gemini & Streamlit")

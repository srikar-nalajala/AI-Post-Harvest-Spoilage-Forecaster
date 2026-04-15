**🍅 Smart Farm Seller**

Smart Farm Seller 2026 Prototype | Reducing crop Waste through Intelligent Market Matching

**📖 Overview**

harvest loss is a critical challenge for small-scale farmers. Smart Farm Seller is an AI-powered dashboard that helps farmers decide whether to Sell, Store, or Monitor their produce. By combining Computer Vision (Google Gemini) with Live Weather Data, the app predicts spoilage risks and matches crops to the best-priced local Mandis.

**✨ Key Features**

**AI Crop Analysis:** Uses Gemini 2.5 Flash to analyze images of produce and assign a Spoilage Risk Score (1-10).

**Live Weather Integration:** Fetches real-time temperature and humidity via Open-Meteo API to factor in environmental decay triggers.

**Micro-Market Matcher:** Displays live (simulated) prices for major Mandis across Telangana, Andhra Pradesh, Maharashtra, Karnataka, and Tamil Nadu.

**Multilingual Interface:** Fully localized in English, Telugu (తెలుగు), Kannada (ಕನ್ನಡ), Marathi (మరాठी), and Tamil (தமிழ்).

**Intelligent Recommendations: **Dynamic advice based on a combination of crop health and local weather conditions.

**🛠️ Tech Stack**
**Frontend:** Streamlit

**AI/ML:** Google Gemini API (Vision & Analysis)

**Backend:** Python

**Data:** Pandas, Open-Meteo API (Weather), Mock Market Data

**Styling:** Custom Streamlit Theme (config.toml)

**🚀 Getting Started**
**Prerequisites**
**Python 3.9+**

A Google Gemini API Key

**Installation**
Clone the repository:

Bash
git clone https://github.com/your-username/smart-farm-seller.git
cd smart-farm-seller
Install dependencies:

Bash
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add your API key:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
Running the App
Bash
streamlit run main.py
**📂 Project Structure**
**main.py: **The primary Streamlit application entry point.

**modules/:**

**vision.py:** Gemini API integration for image analysis.

**weather.py:** Live weather fetching logic.

**market.py:** Market data management and recommendation engine.

**translations.py:** Multilingual dictionary and logic.

**.streamlit/config.toml:** Custom dark-mode theme settings.

**🛡️ Fallback System**
In case of API rate limits or connectivity issues during live demos, the system includes a Simulation Mode in vision.py to ensure the core workflow remains testable.

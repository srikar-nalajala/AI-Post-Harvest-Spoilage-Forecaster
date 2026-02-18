from modules import weather, market
import os
from dotenv import load_dotenv

load_dotenv()

print("--- Testing Configuration ---")
key = os.getenv("GEMINI_API_KEY")
if key:
    print(f"API Key found: {key[:5]}...")
else:
    print("ERROR: API Key not found in .env")

print("\n--- Testing Weather Module ---")
w = weather.get_weather("Telangana")
print(f"Weather Data: {w}")

print("\n--- Testing Market Module ---")
m = market.get_market_data()
print(f"Market Data Rows: {len(m)}")
print(m.head())

print("\n--- Testing Recommendation Logic ---")
rec = market.get_recommendation(8, w) # High risk
print(f"High Risk Rec: {rec['action']} because {rec['reason']}")

rec_low = market.get_recommendation(2, w) # Low risk
print(f"Low Risk Rec: {rec_low['action']}")

print("\nTests Complete.")

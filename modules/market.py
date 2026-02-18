import pandas as pd
import random

# Mock Market Data for various regions
MARKET_DATA = {
    "Telangana": [
        {"Market": "Bowenpally", "Tomato_Price": 25, "Onion_Price": 30, "Potato_Price": 20, "Chilli_Price": 45, "Brinjal_Price": 35},
        {"Market": "Gudimalkapur", "Tomato_Price": 22, "Onion_Price": 28, "Potato_Price": 18, "Chilli_Price": 42, "Brinjal_Price": 32},
        {"Market": "Erragadda", "Tomato_Price": 24, "Onion_Price": 32, "Potato_Price": 22, "Chilli_Price": 48, "Brinjal_Price": 36},
        {"Market": "Kothapet", "Tomato_Price": 28, "Onion_Price": 35, "Potato_Price": 24, "Chilli_Price": 50, "Brinjal_Price": 40},
        {"Market": "Shamshabad", "Tomato_Price": 20, "Onion_Price": 25, "Potato_Price": 18, "Chilli_Price": 40, "Brinjal_Price": 30},
        {"Market": "Warangal", "Tomato_Price": 23, "Onion_Price": 29, "Potato_Price": 19, "Chilli_Price": 44, "Brinjal_Price": 34},
        {"Market": "Nizamabad", "Tomato_Price": 21, "Onion_Price": 27, "Potato_Price": 20, "Chilli_Price": 42, "Brinjal_Price": 33}
    ],
    "Andhra Pradesh": [
        {"Market": "Guntur", "Tomato_Price": 18, "Onion_Price": 25, "Potato_Price": 22, "Chilli_Price": 60, "Brinjal_Price": 30},
        {"Market": "Vijayawada", "Tomato_Price": 20, "Onion_Price": 28, "Potato_Price": 24, "Chilli_Price": 55, "Brinjal_Price": 35},
        {"Market": "Kurnool", "Tomato_Price": 22, "Onion_Price": 30, "Potato_Price": 25, "Chilli_Price": 58, "Brinjal_Price": 38},
        {"Market": "Tirupati", "Tomato_Price": 24, "Onion_Price": 32, "Potato_Price": 28, "Chilli_Price": 62, "Brinjal_Price": 40},
        {"Market": "Vizag", "Tomato_Price": 26, "Onion_Price": 35, "Potato_Price": 30, "Chilli_Price": 65, "Brinjal_Price": 45},
        {"Market": "Rajahmundry", "Tomato_Price": 19, "Onion_Price": 26, "Potato_Price": 23, "Chilli_Price": 56, "Brinjal_Price": 32}
    ],
    "Karnataka": [
        {"Market": "Kolar", "Tomato_Price": 15, "Onion_Price": 20, "Potato_Price": 25, "Chilli_Price": 40, "Brinjal_Price": 28},
        {"Market": "Chikkaballapur", "Tomato_Price": 16, "Onion_Price": 22, "Potato_Price": 24, "Chilli_Price": 42, "Brinjal_Price": 30},
        {"Market": "Bangalore (KR Market)", "Tomato_Price": 20, "Onion_Price": 28, "Potato_Price": 30, "Chilli_Price": 50, "Brinjal_Price": 40},
        {"Market": "Mysore", "Tomato_Price": 22, "Onion_Price": 30, "Potato_Price": 28, "Chilli_Price": 48, "Brinjal_Price": 38},
        {"Market": "Hubli", "Tomato_Price": 18, "Onion_Price": 25, "Potato_Price": 22, "Chilli_Price": 45, "Brinjal_Price": 35},
        {"Market": "Belgaum", "Tomato_Price": 19, "Onion_Price": 26, "Potato_Price": 20, "Chilli_Price": 44, "Brinjal_Price": 34}
    ],
    "Maharashtra": [
        {"Market": "Pune", "Tomato_Price": 30, "Onion_Price": 40, "Potato_Price": 25, "Chilli_Price": 55, "Brinjal_Price": 45},
        {"Market": "Nashik", "Tomato_Price": 25, "Onion_Price": 15, "Potato_Price": 20, "Chilli_Price": 50, "Brinjal_Price": 40}, 
        {"Market": "Mumbai (Vashi)", "Tomato_Price": 35, "Onion_Price": 45, "Potato_Price": 30, "Chilli_Price": 60, "Brinjal_Price": 50},
        {"Market": "Nagpur", "Tomato_Price": 28, "Onion_Price": 38, "Potato_Price": 22, "Chilli_Price": 52, "Brinjal_Price": 42}
    ],
    "Tamil Nadu": [
        {"Market": "Koyambedu (Chennai)", "Tomato_Price": 32, "Onion_Price": 40, "Potato_Price": 35, "Chilli_Price": 50, "Brinjal_Price": 45},
        {"Market": "Coimbatore", "Tomato_Price": 28, "Onion_Price": 35, "Potato_Price": 30, "Chilli_Price": 48, "Brinjal_Price": 40},
        {"Market": "Madurai", "Tomato_Price": 30, "Onion_Price": 38, "Potato_Price": 32, "Chilli_Price": 52, "Brinjal_Price": 42}
    ]
}

def get_market_data(region="Telangana"):
    """
    Returns a mock DataFrame of market prices for the specified region.
    """
    # Default to Telangana if region not found
    data = MARKET_DATA.get(region, MARKET_DATA["Telangana"])
    
    # Add some random fluctuation to simulate live updates
    fluctuated_data = []
    for m in data:
        new_row = m.copy()
        new_row["Tomato_Price"] += random.randint(-2, 3)
        new_row["Onion_Price"] += random.randint(-3, 5)
        new_row["Potato_Price"] += random.randint(-1, 2)
        new_row["Chilli_Price"] += random.randint(-4, 4)
        new_row["Brinjal_Price"] += random.randint(-2, 2)
        fluctuated_data.append(new_row)
        
    return pd.DataFrame(fluctuated_data)

def get_recommendation(spoilage_score, weather_data):
    """
    Generates a recommendation based on spoilage risk and weather.
    """
    # Logic:
    # High Spoilage Score (8-10) -> Sell Immediately (Risk of total loss).
    # Moderate Score (4-7) -> Check Weather. High humidity accelerates spoilage -> Sell Soon.
    # Low Score (1-3) -> Hold for better price if current price is low, or Sell if price is high.
    
    humidity = weather_data.get("humidity", 50)
    temp = weather_data.get("temperature", 30)
    
    urgency = "LOW"
    action = "HOLD"
    reason = "Produce occurs fresh. Monitor market prices."

    if spoilage_score >= 8:
        urgency = "CRITICAL"
        action = "SELL IMMEDIATELY"
        reason = "Produce shows significant signs of decay. Immediate sale recommended to avoid total loss."
    elif spoilage_score >= 5:
        if humidity > 70 or temp > 35:
            urgency = "HIGH"
            action = "SELL SOON"
            reason = f"Moderate spoilage risk combined with adverse weather (Hum: {humidity}%, Temp: {temp}°C) accelerates decay."
        else:
            urgency = "MEDIUM"
            action = "PLAN SALE"
            reason = "Produce is degrading but weather conditions are stable. Plan sale within 2-3 days."
    else:
        # Low spoilage
        if humidity > 85:
            urgency = "MEDIUM"
            action = "MONITOR CLOSELY"
            reason = "Produce is fresh, but high humidity is a risk factor."
        else:
            urgency = "LOW"
            action = "HOLD / STORE"
            reason = "Produce is in good condition. You can hold for better market prices."

    return {
        "urgency": urgency,
        "action": action,
        "reason": reason
    }

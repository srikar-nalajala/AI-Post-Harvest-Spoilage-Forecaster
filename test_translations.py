from modules import translations

print("--- Testing Translations ---")
print(f"Title (EN): {translations.get_text('title', 'en')}")
print(f"Title (TE): {translations.get_text('title', 'te')}")

print(f"Sell Now (EN): {translations.get_text('sell_now', 'en')}")
print(f"Sell Now (TE): {translations.get_text('sell_now', 'te')}")

assert translations.get_text('title', 'en') == "🍅 AI Post-Harvest Spoilage Forecaster"
assert translations.get_text('title', 'te') == "🍅 పంట కోత అనంతర నష్టం అంచనా"

print("✅ Translations verified.")

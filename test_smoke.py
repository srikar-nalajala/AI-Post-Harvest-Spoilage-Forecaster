try:
    from modules import vision, weather, market, translations
    print("All modules imported successfully.")
except Exception as e:
    print(f"Import failed: {e}")
    exit(1)

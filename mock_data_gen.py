from DataRecord import DataRecord  # <--- This is the Handshake!
import random


def get_raw_business_data(rows=10):
    """Simulates messy data from a legacy system (like old Lotus exports)."""
    names = ["  alex  ", "jOrdan", "sam", "b", "  CHRIS  ", "M", "taylor", "morgan"]
    raw_data = []

    for i in range(rows):
        record = {
            "record_id": 100 + i,
            "user_name": random.choice(names),
            # Intentionally adding some 'out of bounds' scores to test our (ge=0, le=100) rule
            "score": round(random.uniform(-10, 110), 2),
            "email": f"user{i}@snhu.edu" if i % 2 == 0 else None
        }
        raw_data.append(record)
    return raw_data


if __name__ == "__main__":
    data = get_raw_business_data(5)
    print("--- 📝 RAW MESSY DATA ---")
    for row in data:
        print(row)

        # --- THE FINAL HANDSHAKE ---
        if __name__ == "__main__":
            # 1. Generate the mess (what you just saw in your terminal)
            raw_list = get_raw_business_data(5)

            print("\n--- 🛡️ ACTIVATING THE BOUNCER (Pydantic V2) ---")

            for row in raw_list:
                try:
                    # 2. This turns the 'dict' into a 'Strong DataRecord'
                    clean_record = DataRecord(**row)
                    print(f"✅ ACCEPTED: {clean_record.user_name} | Score: {clean_record.score}")
                except Exception as e:
                    # 3. This catches the 'M' names and '109.36' scores!
                    print(f"❌ REJECTED: ID {row['record_id']} | Reason: {e}")
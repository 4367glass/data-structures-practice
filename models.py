from pydantic import BaseModel, Field, field_validator
from typing import Optional

# This is your 'Strong Structure' for Pydantic V2
class DataRecord(BaseModel):
    record_id: int
    user_name: str
    score: float = Field(ge=0, le=100)
    email: Optional[str] = "No Email Provided"

    # The Modern 'Bouncer' (Validator)
    @field_validator('user_name')
    @classmethod
    def clean_name(cls, v: str):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters!')
        return v.strip().title() # Automatically cleans: "  alex  " -> "Alex"

# --- TEST AREA ---
if __name__ == "__main__":
    try:
        # Testing with 'dirty' data
        test = DataRecord(record_id=101, user_name="  alex  ", score=95)
        print(f"✅ SUCCESS: {test.user_name} is validated and cleaned!")
    except Exception as e:
        print(f"❌ ERROR: {e}")
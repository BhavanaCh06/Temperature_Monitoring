
import os
from google import genai

print("Step 1: Checking API key...")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY is missing.")
    raise SystemExit(1)

print("Step 2: Creating Gemini client...")
client = genai.Client(api_key=api_key)

print("Step 3: Sending request to Gemini...")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Reply with exactly: Hello!"
    )

    print("Step 4: Response received!")
    print(response.text)

except Exception as error:
    print("Request failed:")
    print(type(error).__name__)
    print(error)

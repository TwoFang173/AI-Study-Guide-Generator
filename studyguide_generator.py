import openai
import json

# Load API key from OpenAI
API_KEY = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=API_KEY)

# Unstructed class note
class_notes = """
The water cycle, also known as the hydrologic cycle, describes the continuous movement of water on, above, and below the surface of the Earth. This cycle is vital for ecosystems and climate. The main stages are evaporation, where water turns into vapor; condensation, where vapor forms clouds; precipitation, where water falls back to Earth as rain or snow; and collection, where water gathers in rivers, lakes, and oceans.
"""

# The prompt for a simple JSON object with two keys
# The detailed system prompt for our final application
system_prompt = """
You are an expert academic assistant. Your task is to take the provided class notes and generate a structured study guide.
You must format your output as a single JSON object with the following keys:
- "subject": A string with the general subject.
- "main_topic": A string with the main topic.
- "summary_points": A list of 3-5 concise, bullet-point style summaries of the main concepts.
- "key_terms": A list of important terms from the text. Each term must be a JSON object with a "term" key and a "definition" key.
"""

try:
    response = client.responses.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": class_notes}
        ],
        response_format={"type": "json_object"}
    )
    
    # Extract the JSON string from the response
    study_guide = json.loads(response.output_text)

    # --- Print the formatted study guide ---
    print("--- AI-Generated Study Guide ---")

    print(f"\nSubject: {study_guide['subject']}")
    print(f"Main Topic: {study_guide['main_topic']}")
    
    print("\n✅ Summary Points:")
    for point in study_guide["summary_points"]:
        print(f"- {point}")

    print("\n🔑 Key Terms:")
    for item in study_guide["key_terms"]:
        # Notice the nested access: item['term'] and item['definition']
        print(f"- {item['term']}: {item['definition']}")
        
except Exception as e:
    print(f"An error occurred: {e}")
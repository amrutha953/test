import google.generativeai as genai

genai.configure(api_key="AIzaSyAsHzAZ2mThHw_bqc7KYTYHjNKvE-pxwCM")
# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content
response = model.generate_content("What is the meaning of life?")
print(response.text)
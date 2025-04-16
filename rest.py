
import requests
import os

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("API_KEY"))}
query = "In one word, what is the capital of France?"
data = {"messages": [{"role": "user", "content": query}], "model": "deepseek/deepseek-chat-v3-0324:free"}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Response:", response.json()["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)
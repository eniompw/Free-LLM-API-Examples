# Free-LLM-API-Examples

A collection of examples and resources for accessing free and alternative LLM APIs with OpenAI-compatible interfaces.

## Overview

This repository provides examples of how to interact with various Large Language Model APIs that are either free to use (with certain limitations) or provide alternatives to the official OpenAI services. All of these APIs follow the OpenAI API format, making them easy to integrate into existing applications.

## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)

## API Endpoints

The file [free-llm-api-endpoints.md.md](free-llm-api-endpoints.md.md) contains a curated list of API endpoints from various providers including:

- OpenRouter
- Chutes
- Groq
- Azure AI
- Mistral AI
- NVIDIA
- SambaNova

Each listing includes the endpoint URL and brief notes about the service.

## Example Usage

### Python REST Example

The [rest.py](rest.py) file demonstrates how to make a basic API call to OpenRouter using Python:

```python
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
```

### Additional Example

The [llm_api_example.py](llm_api_example.py) file provides another example of interacting with a compatible LLM API. See the script for details.

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Free-LLM-API-Examples.git
   cd Free-LLM-API-Examples
   ```

2. Set up your API key as an environment variable:
   ```bash
   export API_KEY=your_api_key_here
   ```

3. Run the example script:
   ```bash
   python rest.py
   ```

## License

This project is licensed under the terms of the license included in the repository.

## Disclaimer

This repository is not affiliated with OpenAI or any of the API providers listed. Service availability, pricing, and terms may change over time. Always refer to the official documentation of each provider.
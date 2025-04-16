# Examples of Free LLM API Usage

This document provides examples of how to interact with various OpenAI-compatible LLM APIs using Python. Each example demonstrates how to access a specific provider's API using a similar pattern to our [rest.py](rest.py) reference implementation.

## Overview

All examples follow a similar structure:
1. Make HTTP requests to the provider's API endpoint
2. Pass your API key via authorization headers
3. Structure your prompt in OpenAI-compatible format
4. Process the API response

## Provider-Specific Examples

### Groq

[Groq Example](https://github.com/eniompw/GroqGPT/blob/main/rest.py) - Demonstrates how to use Groq's API, known for extremely fast inference speeds.

### Chutes

[Chutes API Example](https://github.com/eniompw/Chutes-API/blob/main/rest.py) - Shows how to access Chutes' API which offers a free tier for developers.

### GitHub Models

[GitHub Models Example](https://github.com/eniompw/GitHubModels/blob/main/rest.py) - Provides code for accessing GitHub's models.

### Mistral AI

[Mistral Example](https://github.com/eniompw/Mistral/blob/main/rest.py) - Code sample for Mistral AI's models, showcasing their specialized language capabilities.

### NVIDIA NIM

[NVIDIA Example](https://github.com/eniompw/NVIDIA-NIM/blob/main/rest.py) - Demonstrates integration with NVIDIA's NIM platform for AI inference.

### SambaNova

[SambaNova Example](https://github.com/eniompw/SambaNovaREST/blob/main/rest.py) - Shows how to use SambaNova's fast API service.

### Pixtral

[Pixtral Example](https://github.com/eniompw/Pixtral/blob/main/app.py) - Demonstrates how to use Pixtral's multimodal capabilities for image and text processing.

### Google Gemini

[Gemini API Example](https://github.com/eniompw/GeminiAPI/blob/main/dev/rest.py) - Shows how to interact with Google's Gemini models through their API.

## Usage Tips

- Create an environment variable called `API_KEY` with your provider's key
- Most examples can be adapted to work with other providers by changing the endpoint URL
- For detailed endpoint information, see our [API URLs documentation](api-urls.md)

## Basic Implementation Pattern

```python
import requests
import os

url = "https://provider-specific-url.com/api/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("API_KEY"))}
query = "Your prompt here"
data = {
    "messages": [{"role": "user", "content": query}], 
    "model": "provider-specific-model"
}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Response:", response.json()["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)
```
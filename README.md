# Free-LLM-API-Examples

## Overview

This repository provides examples of how to interact with various Large Language Model APIs that are either free to use (with certain limitations) or provide alternatives to the official OpenAI services. All of these APIs follow the OpenAI API format, making them easy to integrate into existing applications.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Provider Integrations](#provider-integrations)
- [Usage](#usage)
- [Example Usage](#example-usage)
- [Usage Tips](#usage-tips)
- [Resources](#resources)
- [Contributing](#contributing)
- [Reporting Issues](#reporting-issues)
- [Code of Conduct](#code-of-conduct)
- [Disclaimer](#disclaimer)


## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)

## Provider Integrations

| Provider     | Endpoint URL                                           | Notes                                  | Example                                              |
|--------------|--------------------------------------------------------|----------------------------------------|------------------------------------------------------|
| OpenRouter   | https://openrouter.ai/api/v1/chat/completions         | Provides access to multiple models     | [Python REST Example](rest.py)                       |
| Chutes       | https://llm.chutes.ai/v1/chat/completions             | Free tier available                    | [Chutes Example](https://github.com/eniompw/Chutes-API/blob/main/rest.py) |
| Groq         | https://api.groq.com/openai/v1/chat/completions       | Known for fast inference               | [Groq Example](https://github.com/eniompw/GroqGPT/blob/main/rest.py)    |
| Azure AI     | https://models.inference.ai.azure.com/chat/completions | Microsoft's AI services                                                          |
| Mistral AI   | https://api.mistral.ai/v1/chat/completions            | Offers various Mistral models          | [Mistral Example](https://github.com/eniompw/Mistral/blob/main/rest.py) |
| NVIDIA       | https://integrate.api.nvidia.com/v1/chat/completions  | NVIDIA AI platform                     | [NVIDIA Example](https://github.com/eniompw/NVIDIA-NIM/blob/main/rest.py) |
| SambaNova    | https://fast-api.snova.ai/v1/chat/completions         | Fast API service                       | [SambaNova Example](https://github.com/eniompw/SambaNovaREST/blob/main/rest.py) |
| Tavily       | https://tavily.com                                     | Free Search API: 1,000 API credits/month, no credit card required                                           |
| Pixtral      | n/a                                                    | Multimodal image & text                | [Pixtral Example](https://github.com/eniompw/Pixtral/blob/main/app.py)  |
| Google Gemini| n/a                                                    | Google's Gemini models                 | [Gemini Example](https://github.com/eniompw/GeminiAPI/blob/main/dev/rest.py) |

### Usage

These endpoints generally follow the OpenAI API format. Use with appropriate authentication as required by each provider.

```python
import requests
import os

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": "Bearer " + os.environ.get("API_KEY", "")}
query = "In one word, what is the capital of France?"
data = {"messages": [{"role": "user", "content": query}], "model": "deepseek/deepseek-chat-v3-0324:free"}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Response:", response.json()["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)
```

Refer to `llm_quickstart.py` for a complete script and additional provider examples.

## Usage Tips

- Set your API key environment variable:
  ```bash
  export API_KEY="your_api_key_here"
  ```
- Adapt endpoints to other providers by updating the URL and model parameters.
- Watch out for rate limits and monitor your provider’s quotas.
- Some services require region or resource-specific endpoint configuration (e.g., Azure).

## Disclaimer

This repository is not affiliated with OpenAI or any of the API providers listed. Service availability, pricing, and terms may change over time. Always refer to the official documentation of each provider.
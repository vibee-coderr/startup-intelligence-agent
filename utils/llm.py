import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
REQUEST_TIMEOUT = 60  # seconds

# Validate API key on module load
if not OPENROUTER_API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY not found in environment variables. "
        "Please set OPENROUTER_API_KEY in your .env file."
    )


def generate_response(prompt):
    """
    Generate a response using OpenRouter API.
    
    Args:
        prompt (str): The user prompt/query
        
    Returns:
        str: The response text from the LLM
        
    Raises:
        ValueError: If API key is missing
        requests.RequestException: If API request fails
        Exception: For invalid responses or other errors
    """
    try:
        # Debug: Configuration
        print(f"\n[DEBUG] === OpenRouter API Call ===")
        print(f"[DEBUG] Endpoint: {OPENROUTER_API_URL}")
        print(f"[DEBUG] Model: {OPENROUTER_MODEL}")
        print(f"[DEBUG] API Key Present: {'Yes' if OPENROUTER_API_KEY else 'No'}")
        print(f"[DEBUG] Prompt Length: {len(prompt)} chars")
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/soul-kamal/phase1",
            "X-Title": "Phase1 AI Agents"
        }
        
        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0,
            "max_tokens": 4096
        }
        
        print(f"[DEBUG] Headers: {dict(headers)}")
        print(f"[DEBUG] Payload Keys: {list(payload.keys())}")
        print(f"[DEBUG] Sending POST request...")
        
        response = requests.post(
            OPENROUTER_API_URL,
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT
        )
        
        print(f"[DEBUG] Status Code: {response.status_code}")
        print(f"[DEBUG] Response Headers: {dict(response.headers)}")
        
        # Check for HTTP errors
        if response.status_code != 200:
            print(f"[DEBUG] Response Body: {response.text}")
        
        response.raise_for_status()
        
        # Parse response
        response_data = response.json()
        
        # Validate response structure
        if "choices" not in response_data or not response_data["choices"]:
            raise ValueError(
                f"Invalid OpenRouter API response structure: {response_data}"
            )
        
        # Extract message content
        message_content = response_data["choices"][0].get("message", {}).get("content")
        
        if not message_content:
            raise ValueError(
                "No content in OpenRouter API response. "
                f"Response: {response_data}"
            )
        
        return message_content
        
    except requests.exceptions.Timeout:
        error_msg = (
            f"OpenRouter API request timed out after {REQUEST_TIMEOUT} seconds. "
            "Please try again or increase REQUEST_TIMEOUT in llm.py."
        )
        raise requests.RequestException(error_msg) from None
        
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        error_detail = e.response.text
        
        print(f"[DEBUG] HTTPError Status {status_code}: {error_detail}")
        
        if status_code == 401:
            error_msg = (
                "OpenRouter API authentication failed. "
                "Please verify your OPENROUTER_API_KEY in .env file."
            )
        elif status_code == 405:
            error_msg = (
                "405 Method Not Allowed - Endpoint issue. "
                f"URL: {OPENROUTER_API_URL}"
            )
        elif status_code == 429:
            error_msg = (
                "OpenRouter API rate limit exceeded. "
                "Please wait before retrying."
            )
        elif status_code >= 500:
            error_msg = (
                f"OpenRouter API server error ({status_code}). "
                "Please try again later."
            )
        else:
            error_msg = (
                f"OpenRouter API HTTP error {status_code}: {error_detail}"
            )
        
        print(f"[DEBUG] Error Message: {error_msg}")
        raise requests.RequestException(error_msg) from None
        
    except requests.exceptions.RequestException as e:
        error_msg = f"OpenRouter API request failed: {str(e)}"
        raise requests.RequestException(error_msg) from e
        
    except ValueError as e:
        # Re-raise ValueError for invalid responses
        raise ValueError(f"OpenRouter API response error: {str(e)}") from e
        
    except Exception as e:
        error_msg = f"Unexpected error calling OpenRouter API: {str(e)}"
        raise Exception(error_msg) from e
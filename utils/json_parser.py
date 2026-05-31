import json
import re

def parse_json(text):
    """
    Extract and parse the first valid JSON object from text.
    Handles Llama3 responses with extra text before/after JSON.
    """
    text = text.strip()
    
    # Try direct parsing first (fastest path)
    try:
        decoder = json.JSONDecoder()
        obj, _ = decoder.raw_decode(text)
        return obj
    except json.JSONDecodeError:
        pass
    
    # Try to find JSON-like blocks in the text
    # Look for text between { and }
    json_pattern = r'\{[^{}]*\}'
    match = re.search(json_pattern, text, re.DOTALL)
    
    if match:
        json_str = match.group()
        try:
            decoder = json.JSONDecoder()
            obj, _ = decoder.raw_decode(json_str)
            return obj
        except json.JSONDecodeError:
            pass
    
    # If all else fails, return empty dict with error info
    return {
        "error": "Could not parse JSON from response",
        "raw_text": text[:200]  # Return first 200 chars for debugging
    }
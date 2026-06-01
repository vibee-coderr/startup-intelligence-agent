import json

def parse_json(text):

    text = text.strip()

    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

    decoder = json.JSONDecoder()

    try:
        obj, _ = decoder.raw_decode(
            text
        )

        return obj

    except Exception:

        return {
            "error": "Could not parse JSON from response",
            "raw_text": text[:500]
        }
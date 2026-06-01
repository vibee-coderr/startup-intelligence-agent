from utils.llm import generate_response

def generate_comparison(
    company1,
    analysis1,
    company2,
    analysis2
):

    prompt = f"""
Compare these two companies.

Company 1: {company1}

Data:
{analysis1}

Company 2: {company2}

Data:
{analysis2}

Provide:

- Innovation Winner
- Market Position Winner
- Growth Potential Winner
- Investment Attractiveness Winner
- Overall Winner

Keep it concise.
"""
    return generate_response(
        prompt
    )
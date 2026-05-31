from utils.llm import generate_response

def generate_report(
    analysis_data,
    competitor_data,
    swot_data
):

    with open(
        "prompts/report_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        prompt = file.read()

    final_prompt = f"""
    {prompt}

    Analysis Data:
    {analysis_data}

    Competitor Data:
    {competitor_data}

    SWOT Data:
    {swot_data}
    """

    return generate_response(final_prompt)
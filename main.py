from agents.analyst import analyze_company
from agents.competitor_agent import find_competitors
from agents.swot_agent import generate_swot
from agents.report_agent import generate_report

company = input(
    "Enter Company Name: "
)

# Agent 1
analysis_data = analyze_company(company)

# Agent 2
competitor_data = find_competitors(company)

# Agent 3
swot_data = generate_swot(company)

# Agent 4
final_report = generate_report(
    analysis_data,
    competitor_data,
    swot_data
)

print()
print("=" * 50)
print("FINAL REPORT")
print("=" * 50)
print()

print(final_report)
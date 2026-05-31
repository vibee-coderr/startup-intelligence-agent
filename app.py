import streamlit as st

from agents.analyst import analyze_company
from agents.competitor_agent import find_competitors
from agents.swot_agent import generate_swot
from agents.report_agent import generate_report

st.set_page_config(
    page_title="AI Startup Intelligence Agent",
    layout="wide"
)

st.title("🚀 AI Startup Intelligence Agent")

company = st.text_input(
    "Enter Company Name"
)

if st.button("Analyze"):

    with st.spinner("Running AI Agents..."):

        analysis_data = analyze_company(
            company
        )

        competitor_data = find_competitors(
            company
        )

        swot_data = generate_swot(
            company
        )

        final_report = generate_report(
            analysis_data,
            competitor_data,
            swot_data
        )

    st.success("Analysis Complete")

    st.divider()

    st.subheader("🏢 Company Overview")

    st.write(
        analysis_data.get(
            "overview",
            "No overview available"
        )
    )

    st.divider()

    st.subheader("📦 Products")

    for product in analysis_data.get(
        "products",
        []
    ):
        st.write(f"• {product}")

    st.divider()

    st.subheader("💰 Revenue Sources")

    for source in analysis_data.get(
        "revenue_sources",
        []
    ):
        st.write(f"• {source}")

    st.divider()

    st.subheader("🏆 Competitors")

    for competitor in competitor_data.get(
        "competitors",
        []
    ):
        st.write(f"• {competitor}")

    st.divider()

    st.subheader("📊 SWOT Analysis")

    swot = swot_data.get("swot", {})

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Strengths")

        for item in swot.get(
            "strengths",
            []
        ):
            st.write(f"• {item}")

        st.markdown("### Opportunities")

        for item in swot.get(
            "opportunities",
            []
        ):
            st.write(f"• {item}")

    with col2:

        st.markdown("### Weaknesses")

        for item in swot.get(
            "weaknesses",
            []
        ):
            st.write(f"• {item}")

        st.markdown("### Threats")

        for item in swot.get(
            "threats",
            []
        ):
            st.write(f"• {item}")

    st.divider()

    st.subheader("📈 Investment Summary")

    st.write(
        analysis_data.get(
            "investment_summary",
            "No summary available"
        )
    )

    st.divider()

    st.subheader("📝 Executive Report")

    st.write(final_report)
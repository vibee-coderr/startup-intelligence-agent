import streamlit as st

from agents.analyst import analyze_company
from agents.competitor_agent import find_competitors
from agents.swot_agent import generate_swot
from agents.report_agent import generate_report
from agents.comparison_agent import generate_comparison

st.set_page_config(
    page_title="AI Startup Intelligence Agent",
    layout="wide"
)

st.title("🚀 AI Startup Intelligence Agent")

# Mode selection
mode = st.radio(
    "Select Mode",
    ["Single Company Analysis", "Company Comparison"],
    horizontal=True
)

st.divider()

if mode == "Single Company Analysis":
    
    company = st.text_input("Enter Company Name")

    if st.button("Analyze"):

        with st.spinner("Running AI Agents..."):

            analysis_data = analyze_company(company)
            competitor_data = find_competitors(company)
            swot_data = generate_swot(company)
            final_report = generate_report(analysis_data, competitor_data, swot_data)

        st.success("Analysis Complete")

        st.divider()

        st.subheader("🏢 Company Overview")
        st.write(analysis_data.get("overview", "No overview available"))

        st.divider()

        st.subheader("📦 Products")
        for product in analysis_data.get("products", []):
            st.write(f"• {product}")

        st.divider()

        st.subheader("💰 Revenue Sources")
        for source in analysis_data.get("revenue_sources", []):
            st.write(f"• {source}")

        st.divider()

        st.subheader("🏆 Competitors")
        for competitor in competitor_data.get("competitors", []):
            st.write(f"• {competitor}")

        st.divider()

        st.subheader("📊 SWOT Analysis")
        swot = swot_data.get("swot", {})

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Strengths")
            for item in swot.get("strengths", []):
                st.write(f"• {item}")

            st.markdown("### Opportunities")
            for item in swot.get("opportunities", []):
                st.write(f"• {item}")

        with col2:
            st.markdown("### Weaknesses")
            for item in swot.get("weaknesses", []):
                st.write(f"• {item}")

            st.markdown("### Threats")
            for item in swot.get("threats", []):
                st.write(f"• {item}")

        st.divider()

        st.subheader("📈 Investment Summary")
        st.write(analysis_data.get("investment_summary", "No summary available"))

        st.divider()

        st.subheader("📝 Executive Report")
        st.write(final_report)

# Company Comparison Mode

else:

    col1, col2 = st.columns(2)

    with col1:
        company1 = st.text_input(
            "Enter First Company Name",
            key="company1"
        )

    with col2:
        company2 = st.text_input(
            "Enter Second Company Name",
            key="company2"
        )

    if st.button("Compare"):

        if not company1 or not company2:
            st.error(
                "Please enter both company names"
            )

        else:

            with st.spinner(
                "Analyzing companies..."
            ):

                try:

                    analysis1 = analyze_company(company1)
                    analysis2 = analyze_company(company2)

                    competitors1 = find_competitors(company1)
                    competitors2 = find_competitors(company2)

                    swot1 = generate_swot(company1)
                    swot2 = generate_swot(company2)

                    comparison = generate_comparison(
                        company1,
                        analysis1,
                        company2,
                        analysis2
                    )

                except Exception as e:

                    st.error(
                        f"Error: {e}"
                    )

                    st.stop()

            st.success(
                "Comparison Complete"
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(company1)

                st.write(
                    analysis1.get(
                        "overview",
                        "No overview available"
                    )
                )

                st.markdown(
                    "### Products"
                )

                for product in analysis1.get(
                    "products",
                    []
                ):
                    st.write(
                        f"• {product}"
                    )

                st.markdown(
                    "### Revenue Sources"
                )

                for source in analysis1.get(
                    "revenue_sources",
                    []
                ):
                    st.write(
                        f"• {source}"
                    )

                st.markdown(
                    "### Investment Summary"
                )

                st.write(
                    analysis1.get(
                        "investment_summary",
                        "N/A"
                    )
                )

                st.markdown("### Competitors")

                for competitor in competitors1.get(
                    "competitors",
                    []
                ):
                    st.write(f"• {competitor}")

                st.markdown("### SWOT")

                swot = swot1.get("swot", swot1)

                st.markdown("#### Strengths")
                for item in swot.get("strengths", []):
                    st.write(f"• {item}")

                st.markdown("#### Weaknesses")
                for item in swot.get("weaknesses", []):
                    st.write(f"• {item}")

                st.markdown("#### Opportunities")
                for item in swot.get("opportunities", []):
                    st.write(f"• {item}")

                st.markdown("#### Threats")
                for item in swot.get("threats", []):
                    st.write(f"• {item}")

            with col2:

                st.subheader(company2)

                st.write(
                    analysis2.get(
                        "overview",
                        "No overview available"
                    )
                )

                st.markdown(
                    "### Products"
                )

                for product in analysis2.get(
                    "products",
                    []
                ):
                    st.write(
                        f"• {product}"
                    )

                st.markdown(
                    "### Revenue Sources"
                )

                for source in analysis2.get(
                    "revenue_sources",
                    []
                ):
                    st.write(
                        f"• {source}"
                    )

                st.markdown(
                    "### Investment Summary"
                )

                st.write(
                    analysis2.get(
                        "investment_summary",
                        "N/A"
                    )
                )

                st.markdown("### Competitors")

                for competitor in competitors2.get(
                    "competitors",
                    []
                ):
                    st.write(f"• {competitor}")

                st.markdown("### SWOT")

                swot = swot2.get("swot", swot2)

                st.markdown("#### Strengths")
                for item in swot.get("strengths", []):
                    st.write(f"• {item}")

                st.markdown("#### Weaknesses")
                for item in swot.get("weaknesses", []):
                    st.write(f"• {item}")

                st.markdown("#### Opportunities")
                for item in swot.get("opportunities", []):
                    st.write(f"• {item}")

                st.markdown("#### Threats")
                for item in swot.get("threats", []):
                    st.write(f"• {item}")

            st.divider()

            st.markdown("### 🏆 Comparison Verdict")
            st.markdown(comparison)
            
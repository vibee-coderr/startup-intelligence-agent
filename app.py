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

else:  # Company Comparison mode
    
    col1, col2 = st.columns(2)

    with col1:
        company1 = st.text_input("Enter First Company Name", key="company1")

    with col2:
        company2 = st.text_input("Enter Second Company Name", key="company2")

    if st.button("Compare"):
        
        if not company1 or not company2:
            st.error("Please enter both company names")
        else:

            with st.spinner("Analyzing both companies and generating comparison..."):

                # Analyze Company 1
                analysis1 = analyze_company(company1)
                competitor1 = find_competitors(company1)
                swot1 = generate_swot(company1)

                # Analyze Company 2
                analysis2 = analyze_company(company2)
                competitor2 = find_competitors(company2)
                swot2 = generate_swot(company2)

                # Generate comparison
                comparison = generate_comparison(
                    company1, analysis1, competitor1, swot1,
                    company2, analysis2, competitor2, swot2
                )

            st.success("Comparison Complete")

            st.divider()

            # Side-by-side comparison
            st.subheader("📊 Side-by-Side Comparison")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"### {company1}")
                
                st.markdown("**Overview**")
                st.write(analysis1.get("overview", "N/A"))
                
                st.markdown("**Products**")
                for product in analysis1.get("products", []):
                    st.write(f"• {product}")
                
                st.markdown("**Revenue Sources**")
                for source in analysis1.get("revenue_sources", []):
                    st.write(f"• {source}")
                
                st.markdown("**Competitors**")
                for competitor in competitor1.get("competitors", []):
                    st.write(f"• {competitor}")

            with col2:
                st.markdown(f"### {company2}")
                
                st.markdown("**Overview**")
                st.write(analysis2.get("overview", "N/A"))
                
                st.markdown("**Products**")
                for product in analysis2.get("products", []):
                    st.write(f"• {product}")
                
                st.markdown("**Revenue Sources**")
                for source in analysis2.get("revenue_sources", []):
                    st.write(f"• {source}")
                
                st.markdown("**Competitors**")
                for competitor in competitor2.get("competitors", []):
                    st.write(f"• {competitor}")

            st.divider()

            # SWOT Comparison
            st.subheader("📈 SWOT Analysis Comparison")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"### {company1} SWOT")
                swot = swot1.get("swot", {})
                
                st.markdown("**Strengths**")
                for item in swot.get("strengths", []):
                    st.write(f"• {item}")
                
                st.markdown("**Weaknesses**")
                for item in swot.get("weaknesses", []):
                    st.write(f"• {item}")
                
                st.markdown("**Opportunities**")
                for item in swot.get("opportunities", []):
                    st.write(f"• {item}")
                
                st.markdown("**Threats**")
                for item in swot.get("threats", []):
                    st.write(f"• {item}")

            with col2:
                st.markdown(f"### {company2} SWOT")
                swot = swot2.get("swot", {})
                
                st.markdown("**Strengths**")
                for item in swot.get("strengths", []):
                    st.write(f"• {item}")
                
                st.markdown("**Weaknesses**")
                for item in swot.get("weaknesses", []):
                    st.write(f"• {item}")
                
                st.markdown("**Opportunities**")
                for item in swot.get("opportunities", []):
                    st.write(f"• {item}")
                
                st.markdown("**Threats**")
                for item in swot.get("threats", []):
                    st.write(f"• {item}")

            st.divider()

            # Comparison Verdict
            st.subheader("🏆 Comparison Verdict")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                innovation = comparison.get("innovation_winner", {})
                st.metric(
                    "Innovation Winner",
                    innovation.get("company", "N/A"),
                    f"Score: {innovation.get('score', 'N/A')}"
                )
                st.write(innovation.get("reason", ""))

            with col2:
                market = comparison.get("market_position_winner", {})
                st.metric(
                    "Market Position Winner",
                    market.get("company", "N/A"),
                    f"Score: {market.get('score', 'N/A')}"
                )
                st.write(market.get("reason", ""))

            with col3:
                growth = comparison.get("growth_potential_winner", {})
                st.metric(
                    "Growth Potential Winner",
                    growth.get("company", "N/A"),
                    f"Score: {growth.get('score', 'N/A')}"
                )
                st.write(growth.get("reason", ""))

            with col4:
                overall = comparison.get("overall_winner", {})
                st.metric(
                    "Overall Winner",
                    overall.get("company", "N/A"),
                    f"Score: {overall.get('score', 'N/A')}"
                )
                st.write(overall.get("reason", ""))
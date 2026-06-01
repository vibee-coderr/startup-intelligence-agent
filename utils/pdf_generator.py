from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
from io import BytesIO


def generate_pdf_report(company_name, analysis_data, competitor_data, swot_data, final_report):
    """
    Generate a professional PDF report for a company analysis.
    
    Args:
        company_name: Name of the company
        analysis_data: Dictionary containing company overview, products, revenue sources, etc.
        competitor_data: Dictionary containing competitors list
        swot_data: Dictionary containing SWOT analysis
        final_report: String containing the executive report
    
    Returns:
        BytesIO object containing the PDF data
    """
    
    # Create a BytesIO object to store PDF data
    pdf_buffer = BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f77e1'),
        spaceAfter=12,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1f77e1'),
        spaceAfter=8,
        spaceBefore=8
    )
    
    normal_style = styles['Normal']
    
    # Build PDF content
    story = []
    
    # Title and date
    story.append(Paragraph(f"📊 {company_name}", title_style))
    story.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Company Overview
    story.append(Paragraph("🏢 Company Overview", heading_style))
    overview_text = analysis_data.get("overview", "No overview available")
    story.append(Paragraph(overview_text, normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Products
    story.append(Paragraph("📦 Products", heading_style))
    products = analysis_data.get("products", [])
    if products:
        for product in products:
            story.append(Paragraph(f"• {product}", normal_style))
    else:
        story.append(Paragraph("No products available", normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Revenue Sources
    story.append(Paragraph("💰 Revenue Sources", heading_style))
    revenue_sources = analysis_data.get("revenue_sources", [])
    if revenue_sources:
        for source in revenue_sources:
            story.append(Paragraph(f"• {source}", normal_style))
    else:
        story.append(Paragraph("No revenue sources available", normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Competitors
    story.append(Paragraph("🏆 Competitors", heading_style))
    competitors = competitor_data.get("competitors", [])
    if competitors:
        for competitor in competitors:
            story.append(Paragraph(f"• {competitor}", normal_style))
    else:
        story.append(Paragraph("No competitors identified", normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Page break before SWOT
    story.append(PageBreak())
    
    # SWOT Analysis
    story.append(Paragraph("📊 SWOT Analysis", heading_style))
    swot = swot_data.get("swot", {})
    
    # Strengths
    story.append(Paragraph("Strengths", styles['Heading3']))
    strengths = swot.get("strengths", [])
    if strengths:
        for item in strengths:
            story.append(Paragraph(f"• {item}", normal_style))
    else:
        story.append(Paragraph("• No strengths identified", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Weaknesses
    story.append(Paragraph("Weaknesses", styles['Heading3']))
    weaknesses = swot.get("weaknesses", [])
    if weaknesses:
        for item in weaknesses:
            story.append(Paragraph(f"• {item}", normal_style))
    else:
        story.append(Paragraph("• No weaknesses identified", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Opportunities
    story.append(Paragraph("Opportunities", styles['Heading3']))
    opportunities = swot.get("opportunities", [])
    if opportunities:
        for item in opportunities:
            story.append(Paragraph(f"• {item}", normal_style))
    else:
        story.append(Paragraph("• No opportunities identified", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Threats
    story.append(Paragraph("Threats", styles['Heading3']))
    threats = swot.get("threats", [])
    if threats:
        for item in threats:
            story.append(Paragraph(f"• {item}", normal_style))
    else:
        story.append(Paragraph("• No threats identified", normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Investment Summary
    story.append(Paragraph("📈 Investment Summary", heading_style))
    investment_summary = analysis_data.get("investment_summary", "No summary available")
    story.append(Paragraph(investment_summary, normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Page break before Executive Report
    story.append(PageBreak())
    
    # Executive Report
    story.append(Paragraph("📝 Executive Report", heading_style))
    story.append(Paragraph(final_report, normal_style))
    
    # Build PDF
    doc.build(story)
    
    # Reset buffer position to beginning
    pdf_buffer.seek(0)
    
    return pdf_buffer


def generate_comparison_pdf_report(company1_name, analysis1, competitor1, swot1, company2_name, analysis2, competitor2, swot2, comparison):
    """
    Generate a professional PDF report for a company comparison.
    
    Args:
        company1_name: Name of first company
        analysis1: Dictionary containing first company analysis
        competitor1: Dictionary containing first company competitors
        swot1: Dictionary containing first company SWOT
        company2_name: Name of second company
        analysis2: Dictionary containing second company analysis
        competitor2: Dictionary containing second company competitors
        swot2: Dictionary containing second company SWOT
        comparison: String containing the comparison verdict
    
    Returns:
        BytesIO object containing the PDF data
    """
    
    # Create a BytesIO object to store PDF data
    pdf_buffer = BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f77e1'),
        spaceAfter=12,
        alignment=1  # Center alignment
    )
    
    comparison_title_style = ParagraphStyle(
        'ComparisonTitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1f77e1'),
        spaceAfter=10,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1f77e1'),
        spaceAfter=8,
        spaceBefore=8
    )
    
    normal_style = styles['Normal']
    
    # Build PDF content
    story = []
    
    # Title and date
    story.append(Paragraph(f"📊 Company Comparison Report", title_style))
    story.append(Paragraph(f"{company1_name} vs {company2_name}", comparison_title_style))
    story.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Company 1 Section
    story.append(Paragraph(f"🏢 {company1_name}", heading_style))
    
    # Overview
    story.append(Paragraph("Overview", styles['Heading3']))
    overview_text = analysis1.get("overview", "No overview available")
    story.append(Paragraph(overview_text, normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Products
    story.append(Paragraph("Products", styles['Heading3']))
    products = analysis1.get("products", [])
    if products:
        for product in products:
            story.append(Paragraph(f"• {product}", normal_style))
    else:
        story.append(Paragraph("• No products available", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Revenue Sources
    story.append(Paragraph("Revenue Sources", styles['Heading3']))
    revenue_sources = analysis1.get("revenue_sources", [])
    if revenue_sources:
        for source in revenue_sources:
            story.append(Paragraph(f"• {source}", normal_style))
    else:
        story.append(Paragraph("• No revenue sources available", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Competitors
    story.append(Paragraph("Competitors", styles['Heading3']))
    competitors = competitor1.get("competitors", [])
    if competitors:
        for comp in competitors:
            story.append(Paragraph(f"• {comp}", normal_style))
    else:
        story.append(Paragraph("• No competitors identified", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Investment Summary
    story.append(Paragraph("Investment Summary", styles['Heading3']))
    investment_summary = analysis1.get("investment_summary", "No summary available")
    story.append(Paragraph(investment_summary, normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Page break
    story.append(PageBreak())
    
    # Company 2 Section
    story.append(Paragraph(f"🏢 {company2_name}", heading_style))
    
    # Overview
    story.append(Paragraph("Overview", styles['Heading3']))
    overview_text = analysis2.get("overview", "No overview available")
    story.append(Paragraph(overview_text, normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Products
    story.append(Paragraph("Products", styles['Heading3']))
    products = analysis2.get("products", [])
    if products:
        for product in products:
            story.append(Paragraph(f"• {product}", normal_style))
    else:
        story.append(Paragraph("• No products available", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Revenue Sources
    story.append(Paragraph("Revenue Sources", styles['Heading3']))
    revenue_sources = analysis2.get("revenue_sources", [])
    if revenue_sources:
        for source in revenue_sources:
            story.append(Paragraph(f"• {source}", normal_style))
    else:
        story.append(Paragraph("• No revenue sources available", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Competitors
    story.append(Paragraph("Competitors", styles['Heading3']))
    competitors = competitor2.get("competitors", [])
    if competitors:
        for comp in competitors:
            story.append(Paragraph(f"• {comp}", normal_style))
    else:
        story.append(Paragraph("• No competitors identified", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Investment Summary
    story.append(Paragraph("Investment Summary", styles['Heading3']))
    investment_summary = analysis2.get("investment_summary", "No summary available")
    story.append(Paragraph(investment_summary, normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Page break before comparison verdict
    story.append(PageBreak())
    
    # Comparison Verdict
    story.append(Paragraph("🏆 Comparison Verdict", heading_style))
    story.append(Paragraph(comparison, normal_style))
    
    # Build PDF
    doc.build(story)
    
    # Reset buffer position to beginning
    pdf_buffer.seek(0)
    
    return pdf_buffer

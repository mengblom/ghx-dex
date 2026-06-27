#!/usr/bin/env python3
"""
Create Exchange Resiliency Report PDF with professional formatting, charts, and icons.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import (
    Drawing, Rect, String, Circle, Line, Polygon, Path
)
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics import renderPDF
import sys
from datetime import datetime
import math

# Color scheme - professional and accessible
COLOR_COMPLETED = colors.HexColor('#28A745')  # Green
COLOR_IN_PROGRESS = colors.HexColor('#007BFF')  # Blue
COLOR_UNKNOWN = colors.HexColor('#FD7E14')  # Orange
COLOR_HEADER = colors.HexColor('#2C3E50')  # Dark blue-gray
COLOR_ACCENT = colors.HexColor('#3498DB')  # Light blue
COLOR_LIGHT_BG = colors.HexColor('#F8F9FA')  # Very light gray

def create_header_footer(canvas_obj, doc):
    """Add header and footer to each page."""
    canvas_obj.saveState()
    width, height = letter

    # Header
    canvas_obj.setFillColor(COLOR_HEADER)
    canvas_obj.setFont('Helvetica-Bold', 8)
    canvas_obj.drawString(0.75*inch, height - 0.5*inch,
                         "Exchange Resiliency Report")
    canvas_obj.drawString(width - 2*inch, height - 0.5*inch,
                         "June 26, 2026")

    # Footer with page number
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.setFillColor(colors.gray)
    page_num = canvas_obj.getPageNumber()
    canvas_obj.drawCentredString(width/2, 0.5*inch,
                                 f"Page {page_num}")

    canvas_obj.restoreState()

def create_status_icon(status, size=12):
    """Create a graphical status icon."""
    drawing = Drawing(size, size)
    center = size / 2
    radius = size / 2.5

    if status == "completed":
        # Green circle with white checkmark
        circle = Circle(center, center, radius, fillColor=COLOR_COMPLETED, strokeColor=COLOR_COMPLETED, strokeWidth=0.5)
        drawing.add(circle)

        # Checkmark path
        check_path = Path(fillColor=colors.white, strokeColor=colors.white, strokeWidth=1.5)
        check_path.moveTo(center - radius*0.4, center)
        check_path.lineTo(center - radius*0.1, center - radius*0.3)
        check_path.lineTo(center + radius*0.5, center + radius*0.4)
        drawing.add(check_path)

    elif status == "in_progress":
        # Blue circle with rotating arrows
        circle = Circle(center, center, radius, fillColor=COLOR_IN_PROGRESS, strokeColor=COLOR_IN_PROGRESS, strokeWidth=0.5)
        drawing.add(circle)

        # Circular arrow (simplified as curved segments)
        arrow_color = colors.white
        arrow_width = 1.2

        # Draw arrow arc
        for i in range(3):
            angle_start = i * 120 + 30
            angle_end = angle_start + 80

            x1 = center + radius * 0.5 * math.cos(math.radians(angle_start))
            y1 = center + radius * 0.5 * math.sin(math.radians(angle_start))
            x2 = center + radius * 0.5 * math.cos(math.radians(angle_end))
            y2 = center + radius * 0.5 * math.sin(math.radians(angle_end))

            line = Line(x1, y1, x2, y2, strokeColor=arrow_color, strokeWidth=arrow_width)
            drawing.add(line)

    elif status == "unknown":
        # Orange circle with white question mark
        circle = Circle(center, center, radius, fillColor=COLOR_UNKNOWN, strokeColor=COLOR_UNKNOWN, strokeWidth=0.5)
        drawing.add(circle)

        # Question mark (simplified)
        q_string = String(center, center - radius*0.4, '?',
                         fontSize=size*0.7, fillColor=colors.white,
                         textAnchor='middle', fontName='Helvetica-Bold')
        drawing.add(q_string)

    else:  # not_started
        # Gray circle with pause bars
        circle = Circle(center, center, radius, fillColor=colors.lightgrey, strokeColor=colors.grey, strokeWidth=0.5)
        drawing.add(circle)

        # Pause bars
        bar_width = radius * 0.25
        bar_height = radius * 1.0
        bar1 = Rect(center - radius*0.35, center - bar_height/2, bar_width, bar_height,
                   fillColor=colors.white, strokeColor=None)
        bar2 = Rect(center + radius*0.1, center - bar_height/2, bar_width, bar_height,
                   fillColor=colors.white, strokeColor=None)
        drawing.add(bar1)
        drawing.add(bar2)

    return drawing

def create_status_icon_legend():
    """Create a legend showing all status icons with labels."""
    from reportlab.platypus import Table, TableStyle

    legend_data = [
        [create_status_icon("completed", 14), "Completed - Work is done and deployed"],
        [create_status_icon("in_progress", 14), "In Progress - Work is actively underway"],
        [create_status_icon("unknown", 14), "Unknown - Status unclear from documentation"],
        [create_status_icon("not_started", 14), "Not Started - Work has not yet begun"]
    ]

    legend_table = Table(legend_data, colWidths=[0.3*inch, 5*inch])
    legend_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))

    return legend_table

def create_completion_chart(data):
    """Create horizontal bar chart for completion rates."""
    drawing = Drawing(400, 200)
    chart = HorizontalBarChart()
    chart.x = 50
    chart.y = 20
    chart.height = 150
    chart.width = 300

    # Data format: [values]
    chart.data = [data]

    # Categories
    chart.categoryAxis.categoryNames = [
        'Observability\n& Operations',
        'Process, Governance\n& Security',
        'Database &\nData Layer',
        'Infrastructure &\nResilience',
        'Architectural\nDecoupling'
    ]

    # Styling
    chart.bars[0].fillColor = COLOR_ACCENT
    chart.categoryAxis.labels.fontSize = 8
    chart.categoryAxis.labels.dx = -5
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 100
    chart.valueAxis.valueStep = 25
    chart.valueAxis.labels.fontSize = 8

    # Add percentage labels on bars
    chart.barLabels.fontSize = 9
    chart.barLabels.fillColor = colors.white
    chart.barLabelFormat = '%d%%'
    chart.barLabels.nudge = 10

    drawing.add(chart)
    return drawing

def create_summary_table():
    """Create the status summary table with graphical icons."""
    # Create header row with icons
    completed_icon = create_status_icon("completed", 12)
    progress_icon = create_status_icon("in_progress", 12)
    unknown_icon = create_status_icon("unknown", 12)

    # Create a nested table for icon+text headers
    def icon_header(icon, text):
        inner_data = [[icon, text]]
        inner_table = Table(inner_data, colWidths=[16, 70])
        inner_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1, 0), (1, 0), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]))
        return inner_table

    data = [
        ['Group', icon_header(completed_icon, 'Completed'),
         icon_header(progress_icon, 'In Progress'),
         icon_header(unknown_icon, 'Unknown'), 'Total'],
        ['Database & Data Layer', '5', '4', '3', '12'],
        ['Architectural Decoupling', '3', '4', '6', '13'],
        ['Infrastructure & Resilience', '4', '5', '2', '11'],
        ['Observability & Operations', '6', '0', '2', '8'],
        ['Process, Governance & Security', '5', '3', '2', '10'],
        ['TOTAL', '23', '16', '15', '54'],
    ]

    table = Table(data, colWidths=[2.5*inch, 1*inch, 1.2*inch, 1*inch, 0.8*inch])

    style = TableStyle([
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_HEADER),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),

        # Data rows
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, COLOR_LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),

        # Totals row
        ('BACKGROUND', (0, -1), (-1, -1), COLOR_LIGHT_BG),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, -1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 12),

        # Color-coded columns
        ('TEXTCOLOR', (1, 1), (1, -1), COLOR_COMPLETED),
        ('TEXTCOLOR', (2, 1), (2, -1), COLOR_IN_PROGRESS),
        ('TEXTCOLOR', (3, 1), (3, -1), COLOR_UNKNOWN),
    ])

    table.setStyle(style)
    return table

def create_metrics_highlight(metric_text, value_text):
    """Create a highlighted metric box."""
    data = [[metric_text], [value_text]]
    table = Table(data, colWidths=[2.5*inch])

    style = TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), COLOR_ACCENT),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 9),
        ('FONTSIZE', (0, 1), (0, 1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 2, COLOR_ACCENT),
    ])

    table.setStyle(style)
    return table

def create_pdf_report(output_path):
    """Create the complete PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch
    )

    # Container for PDF elements
    story = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=COLOR_HEADER,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=COLOR_HEADER,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=COLOR_HEADER,
        spaceBefore=20,
        spaceAfter=12,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=COLOR_ACCENT,
        borderPadding=5,
        leftIndent=0
    )

    subsection_style = ParagraphStyle(
        'Subsection',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=COLOR_HEADER,
        spaceBefore=12,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=6
    )

    # ====================
    # TITLE PAGE
    # ====================
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Exchange Resiliency Report", title_style))
    story.append(Paragraph("Promised vs. Completed Work Analysis", subtitle_style))
    story.append(Spacer(1, 0.3*inch))

    # Report metadata
    metadata = [
        ['Report Date:', 'June 26, 2026'],
        ['Prepared For:', 'CJ Singh'],
        ['Prepared By:', 'Marten Engblom'],
        ['Purpose:', 'Transformation narrative support for resiliency update meeting'],
    ]

    meta_table = Table(metadata, colWidths=[1.5*inch, 4*inch])
    meta_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))

    story.append(meta_table)
    story.append(Spacer(1, 0.5*inch))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_ACCENT))
    story.append(PageBreak())

    # ====================
    # EXECUTIVE SUMMARY
    # ====================
    story.append(Paragraph("Executive Summary", section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=12))

    exec_summary = """This report provides a comprehensive view of Exchange resiliency work completed
    over the last 18 months, organized into five thematic dimensions rather than granular item-by-item
    mapping. This approach demonstrates comprehensive execution across all aspects of system resilience."""
    story.append(Paragraph(exec_summary, body_style))
    story.append(Spacer(1, 0.2*inch))

    # Key findings in table format
    story.append(Paragraph("<b>Key Findings:</b>", subsection_style))

    findings_data = [
        ['Metric', 'Value'],
        ['Completed work deployed to production', '43%'],
        ['Actively in progress', '30%'],
        ['Status unclear from documentation', '27%'],
        ['Distinct initiatives tracked', '54'],
        ['Resiliency dimensions', '5'],
    ]

    findings_table = Table(findings_data, colWidths=[3.5*inch, 2*inch])
    findings_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_HEADER),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))

    story.append(findings_table)
    story.append(Spacer(1, 0.2*inch))

    # Performance highlights
    story.append(Paragraph("<b>Strongest Performance:</b> Observability & Operations (75% complete)", body_style))
    story.append(Paragraph("<b>Most Active Work:</b> Database & Data Layer, Infrastructure & Resilience (ongoing migrations)", body_style))
    story.append(Spacer(1, 0.2*inch))

    # Status legend with graphical icons
    story.append(Paragraph("<b>Status Legend:</b>", subsection_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(create_status_icon_legend())

    story.append(PageBreak())

    # ====================
    # STATUS SUMMARY
    # ====================
    story.append(Paragraph("Status Summary", section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=12))

    story.append(Paragraph("Overall Progress Across All Groups", subsection_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(create_summary_table())
    story.append(Spacer(1, 0.3*inch))

    # Completion rate chart
    story.append(Paragraph("Completion Rate by Dimension", subsection_style))
    story.append(Spacer(1, 0.1*inch))

    # Chart data: percentages for each dimension
    completion_data = [75, 50, 42, 36, 23]  # Observability, Process, Database, Infrastructure, Architectural
    story.append(create_completion_chart(completion_data))
    story.append(Spacer(1, 0.3*inch))

    # Key insights
    story.append(Paragraph("Key Insights", subsection_style))

    insights = [
        "<b>Strengths:</b> Observability infrastructure mature and comprehensive; Process improvements embedded across organization; Database optimization delivering measurable impact (80% read reduction, 30min→5min loads)",
        "<b>Active Investment Areas:</b> Architectural decoupling work (4 initiatives in flight, 6 awaiting confirmation); Infrastructure resilience (5 major migrations ongoing: Atlas, ES, Aurora, DR, Tracking Phase 3); Database modernization (managed services migrations)",
        "<b>Documentation Gaps:</b> 15 items (27%) need status clarification; Primarily in architectural decoupling and granular database work; Likely candidates for director input sessions"
    ]

    for insight in insights:
        story.append(Paragraph(f"• {insight}", bullet_style))

    story.append(PageBreak())

    # ====================
    # KEY METRICS & IMPACT
    # ====================
    story.append(Paragraph("Key Metrics & Impact Summary", section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=12))

    story.append(Paragraph("Quantifiable Improvements Delivered", subsection_style))
    story.append(Spacer(1, 0.2*inch))

    # Create metrics highlights in a grid
    metrics_row1 = Table([[
        create_metrics_highlight("Database Read Reduction", "80%"),
        create_metrics_highlight("Bulk Load Time", "30min → 5min"),
        create_metrics_highlight("Validation Time", "Days → 2min")
    ]], colWidths=[2.5*inch, 2.5*inch, 2.5*inch])

    story.append(metrics_row1)
    story.append(Spacer(1, 0.3*inch))

    # Architectural progress
    story.append(Paragraph("Architectural Progress", subsection_style))
    arch_items = [
        "52 tables migrated from TPM to dedicated SSO DB",
        "4 tables migrated to dedicated BR DB (~40% of TPM footprint)",
        "4 UIs fully decoupled from monolithic ALL repo"
    ]
    for item in arch_items:
        story.append(Paragraph(f"✓ {item}", bullet_style))

    story.append(Spacer(1, 0.2*inch))

    # Reliability & Availability
    story.append(Paragraph("Reliability & Availability", subsection_style))
    rel_items = [
        "Multi-region data synchronization enabled (Aurora migration)",
        "Performance environment preventing production incidents",
        "EventBus resilience reducing doc processing incident impact"
    ]
    for item in rel_items:
        story.append(Paragraph(f"✓ {item}", bullet_style))

    story.append(Spacer(1, 0.2*inch))

    # Security & Compliance
    story.append(Paragraph("Security & Compliance", subsection_style))
    sec_items = [
        "Mongo 8.X support enabled",
        "EOL libraries remediated",
        "Vulnerability remediation across stack",
        "SAML protocol added to GHX SSO"
    ]
    for item in sec_items:
        story.append(Paragraph(f"✓ {item}", bullet_style))

    story.append(PageBreak())

    # ====================
    # DETAILED BREAKDOWN BY DIMENSION
    # ====================
    story.append(Paragraph("Detailed Work by Dimension", section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=12))

    dimensions = [
        {
            'name': '1. Database & Data Layer',
            'completed': 5,
            'in_progress': 4,
            'unknown': 3,
            'total': 12,
            'highlights': [
                'IBR User Data Separation (Phase 2 & 3) - Migrated 4 tables (~40% of TPM footprint)',
                'BR User Data Cache Replacement - 80% reduction in TPM database reads',
                'TPM Migration from MySQL to Aurora - Multi-region data synchronization',
                'Organization Search Data in Elasticsearch - 30min → 5min bulk load time'
            ]
        },
        {
            'name': '2. Architectural Decoupling',
            'completed': 3,
            'in_progress': 4,
            'unknown': 6,
            'total': 13,
            'highlights': [
                'SSO Database Separation - Migrated 52 tables from TPM DB to dedicated SSO DB',
                'SSO moved out of AuditDB - Independent authentication service',
                '4 UIs fully decoupled from monolithic ALL repo (Orders, Notifications, Transactions, Invoicing)',
                'RC 2.0 Monolith Decoupling - Ongoing migration to GitHub with independent pipelines'
            ]
        },
        {
            'name': '3. Infrastructure & Resilience',
            'completed': 4,
            'in_progress': 5,
            'unknown': 2,
            'total': 11,
            'highlights': [
                'Performance Environment Setup - Widely used for database upgrades and release testing',
                'EventBus Resiliency - Reduced doc processing impact during incidents',
                'Industry Continuity Solution (ICS) - Contractor-built solution deployed',
                'Tracking Resiliency Phase 1 & 2 - Bug reduction and race condition fixes'
            ]
        },
        {
            'name': '4. Observability & Operations',
            'completed': 6,
            'in_progress': 0,
            'unknown': 2,
            'total': 8,
            'highlights': [
                'Heartbeat: CoreX Business Intelligence - Comprehensive metrics dashboard',
                'Canary Program (Document Prediction) - Kinesis stream for predictive monitoring',
                'Org API GitHub Validation - Multiple person-days → 2 minutes validation time',
                'Feature Flagging Capability - Enabled safer, incremental rollouts'
            ]
        },
        {
            'name': '5. Process, Governance & Security',
            'completed': 5,
            'in_progress': 3,
            'unknown': 2,
            'total': 10,
            'highlights': [
                'Release Rigor & Change Management - Multi-person go-live audit implemented',
                'Mongo 8.X Support - Upgraded drivers, EOL libs, vulnerability remediation',
                'SAML Implementation - Added SAML protocol to GHX SSO',
                'Customer Empathy Training - Team-wide rollout completed'
            ]
        }
    ]

    for dim in dimensions:
        # Dimension header with colored bar
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph(dim['name'], subsection_style))

        # Status summary for this dimension
        status_text = f"""<b>Status:</b> {dim['completed']} [✓] Completed |
        {dim['in_progress']} [~] In Progress | {dim['unknown']} [?] Unknown |
        Total: {dim['total']} initiatives"""
        story.append(Paragraph(status_text, body_style))
        story.append(Spacer(1, 0.1*inch))

        # Key highlights
        story.append(Paragraph("<b>Key Highlights:</b>", body_style))
        for highlight in dim['highlights']:
            story.append(Paragraph(f"• {highlight}", bullet_style))

        story.append(Spacer(1, 0.15*inch))
        story.append(HRFlowable(width="80%", thickness=0.5, color=colors.lightgrey))

    story.append(PageBreak())

    # ====================
    # ANALYSIS & INSIGHTS
    # ====================
    story.append(Paragraph("Analysis & Insights", section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=12))

    story.append(Paragraph("What This Data Tells Us", subsection_style))

    analysis_points = [
        {
            'title': '1. Comprehensive Execution',
            'text': "We've made progress across all five resiliency dimensions, not cherry-picking easy wins. The work spans infrastructure, architecture, operations, and culture."
        },
        {
            'title': '2. Momentum Sustained',
            'text': "30% of work actively in progress demonstrates sustained investment. Key migrations (Atlas, ES, Aurora) are all moving forward simultaneously."
        },
        {
            'title': '3. Operational Excellence Achieved',
            'text': "75% completion in Observability & Operations shows mature monitoring, alerting, and incident management capabilities now in place."
        },
        {
            'title': '4. Architectural Transformation Underway',
            'text': "While only 23% complete in Architectural Decoupling, 4 major initiatives are in progress. This is expected given the complexity and scope of monolith deconstruction."
        },
        {
            'title': '5. Documentation Discipline Needed',
            'text': "27% of items have unclear status. This likely reflects work completed but not formally documented rather than work not done. Director input sessions needed."
        }
    ]

    for point in analysis_points:
        story.append(Paragraph(f"<b>{point['title']}</b>", body_style))
        story.append(Paragraph(point['text'], body_style))
        story.append(Spacer(1, 0.1*inch))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Strategic Implications", subsection_style))

    strategic_text = """
    <b>This Week's Incident Validates Strategy:</b> The June 22-24 production incident demonstrated
    exactly why architectural decoupling matters. Monolithic coupling caused 6 simultaneous issues,
    deployment pipeline fragility prevented rapid fixes, and every root cause is addressed by
    autonomous teams + continued decoupling.<br/><br/>

    <b>Conway's Law Opportunity:</b> Current organizational structure (4 directors, 12 managers,
    small teams) is in place. Now aligning team boundaries to architectural boundaries will
    accelerate decoupling organically.<br/><br/>

    <b>Infrastructure Foundation Ready:</b> Performance environment, monitoring, incident management
    processes are mature. This foundation supports the next phase of architectural transformation.
    """
    story.append(Paragraph(strategic_text, body_style))

    story.append(PageBreak())

    # ====================
    # NEXT STEPS
    # ====================
    story.append(Paragraph("Next Steps & Recommendations", section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=12))

    next_steps = [
        {
            'timeframe': 'Immediate Actions (This Week)',
            'items': [
                '[✓] Extract completed items from Exchange Resiliency Completed.docx - DONE',
                '[✓] Populate "What We Completed" sections for each group - DONE',
                '[✓] Add all Jira tickets and metrics from source document - DONE',
                '[✓] Add status icons to "What We Promised" items - DONE'
            ]
        },
        {
            'timeframe': 'Short-Term (Next 2 Weeks)',
            'items': [
                'Review with directors (Daniel, Aaron, Arshad, Ramesh) to confirm status of 15 "Unknown" items',
                'Validate brainstormed list items (Tracking/Notifications decoupling, IO Guarantee, etc.)',
                'Gather missing metrics (Customer empathy training dates, audit results)',
                'Fill in remaining gaps from Aaron: Red Mythos Exchange status and metrics'
            ]
        },
        {
            'timeframe': 'Medium-Term (Q3 2026)',
            'items': [
                'Establish baseline metrics for transformation success criteria (incident frequency, MTTR, deployment frequency, change failure rate)',
                'Document ongoing migrations with milestones (Atlas, Elasticsearch, Aurora, DR drill schedule)',
                'Define team autonomy scores and cross-team dependency counts'
            ]
        },
        {
            'timeframe': 'Long-Term (Q4 2026+)',
            'items': [
                'Continuous documentation discipline - all completed work captured',
                'Monthly status updates to this report',
                'Quarterly review with leadership',
                'Tell the transformation story more broadly (internal comms, customer messaging)'
            ]
        }
    ]

    for step in next_steps:
        story.append(Paragraph(f"<b>{step['timeframe']}</b>", subsection_style))
        for item in step['items']:
            story.append(Paragraph(f"• {item}", bullet_style))
        story.append(Spacer(1, 0.15*inch))

    # ====================
    # FOOTER
    # ====================
    story.append(Spacer(1, 0.5*inch))
    story.append(HRFlowable(width="100%", thickness=2, color=COLOR_ACCENT))
    story.append(Spacer(1, 0.1*inch))

    footer_text = """
    <b>Report Version:</b> 1.0<br/>
    <b>Created:</b> June 25, 2026<br/>
    <b>Last Updated:</b> June 26, 2026<br/>
    <b>Next Review:</b> July 10, 2026 (post-CJ meeting)
    """
    story.append(Paragraph(footer_text, body_style))

    # Build PDF
    doc.build(story, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    print(f"[✓] PDF report created successfully: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/mengblom/Documents/ghx-dex/04-Projects/21-Exchange_Modernization_Report_May_2026/2026-06-26 Exchange Resiliency Update/Exchange Resiliency Report - Promised vs Completed.pdf"

    try:
        create_pdf_report(output_file)
        print(f"\n📄 Report saved to:\n{output_file}")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

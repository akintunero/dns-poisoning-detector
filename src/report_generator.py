from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os
import time


def generate_pdf_report(suspicious_responses):
    if not os.path.exists('reports'):
        os.makedirs('reports')

    filename = f"reports/dns_poisoning_report_{int(time.time())}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "DNS Poisoning Detection Report")

    # Summary
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Total suspicious responses detected: {len(suspicious_responses)}")

    # Table header
    data = [["Source IP", "Queried Domain", "Suspicious IP"]]
    data.extend(suspicious_responses)

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    table.wrapOn(c, width - 100, height)
    table.drawOn(c, 50, height - 150 - (len(suspicious_responses) * 20))

    c.save()
    print(f"PDF report generated: {filename}")

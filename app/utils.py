from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Catalogue

def generate_catalogue_pdf(catalogue_items, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)

    y = height - 40
    for item in catalogue_items:
        c.drawString(40, y - 15, f"Name: {item.name}")
        c.drawString(40, y - 30, f"Description: {item.description}")
        c.drawString(40, y - 45, f"Cost Price: {item.cost_price}")
        c.drawString(40, y - 60, f"In Stock: {'Yes'}")
        c.drawString(40, y - 75, "-"*int(width))
        y -= 135

        if y < 40:
            c.showPage()
            y = height - 40
            c.setFont("Helvetica", 12)

    c.save()

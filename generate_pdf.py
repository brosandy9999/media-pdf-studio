from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_sample_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 700, "Interactive PDF Sample")
    
    # Instructions
    c.setFont("Helvetica", 12)
    c.drawString(100, 650, "Click the link below to play the video.")
    
    # Link Text
    c.setFont("Helvetica", 14)
    c.setFillColorRGB(0, 0, 1) # Blue
    c.drawString(100, 600, "Play Sample Video (video.mp4)")
    
    # Add link annotation
    c.linkURL("video.mp4", (100, 595, 300, 615), relative=1)
    
    c.save()

if __name__ == "__main__":
    create_sample_pdf("sample.pdf")

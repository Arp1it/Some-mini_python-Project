from fpdf import FPDF

def create_pdf():
    pdf = FPDF()

    # add a blank page to the pdf
    pdf.add_page()

    # change the text color
    pdf.set_text_color(255, 0, 0)

    # set the font of the text
    pdf.set_font('Arial', size=25)

    # add some text
    pdf.text(10, 50, "Hey My first PDF")

    # add image
    pdf.image("0.jpg", 10, 10, 15, 15)

    # save the pdf document
    pdf.output("first.pdf")

def creat_img_pdf():
    pdf_img = FPDF()

    pdf_img.add_page()

    pdf_img.set_auto_page_break(0)

    image = "0.jpg"
    pdf_img.image(image, w=200, h=260)

    pdf_img.output("images.pdf")

if __name__=="__main__":
    # create_pdf()
    creat_img_pdf()
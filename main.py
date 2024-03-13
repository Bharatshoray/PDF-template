from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("003 topics.csv")

for index, row in df.iterrows():
    pdf.add_page()                                              # master page

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)                  # colours ranging from blue to red 0-254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)                    # pdf.line(x1, y1, x2, y2)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):                   # this is a nested for loop and subtracting 1 will print correct
        pdf.add_page()                                  # no. of pages as the header add page will add one more page

        pdf.ln(277)                                     # 277 = 265(ln of first page footer) + 12(h)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
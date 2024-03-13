from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("003 topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)               # colours ranging from blue to red 0-254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)                 # pdf.line(x1, y1, x2, y2)

    for i in range(row["Pages"] - 1):                        # subtracting 1 will give correct no. of pages as the
        pdf.add_page()                                       # header add page will add one more page


pdf.output("output.pdf")
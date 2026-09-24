class Report:
    def generate(self):
        print("Generating report")

class PDF(Report):
    def generate(self):
        print("Generating PDF report")

class Excel(Report):
    def generate(self):
        print("Generating Excel report")

class HTML(Report):
    def generate(self):
        print("Generating HTML report")

def generate_report(report):
    report.generate()

pdf = PDF()
excel = Excel()
html = HTML()
generate_report(pdf)
generate_report(excel)
generate_report(html)
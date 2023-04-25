# docx.py
class DocxFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        print(f"Reading from DOCX file: {self.filename}")

    def write(self, contents):
        print(f"Writing to DOCX file: {self.filename}")
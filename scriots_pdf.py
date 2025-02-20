import os.path

from pypdf import PdfReader

reader = PdfReader("tmp/Python Testing with Pytest (Brian Okken).pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())

assert "This book is licensed to" in reader.pages[1]
print(os.path.getsize("tmp/Python Testing with Pytest (Brian Okken).pdf"))
assert os.path.getsize("tmp/Python Testing with Pytest (Brian Okken).pdf") == 3035139
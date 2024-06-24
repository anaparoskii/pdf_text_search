import fitz


def parse_pdf():
    pdf_doc = fitz.open('data/Data Structures and Algorithms in Python.pdf')

    hashmap = {}
    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        page_text = page.get_text()
        hashmap[page_num + 1] = page_text

    return hashmap

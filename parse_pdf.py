import fitz


def parse_pdf():
    pdf_doc = fitz.open('data/Data Structures and Algorithms in Python.pdf')

    hashmap = {}
    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        page_text = page.get_text()
        hashmap[page_num + 1] = page_text

    return hashmap


"""
if __name__ == "__main__":
    results = parse_pdf()
    for key in results:
        page = results[key]
        print('Index: %s' % key)
        print('Content:\n\n' + page)
        print('\n\n\n')

    n = 3
    print(f"Text on page {n}:\n{results[n]}")
"""

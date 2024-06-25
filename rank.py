def rank(pages, graph):
    ranked_pages = {}
    for page in pages:
        ranked_pages[page] = ranked_pages.get(page, 0) + 1
    return reference_rank(graph, ranked_pages, 1)


def reference_rank(graph, medium_rank, max_value):
    references = graph.search_references(list(medium_rank.keys()))
    for page_number, reference in references.items():
        if reference in list(medium_rank.keys()):
            medium_rank[reference] *= 1.5
    ranked_pages = sorted(medium_rank.items(), key=lambda item: item[1], reverse=True)
    sorted_pages = []
    for page, frequency in ranked_pages:
        frequency *= max_value
        for page_number, page_references in references.items():
            if page_references in list(medium_rank.keys()):
                medium_rank[page_references] /= 1.5
        sorted_pages.append((page, frequency))
    return sorted_pages

"""

def search_words(self, words):
    if not words:
        return []
    if len(words) >= 3:
        condition = words[1]
        if condition in ["AND", "OR", "NOT"]:
            words = words[0::2]
    else:
        condition = None

    if condition == "AND":
        # Find pages where all words appear
        all_pages = []
        for word in words:
            if self.has_node(word.lower()):
                pages = self.get_pages(word.lower())
                all_pages.append(pages)
        if not all_pages:
            return []
        # Intersect sets to find common pages
        common_pages = set(all_pages[0])
        for pages in all_pages[1:]:
            common_pages.intersection_update(pages)
        return list(common_pages)

    elif condition == "OR":
        # Find pages where at least one word appears
        all_pages = {}
        for word in words:
            if self.has_node(word.lower()):
                pages = self.get_pages(word.lower())
                for page in pages:
                    if page not in all_pages:
                        all_pages[page] = 0
                    all_pages[page] += 1
        # Rank pages based on frequency (or another relevance metric)
        ranked_pages = sorted(all_pages.items(), key=lambda item: item[1], reverse=True)
        return [page for page, frequency in ranked_pages]

    elif condition == "NOT":
        # Find pages where only the first word appears
        all_pages = []
        for word in words:
            if self.has_node(word.lower()):
                pages = self.get_pages(word.lower())
                all_pages.append(pages)
        if not all_pages:
            return []

        wanted_pages = []
        for pages in all_pages[0]:
            for page in pages:
                for p in all_pages[1:]:
                    if page not in p:
                        wanted_pages.append(page)
        return wanted_pages

    else:
        # Default to searching for individual words
        result = []
        for word in words:
            result.append(self.search_word(word))
        return result



Condition 1 (All Words Appear):

For each word, check if it exists in the data structure and get its associated pages.
Use set intersection to find common pages where all words appear.
Return the list of common pages.


Condition 2 (At Least One Word Appears):

For each word, check if it exists in the data structure and get its associated pages.
Use a dictionary to count the occurrence of pages.
Rank pages based on the frequency of words appearing on them (or another relevance metric).
Return the ranked list of pages.
Ranking Explanation:

To rank pages, you could consider:
Frequency: Count how many of the search words appear on each page.
Relevance: Weight certain words more heavily based on their importance.
Combination of factors: Combine frequency and relevance to score pages.


Condition 3 (Only the First Word Appears):

Check if the first word exists in the data structure and get its associated pages.
Return the list of pages associated with the first word.
Final Thoughts
This approach ensures that your search_words function is versatile and can handle different 
search conditions efficiently. The ranking logic for condition 2 is flexible and can be tailored 
to suit the specific needs of your application, such as by incorporating additional 
relevance metrics or weighting schemes.
"""


"""
def search_words(trie, words):
    if len(words) >= 3:
        condition = words[1]
        if condition in ["AND", "OR", "NOT"]:
            words = words[0::2]
    else:
        condition = None

    if condition == "AND":
        return and_search(trie, words)
    elif condition == "OR":
        return or_search(trie, words)
    elif condition == "NOT":
        return not_search(trie, words)
    else:
        return default_search(trie, words)

def and_search(trie, words):
    common_pages = None
    for word in words:
        pages = trie.search(word.lower())
        if pages is None:
            return []  # If any word isn't found, return empty list
        if common_pages is None:
            common_pages = set(pages)
        else:
            common_pages.intersection_update(pages)
    return list(common_pages)

def or_search(trie, words):
    all_pages = []
    for word in words:
        pages = trie.search(word.lower())
        if pages:
            all_pages.extend(pages)
    return rank(all_pages)

def not_search(trie, words):
    all_pages = []
    for word in words[1:]:
        pages = trie.search(word.lower())
        if pages:
            all_pages.extend(pages)
    not_pages = [page for page in trie.root.pages if page not in all_pages]
    return not_pages

def default_search(trie, words):
    all_pages = []
    for word in words:
        pages = trie.search(word.lower())
        if pages:
            all_pages.extend(pages)
    return rank(all_pages)

def rank(pages):
    ranked_pages = {}
    for page in pages:
        if isinstance(page, int):
            ranked_pages[page] = ranked_pages.get(page, 0) + 1
        else:
            for p in page:
                ranked_pages[p] = ranked_pages.get(p, 0) + 1
    sorted_pages = sorted(ranked_pages.items(), key=lambda x: x[1], reverse=True)
    return sorted_pages

def get_paragraph(page, words, code):
    if code == 1:
        paragraph = page.split('\n')
        paragraph_value = ''
        search_range = len(paragraph) // 2
        for word in words:
            for i in range(search_range, len(paragraph)):
                if word.lower() in paragraph[i].lower():
                    if paragraph_value == '':
                        paragraph_value = paragraph[i]
                    elif paragraph_value != paragraph[i]:
                        paragraph_value += '\n' + paragraph[i]
                        break
        for word in words:
            if paragraph_value != '':
                paragraph_value = paragraph_value.lower().replace(word, f"{Color.PURPLE}{word}{Color.RESET}")
        return paragraph_value
    else:
        paragraph = page.split('\n')
        paragraph_value = ''
        search_range = len(paragraph) // 2
        for i in range(search_range, len(paragraph)):
            if words in paragraph[i]:
                if paragraph_value == '':
                    paragraph_value = paragraph[i]
                elif paragraph_value != paragraph[i]:
                    paragraph_value += '\n' + paragraph[i]
                    break
        if paragraph_value != '':
            paragraph_value = paragraph_value.replace(words, f"{Color.PURPLE}{words}{Color.RESET}")
        return paragraph_value
        
        
    
import re

def extract_references(text):
    references = []
    pattern = r'page\s+(\d+)'
    matches = re.findall(pattern, text)
    for match in matches:
        references.append(int(match) + 22)  # Convert to integer if page numbers are represented as strings
    return references
    
def build_graph(hashmap):
   for page_number, text in hashmap.items():
        references = extract_references(text)
        if references:
            for ref in references:
                graph.add_edge(page_number, ref)
        else:
            graph.add_edge(page_number, None)
    
    return graph
"""

def search_words(self, words, condition):
    if not words:
        return []

    if condition == 1:
        # Find pages where all words appear
        all_pages = [self.get_pages(word.lower()) for word in words if self.has_node(word.lower())]
        if not all_pages:
            return []
        # Intersect sets to find common pages
        common_pages = set(all_pages[0])
        for pages in all_pages[1:]:
            common_pages.intersection_update(pages)
        return list(common_pages)

    elif condition == 2:
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

    elif condition == 3:
        # Find pages where only the first word appears
        first_word = words[0].lower()
        if self.has_node(first_word):
            return self.get_pages(first_word)
        return []

    else:
        raise ValueError("Invalid condition value")


"""
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

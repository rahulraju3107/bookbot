def get_number_of_words(contents):
    return len(contents.split())

# Counts number of characters in text
def get_character_count(contents):
    counts = {}
    for ch in contents:
        key = ch.lower()
        counts[key] = counts.get(key, 0) + 1
    return counts

# Sort by frequency
def sorted_list(counts):
    rows = []
    for char, freq in counts.items():
        if not char.isalpha():
            continue
        rows.append({"char": char, "num": freq})
    
    # Helper function for sorting
    def sort_on(item):
        return item["num"]
    
    rows.sort(reverse=True, key=sort_on)

    return rows
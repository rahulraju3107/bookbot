def get_number_of_words(contents):
    return len(contents.split())

def get_character_count(contents):
    counts = {}
    for ch in contents:
        key = ch.lower()
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts
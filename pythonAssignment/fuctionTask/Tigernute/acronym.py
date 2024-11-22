def get_acronym(word):
    acronym = ""
    words = word.split()
    for word in words:
        acronym += word[0].upper()
    return acronym


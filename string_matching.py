def boyer_moore(text, pattern):
    def last_occurrence_function(pattern):
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    def boyer_moore_search(text, pattern):
        last = last_occurrence_function(pattern)
        m = len(pattern)
        n = len(text)
        i = m - 1  # Start with the end of the pattern aligned at the start of the text

        while i < n:
            j = m - 1  # Start comparing from the end of the pattern
            while j >= 0 and pattern[j] == text[i]:
                j -= 1
                i -= 1
            if j < 0:  # Found a match
                return i + 1
            else:
                lo = last.get(text[i], -1)  # Get the last occurrence of text[i] in the pattern
                i += m - min(j, lo + 1)

        return -1  # No match found

    return boyer_moore_search(text, pattern)
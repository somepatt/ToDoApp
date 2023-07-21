from fuzzywuzzy import fuzz

def tolerant_search(query, items, threshold=60):
    result = []
    for item in items:
        sim = fuzz.token_set_ratio(query, item)
        print(sim)
        if sim >= threshold:
            result.append((item, sim))
    return result
    
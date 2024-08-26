def best_score(a_dictionary):
    best_score = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                best_score_key = key
            else:
                continue
        if not best_score:
            return None
        else: 
            return best_score_key
    else:
        return None
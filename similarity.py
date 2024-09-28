from Levenshtein import distance
from json_handler import get_keys_from_file

def find_most_similar(target, word_list):
    if not word_list:
        return None
    
    most_similar = min(word_list, key=lambda word: distance(target, word))
    similarity = distance(target, most_similar)
    
    return most_similar, similarity

if __name__ == "__main__":
    word_list = get_keys_from_file('support_ro.json', depth=2)
    word_list.remove("script_support")

    target_word = 'CABINET{"Class": "ÎNCHEIERE"}'

    closest_match, similarity_score = find_most_similar(target_word, word_list)
    print(f"The most similar word to '{target_word}' is '{closest_match}' with a distance of {similarity_score}")
def sort_words_in_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)  # Sort words in a case-insensitive manner
    sorted_sentence = ' '.join(words) # Join the sorted words back into a sentence
    return sorted_sentence


sentence = "The quick brown fox jumps over the lazy dog"
sorted_result = sort_words_in_sentence(sentence)
print("Original sentence:", sentence)
print("Sorted sentence:", sorted_result)
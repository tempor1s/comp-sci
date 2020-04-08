# Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order. 

def find_k_freq(text, k):
    ht = {}
    for word in text.split():
        ht[word] = ht.get(word, 0) + 1
    
    return sorted(ht.keys(), key=lambda x: x[1], reverse=True)[:k]


if __name__ == "__main__":
    text = "one two three two four three five two onkke"
    k = 3
    print(find_k_freq(text, k))

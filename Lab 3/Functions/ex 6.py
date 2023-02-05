def reverse_sentence():
    sentence = input("Enter a sentence: ")
    return " ".join(sentence.split()[::-1])
print(reverse_sentence())
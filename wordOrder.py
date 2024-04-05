'''
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
'''
word = int(input())
word_dict = {}
word_list = []

for _ in range(word):
    word_input = input()
    if word_input not in word_dict.keys():
        word_list.append(word_input)
        word_dict[word_input] = 1
    else:
        word_dict[word_input] += 1
print(len(word_dict))

for word_input in word_list:
    print(word_dict[word_input], end=' ')

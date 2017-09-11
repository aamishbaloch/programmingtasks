from collections import Counter
import re


def count_words(text):
    counter_obj = Counter(re.findall("\w+", text))

    for word_count in counter_obj.most_common():
        print("Word: {} - Count: {}".format(word_count[0], word_count[1]))


def most_used_word(text):
    counter_obj = Counter(re.findall("\w+", text))

    most_common_word = counter_obj.most_common()[0]
    print("Word: {} - Count: {}".format(most_common_word[0], most_common_word[1]))


def count_words_implementation(text):
    result = {}

    for word in re.findall("\w+", text):
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    for key, value in result.items():
        print("Word: {} - Count: {}".format(key, value))


def max_used_word_implementation(text):
    result = {}

    for word in re.findall("\w+", text):
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    my_max = 0
    my_key = None
    for key, value in result.items():
        if value > my_max:
            my_max = value
            my_key = key

    print("Word: {} - Count: {}".format(my_key, my_max))



text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
max_used_word_implementation(text)

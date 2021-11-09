# Practice problem 7 tut 116 CWH Python

# Search Engine

'''
You are given few sentences as a list (Python list of sentences).
Take a query string as an input from the user.
You have to pull out the sentences matching this query
input by the user in decreasing order of relevance
after converting every word in the query
and the sentence to lowercase.
The most relevant sentence is the one with the
maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
'''


def search(sentence, query):
    '''
    :param sentence: sentences to search query from
    :param query: query provided by user
    :return: return the number of occurances of queried words
    '''
    # making list of words from sentence
    words_sentence = sentence.strip().split(" ")
    words_query = query.strip().split(" ")

    count = 0
    for word_sentence in words_sentence:
        for word_query in words_query:
            if word_sentence == word_query:
                count += 1
    return count

if __name__ == '__main__':
    sentences = ["Python is cool snake", "Python is Good",
                 "Python is not python snake"]
    query = input("Enter your query you want to search\n")

    sentences_lower = [x.lower() for x in sentences]
    query = query.lower()

    # to store number of occurances of queried words
    frequency = [0] * len(sentences)

    result = 0

    i = 0
    for sentence_lower in sentences_lower:
        frequency[i] = search(sentence_lower, query)
        if frequency[i] > 0:
            result += 1
        i += 1

    print(f"\n{result} results found:\n")
    for i in range(1,result+1):

        # taking the index of maximum number in frequency list
        print(f"{i}. {sentences[frequency.index(max(frequency))]}")

        # assigning 0 to the index with max number to get the next max index
        frequency[frequency.index(max(frequency))] = 0

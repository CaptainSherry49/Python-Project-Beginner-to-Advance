# # --------------------------- "Search Engine" ----------------------------------------- #
# """
# The task you have to perform is “Search Engine”. This task consists of a total of 20 points to evaluate your performance
#
# Problem Statement:-
#
# You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You
# have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after
# converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum
# number of matching words with the query.
#
# Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
#
# Input:
# Please input your query string
#
# “Python is”
#
# Output:
# 3 results found:
#
# python is not python snake
# python is good
# Python is cool
# """
#
#
# # ------------------ Let's Starts -------------- #

print("------------------------- Search Engine ------------------")
print()
print("You have to input a string as query and we will find you the most relevant matches for your string. ")


def matching_words(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1

    return score


if __name__ == '__main__':
    sentences = ['Python is cool', 'python is good', 'python is not python snake']

    print()
    user_inp = input("Please input your query string:\n\t").lower()
    scores = [matching_words(user_inp, sentence) for sentence in sentences]

    # print(scores)

    sortedSentScore = [SentScore for SentScore in sorted(zip(scores, sentences), reverse=True)]
    # print(sortedSentScore)

    print('---------------------------------------------')
    print(f"{len(sortedSentScore)} results found !")
    print('----------------------------------------------')

    for score, item in sortedSentScore:
        print(f"{item}")

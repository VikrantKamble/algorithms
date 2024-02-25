"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


NOTE: If the input has ordinal structure, check if sorting can help.

"""


def h_index(citations):
    # First we will sort the citations in descending order
    citations = sorted(citations, reverse=True)

    h_index = 0
    while h_index < len(citations):
        if citations[h_index] < h_index + 1:
            break

        h_index += 1

    return h_index


if __name__ == "__main__":
    print(h_index([0]))

def close_strings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    # Check that the letters match
    if set(word2) != set(word1):
        return False

    char_dict_1 = {}
    char_dict_2 = {}

    for ele in word1:
        if ele in char_dict_1:
            char_dict_1[ele] += 1
        else:
            char_dict_1[ele] = 1

    for ele in word2:
        if ele in char_dict_2:
            char_dict_2[ele] += 1
        else:
            char_dict_2[ele] = 1

    count_dict_1 = {}
    count_dict_2 = {}
    for _, value in char_dict_1.items():
        if value in count_dict_1:
            count_dict_1[value] += 1
        else:
            count_dict_1[value] = 1

    for _, value in char_dict_2.items():
        if value in count_dict_2:
            count_dict_2[value] += 1
        else:
            count_dict_2[value] = 1

    # Check that the two count dictionaries (frequencies) match
    return count_dict_1 == count_dict_2


if __name__ == "__main__":
    res = close_strings(word1="uau", word2="ssx")
    print(res)

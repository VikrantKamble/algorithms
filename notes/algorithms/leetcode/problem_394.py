def decode_string(s: str) -> str:
    my_stack = []
    num_stack = []

    pos = 0
    while pos < len(s):

        if s[pos] == "]":
            # Check how many times this sequences needs to be repeated
            this_multiplier = num_stack.pop()

            acc = []
            while True:
                ele = my_stack.pop()
                if ele == "[":
                    break
                else:
                    acc.append(ele)
            my_stack.append("".join(acc) * this_multiplier)
            pos += 1

        elif s[pos].isalpha() or s[pos] == "[":
            my_stack.append(s[pos])
            pos += 1

        else:
            curr_num = []
            while not (s[pos].isalpha() or s[pos] == "[" or s[pos] == "]"):
                curr_num.append(s[pos])
                pos += 1

            num_stack.append(int("".join(curr_num)))

    return "".join(my_stack[::-1])[::-1]


if __name__ == "__main__":
    res = decode_string(s="2[abc]3[cd]ef")
    print(res)

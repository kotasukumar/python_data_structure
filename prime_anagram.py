def reverse(num):
    return num[::-1]


def anagram(lower, upper):
    anagram_list = []
    not_anagram_list = []
    for i in range(lower, upper):
        if str(i) == reverse(str(i)):
            anagram_list.append(i)
        else:
            not_anagram_list.append(i)
    prime_list = prime(anagram_list)
    return prime_list, not_anagram_list


def prime(palindrome_list):
    dummy_list = []
    for number in palindrome_list:
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            dummy_list.append(number)
    return dummy_list


if __name__ == "__main__":
    anagram, not_anagram = anagram(0, 1000)
    print("Anagram list\n", anagram)
    print("Not anagram list\n", not_anagram)
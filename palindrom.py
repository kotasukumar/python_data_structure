import collections


def check_palindrome(string):
    deque = collections.deque()
    for i in range(len(string)):
        deque.appendleft(string[i])
    deque_to_string = ''.join(deque)

    if string == deque_to_string:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


if __name__ == "__main__":
    print(check_palindrome(str(input("Enter any word to check palindrome: "))))
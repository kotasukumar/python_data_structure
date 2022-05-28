def prime(lower, upper):
    prime_list = []

    for number in range(lower, upper):
        for j in range(2, number//2):
            if number % j == 0:
                break
        else:
            prime_list.append(number)

    return prime_list


if __name__ == "__main__":
    print(prime(0, 1000))

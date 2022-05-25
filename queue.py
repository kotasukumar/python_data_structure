def queue(person):
    bank_account_balance = 10000
    for i in range(len(person)):
        choice = int(input("hi " + person[0] + "\n1 - deposit\n2 - withdraw\nEnter your choice: "))
        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            bank_account_balance = bank_account_balance + amount
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            bank_account_balance = bank_account_balance + amount
        person.pop(0)
        print(person)

    return bank_account_balance


if __name__ == "__main__":
    n = int(input("Enter number of person in queue: "))
    name = []
    for i in range(n):
        name_Person = str(input("Entre name of the persons in queue: "))
        name.append(name_Person)
    balance = queue(name)
    print("after queue balance in bank is: ", balance)

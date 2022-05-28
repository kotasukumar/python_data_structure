def get_month(y, month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 1
    month_list = []
    for i in range(m[month - 1]):
        temp = []
        for j in range(7):
            day_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
            year = y - (14 - month) / 12
            x = year + (year / 4) - (year / 100) + (year / 400)
            month = month + 12 * ((14 - month) / 12) - 2
            day = int(d + x + 31 * month / 12) % 7
            temp.append(day_list[day])
            d += 1
        month_list.append(temp)

    return month_list


if __name__ == "__main__":
    print(get_month(2022, 5))

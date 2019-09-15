# Brute forces all dates in a century to find dates which are palindromes (the same value forwards and backwards, i.e. 9/13/19)
# Ben Rongey

count = 0
m = list(range(1, 13))

d = list(range(1, 31))

y = list(range(0, 101))
# print (y)
og_date = []
for year in y:

    # og_date.append(m)
    # og_date.append(d)
    # og_date.append(year)

    # if m <= 12:
    #     m = m + 1
    # elif m > 12:
    #     m = 1

    # if d <= 31:
    #     d = d + 1
    # elif d > 31:
    #     d = 1

    # print (og_date)
    
    for day in d:
    #     og_date.append(day)
        

        for month in m:
            # count = count +1
            # og_date = [month, day, year]
            og_date = str(month) +str(day) +str(year)
            palin_num = og_date[::-1]
            if og_date == palin_num:
                print (str(month) + '/' + str(day) + '/' + str(year))
                count = count + 1


    #         og_date.append(month)
    #         print (str(og_date[0]) + '/' +str(og_date[1]) + '/' +str(og_date[2]))
    # # print (str(m) + '/' + str(d) + '/' + str(year))
print (count)
# og_date_int = "12345"
# print (og_date_int[::-1])

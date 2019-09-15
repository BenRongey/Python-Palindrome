# Brute forces all dates in a century to find dates which are palindromes (the same value forwards and backwards, i.e. 9/13/19)
# Ben Rongey

count = 0
m = list(range(1, 13))
d = list(range(1, 31))
y = list(range(0, 101))

for year in y:
    
    for day in d:

        for month in m:

            og_date = str(month) +str(day) +str(year)
            palin_num = og_date[::-1]

            if og_date == palin_num:
                print (str(month) + '/' + str(day) + '/' + str(year))
                count = count + 1

print ("In a century there are " + str(count) + " palindrome dates!")
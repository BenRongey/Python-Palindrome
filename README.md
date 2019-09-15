# Python-Palindrome

Since yesterday someone pointed out that the date was a palindrome (9/13/19), I was curious to see what other palindrome dates occur in a 100 year period (excluding the first two digits in the year).

## The Solution

I created 3 lists to set the ranges of days months and years
```
m = list(range(1, 13))
d = list(range(1, 31))
y = list(range(0, 101))
```
I then used nested for loops to loop through all days, months, and years.  The easiest solution (instead of Python's reverse function) was [Python Slice()](https://docs.python.org/2.3/whatsnew/section-slices.html).  By forcing the dates to a string, one can then reverse slice it without complication:
```
og_date = str(month) +str(day) +str(year)
palin_num = og_date[::-1]
```

## Results

There are 400 palindrome dates in a century!  Way more than I expected!

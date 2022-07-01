    """
3. Make a upper and lower quantile calculator.
The goal is to create a program that can find the upper and lower interval of a list of number (like a numerical
confidence interval), based on some confidence level.
 a. Start by defining the variables
i. values (which is a list of random number, you
can type in yourself)
ii. alpha (a number between 0 and 1)
c. The next step is to extract the two indexes that
defines the lower and upper interval given some alpha, such that the middle 1-alpha amount of the values lands within the middle.
calculate the lower and upper index by:
remember the “round” as indexes require integers to
work with list.
d. Use the sorted list to extract the lower and upper
value, and print them.
    """
values = [8,4,5,3,6,7,8,23,456,7,4345,45,23,1,3,34,3545,45,56,45,42,46,]
alpha = 0,5

# b. Sort the list of values.
values_sorted = sorted(values)

lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2))-1
lower_ci = values_sorted[lower_idx]
upper_ci = values_sorted[upper_idx]

print(lower_idx)
print(upper_idx)

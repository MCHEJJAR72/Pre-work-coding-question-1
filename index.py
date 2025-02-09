# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.


def hello_name(user_name):
    """Display a simple greeting."""
    print("hello_" + user_name.upper() + "!")

hello_name('bryn')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


odds = range(1, 100, 2)
for odd in odds:
    print(odd)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_list(a_list):
    
    print(f"The greatest # in the list is: {a_list}")


max_num_list(max([1, 66, 101, 3]))

# Question 4
# Write a function to return if the given year is a leap year.\
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. \
# The return should be boolean Type (true/false).

#year = int(input("Tell me the year, and I will tell you if it's a leap year: "))
 #   if (year % 4 == 0):
  #      print(f"{year} is a leap year.")
    #  else:
   #     print(f"{year} is NOT a leap year.")


year = int(input("Tell me the year and I'll tell you if it's a leap year: "))

def leap_year(year):
    if (year % 4 == 0):
        print("True")
    else:
        print("False")
leap_year(year)        


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. \
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. \
# The return should be boolean Type.


#def is_consecutive(a_list):
   # sorted_list = sorted(a_list) # This will always make the if statement print no matter the argument placed.
   # r_list = list(range(min(a_list), max(a_list)+1))
    #if r_list == sorted_list:
 #       print(f"{sorted_list} is consecutive numerically.")
 #   else:
 #       print("This list is not consecutive.")


#is_consecutive([2,4,3,1,5])

def is_consecutive(a_list):
    r_list = list(range(min(a_list), max(a_list)+1)) # fix block to change depending on argument
    if a_list == r_list:
        print(f"{a_list} is consecutive numerically.")
    else:
        print(f"{a_list} is non-consecutive numerically.")


is_consecutive([1,2,3,5,4])
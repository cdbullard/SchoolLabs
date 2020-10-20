from random import randint
from math import gcd
#1
list1 = [randint(-100, 100) for _ in range(25)]
#2
print("List values are", list1, "\nList length is", len(list1))
#3
print("Average of integer in generated list is: ", sum(list1) / len(list1))
#4
print("Number of even integers is:", len([integer for integer in list1 if integer % 2 == 0]))
#5
print("Number of odd integers is:", len([integer for integer in list1 if integer % 2 != 0]))
#6
print("Number of integers greater than 0 is:", len([integer for integer in list1 if integer > 0]))
#7
print("Number of integers less than 0 is:", len([integer for integer in list1 if integer < 0]))
#8
sorted_list = sorted(list1[::])
# print(sorted_list)
print("Median of generated integer list is:", sorted_list[len(sorted_list) // 2])
#9
# also could be done as sorted_list[len(sorted_list) // 2 + 1::] Did it with below method because there is possibility that the median value can exist at the next index as well
print("integers larger than median are:", [i for i in sorted_list if i > sorted_list[len(sorted_list) // 2]])
#10
print("Integers less than median are:", [i for i in sorted_list if i < sorted_list[len(sorted_list) // 2]])
#11
user_value = input("Please input an integer to see the number of occurrences in list: ")
occurrences = [i for i in sorted_list if i == user_value]
print("Number of occurrences of:", user_value, "in the list is:", len(occurrences), "times")
#12
print("Maximum integer in the list is:", sorted_list[-1])
#13
print("Minimum integer in the list is:", sorted_list[0])
#14
print("List in reverse sorted order is:\n", sorted_list[-1::-1])
#15
# If I wasn't waiting to the last second to do this, I would try my hand at writing it from scratch :)
print("GCD of the largest and smallest number in the list is:", gcd(abs(sorted_list[0]), sorted_list[-1]))

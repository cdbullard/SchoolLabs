from random import randint

first_list = []
second_list = []
# Pleaaaaase? :)
# first_list = [randint(1, 9) for i in range(5)]
# second_list = [randint(2, 8) for i in range(5)]
for i in range(5):
    first_list.append(randint(1, 9))
print("First list: ", first_list)
for i in range(5):
    second_list.append(randint(2, 8))
print("Second list: ", second_list)
print("Largest number in each comparison:")
for i in range(len(first_list)):
    if first_list[i] > second_list[i]:
        print(f"--- {first_list[i]} ---")
    elif first_list[i] == second_list[i]:
        print(f"--- {first_list[i]} --- Integers in both lists are equal at list index {i}")
    else:
        print(f"--- {second_list[i]} ---")

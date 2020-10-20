# No User Input..whoop whoop!
from random import randint

random_numbers = tuple([randint(1, 15) for _ in range(10)])

first_three = random_numbers[0:3]
last_three = random_numbers[-1:-4:-1]
# immutable objects!  Whee!
concat_tuples = first_three + last_three
sort_tuple = tuple(sorted(concat_tuples))

print(f"Tuple of {len(random_numbers)} random numbers: ", random_numbers)
print(f"Tuple of first {len(last_three)} numbers: ", first_three)
print(f"Tuple of last {len(last_three)} numbers: ", last_three)
print("Two tuples concatenated: ", concat_tuples)
print("Two tuples concatenated and sorted: ", sort_tuple)



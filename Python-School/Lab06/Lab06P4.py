list1 = [2, 5, 7, 8]
list2 = [1, 2]

print(f"Part A: {[n * 2 + 1 for n in list1]}")
# Really looked for some mathematical pattern here, but couldn't really come up with anything other than exclusiveness
print(f"Part B: {[n + 1 for n in list1 if n + 1 == 3 or n + 1 == 9]}")
print(f"Part C: {[[n, n + 1] for n in list1]}")
print("Part D:", [[x, y] for x in list1 for y in list2])
print("Part E:", [[x + y for y in list2] for x in list1])

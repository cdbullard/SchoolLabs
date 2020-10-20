# input statements
# A = 2
# B = 3
# C = -2

x = int(input(" Please enter integer ..."))
y = int(input(" Please enter another integer ..."))
z = int(input(" Please enter the third integer ..."))

print("the numbers entered are ", x," and", y, " and ", z)
s = x + y + z
m = max(x,y,z)  # MAX function similar function for min
mn = min(x, y, z)
p = x*y*z
int_list = [x, y, z]
average = s / len(int_list)
print("The values are \n  SUM = ", s, "\n  product = ", p,  "\n  maximum = ",  m, "\n  minimum = ", mn,
      "\n  average = ", average)
print("The sum raised to the power of the minimum integer is ", s ** mn)
print("The sum divided by the minimum integer is ", s / mn)
print("The sum divided by the maximum integer is ", s // m)
print("The average of the largest and smallest integer is ", (m + mn) // 2)
print("The integers in sorted order are: ", mn, ",", s - (m + mn), ",", m)

print("My name is Jessica Chappell")
print("My major is Computer Programming and development")
print("I'm taking CSC 120, because even though I've been in the DevOps field for a couple years now and have been "
      "extremely successful, I feel that I'm missing some of the foundational knowledge of how the underlying "
      "systems and hardware operate, and it's holding me back from advancing as quickly as I\'d like.")
print("In 5 years, I aim to be a CTO for a small to mid level company")

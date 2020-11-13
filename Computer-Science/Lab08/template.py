#CSC120Lab08Template
# CSC120
# Lab 08 Template

names = ["Euclid", "Archimedes", "Newton", "Descartes", "Fermat",
     "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Lovelace",
    "Noether", "Nash", "Wiles", "Cantor", "Gauss", "Plato"]  # Initial list n == 17
# we will use alphaCount to store the number of characters in names.
# alphaCount[0] will contain the number of A and a
# alphaCount[1] will contain the number of B and b
# ….
# …
# # alphaCount[25] will contain the number of Z and z
alphaCount = [0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # length == 26

print('0', names)
print ('1', alphaCount)

# first letter and last letter in names uncomment if you want
#  use the code uncomment if you wish
j = 0
cnt = 0
#for k in names:
#    print(cnt, k, len(k), k[j], k[len(k) - 1])  # first letter and last letter in name
#   cnt = cnt + 1

# number of 'a' or 'A' using upper() function a == A
s = 0
print('Counting character a or A in names ')
ch = 'a'
for eachName in names:              # for each name in names
   for letter in eachName:         # for each letter in the name
        if letter == ch.upper()or letter == ch:
            s = s + 1
print('Number of A or a in names is ', s)

#  code to determine the number of A' B C D E  etc in names and
#  store in alphaCount using ord
print('========ORD Values===================')
print(' ord values for characters ')
print('1 ',ord('A')-ord('A'))   # 0    position in alphCount for A
print('2 ',ord('B')-ord('A'))   # 1    position in alphCount for B
print('3 ',ord('C')-ord('A'))   # 2    position in alphCount for C
# .....
print('26 ',ord('Z')-ord('A'))   # 25  position in alphCount for Z
print('AN EXAMPLE counting the number of characters in string name[1] ')
s = names[1]            #  Archimedes
# similar code needed for the list of names
print('s = ',s)
for ch in s:                            #  each character
    x = ord(ch.upper()) - ord('A')      # to uppercase;
    print('x == ',x)                                    # determine place in alphaCnt
    alphaCount[x] = alphaCount[x] + 1   # increment the array
					     # alphaCnt[x]

print('alphaCount == ', alphaCount)  	# number of ‘A’, ‘B’ etc
						# characters in s
print('====FIX the next calculations '
      'an example of what is EXPECTED ===== ')
x ='EdAsNn'
print('1. string consisting of first and last letter ',x  )
print('2. names reversed  ',x  )
print('3. total number of characters ',len(x)  )
print('4. total number of consonants ',len(x)  )
print('5. printout of alphaCount == \n',alphaCount  )
print('6. average length of all the names ',len(x)  )
print('7. the letter that appears most frequent ','Z'  )
print('8. the letter that have a value of 0 in alphaCount ','ABXYZ'  )
print('9. the median name in list names is ','CSC 120'  )
print('10.the number of vowels in names is ',333  )

'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Program: Star

'''


print("How Many Row You Want To Print")
one = int(input())
print("Type 1 Or 0")
two = int(input())
new = bool(two)
if new:
    for i in range(1, one + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif not new:
    for i in range(one, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

input()
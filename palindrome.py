'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Program: Palindrome Number

'''


n_1 = int(input("Enter any number.: "))
rev_1 = int(str(n_1)[::-1])
add_1 = n_1 + rev_1
n_2 = add_1
rev_2 = int(str(n_2)[::-1])
add_2 = n_2 + rev_2
rev_3 = int(str(add_2)[::-1])
if add_2 == rev_3:
    print("This is a Palindrome number: ", n_1)
else:
    print("This is not a Palindrome number: ", n_1)

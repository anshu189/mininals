'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: pywhatkit (pip install pywhatkit)
Program: Direct Youtube Video Player 

'''

import pywhatkit as kit


def main():

    input_query = input("Enter Any Video Query For Direct Play: ")

    if input_query == "help" or input_query == "Help":
        print("1. You Can Search For The Most Appropriate Keywords Of Songs And Specific Videos (Famous one's).\n2. Type 'exit' OR 'Exit' for Exit. ")
        print(kit.help())
        main()

    elif input_query == "exit" or input_query == "Exit":
        exit(kit)

    else:
        kit.playonyt(input_query)


if __name__ == '__main__':
    main()

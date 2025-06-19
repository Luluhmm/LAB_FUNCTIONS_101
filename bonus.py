#luluh almogbil
'''
# Bonus
Rewrite the previous function so that it returns the pattern as a string, then assign the result to a variables and print it.

'''
# number = 5
# print (number)
# numberstr = str(number) #this will convert the number to string
# print(numberstr)

def countdown(number):
    result = ""
    while number > 0:
        for i in range(number,0,-1):
            #print(i,end=" ")
            result = result + str(i) + " " # > result is "" then "5" > "5"+"4" >"5 4"< will be the result and then "5 4"+ "3"="5 4 3" and so on
        #print()#for new line after each iteration
        result = result+ "\n" # 5 4 3 2 1 then new line, result will be such a container to return it after, like a stack or queue
        number-=1
    return result

number = int(input("Please enter a number: "))
#countdown(number)
print(countdown(number))

#Luluh Almogbil
'''
# LAB_FUNCTIONS_101

## Create a function that takes 1 parameter of type int , 
then it prints out the result formatted like the following patter (if we give it 5 for example):

**Example Output for `5`**
```
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
```

#### Document the newly created function. describe what it does, then print the documentation.
'''


#defining the function
def calculate(number):
    """
    This function will take a number from the user and then will display a countdown for that number in a pretty way
    """
    while number > 0:
        for i in range(number,0,-1):
           print(i,end=" ")

        print()
        number-=1
    

#call the function
number = int(input("Please enter a number: "))
calculate(number)
print(calculate.__doc__)
   
        
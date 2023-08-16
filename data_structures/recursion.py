'''Adds together the number of characters for each string in an array of string, for a total count of characters in the array'''
def addString (array):
    if(len(array) == 1):
        return len(array[0])
    else:
        return len(array[0]) + addString(array[1:]) 
    
    #Think of the example of len(array) = 2 
    #It will start at else, before it can finish it will call the function addString again
    #This time it will go to the base case, will return that value to addString 
    #this will complete the function run, as now it has an answer for addString!



'''Provides an array of even numbers only'''
def FindEven(array, list_even=[]):
    if (len(array)== 1):
        if (array[0]%2 == 0):
            list_even.append(array[0])
            return list_even
        else:
            return list_even
    elif (array[0]%2 == 0):
        list_even.append(array[0])
        return FindEven(array[1:],list_even)
    else:
        return FindEven(array[1:],list_even)



        
charString = ["helllo", "hi", "omg"]
final = addString(charString)
evenstr = [2, 7, 0, 5, 3, 8, 16]
finale = FindEven(evenstr)
print("hello")
print(f'final count:{finale}')
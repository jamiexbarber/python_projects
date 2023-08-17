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
    #Base Case - there's only one element and the function is to return a list
    if (len(array)== 1):
        if (array[0]%2 == 0):
            list_even.append(array[0])
            return list_even
        else:
            return list_even
    #If not "Base Case", start with first element, add to the list, and call the function again to check the rest of the array
    #Until we get to the "Base Case"
    elif (array[0]%2 == 0):
        list_even.append(array[0])
        return FindEven(array[1:],list_even)
    else:
        return FindEven(array[1:],list_even)
    
''' Triangular Numbers, returns a number that is the correct number from the series
 e.g N number gives N + the previous number. If N = 4, then N[1] => 1, N[2] => N[1]+2 = 3, N[3] => N[2]+3 = 6, N[4] => N[3]+4 = 10 '''
def TriangularNumber(N):
    if N == 1:
        return 1
    else:
        return N + TriangularNumber(N-1)

'''Accepts a string and returns the index of the first x character found in the string'''
def FindX(array, index = 0):
    if (len(array) == 1):
        return index
    else:
        if (array[0] == 'x'):
            return index
        else:
            index+=1
            return FindX(array[1:],index)


        
charString = ["helllo", "hi", "omg"]
final = addString(charString)
evenstr = [2, 7, 0, 5, 3, 8, 16]
finale = FindEven(evenstr)
trig = TriangularNumber(6)
index = FindX("aaaaxaaax")
print("hello")
print(f'final count:{index}')
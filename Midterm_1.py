from typing import List, Tuple
def foo(bar: int, baz: int = 1) -> Tuple[int, int, str]:
assert condition, "some string" #raises assertion error with message “some string” if condition is False
float("2.5") #converts string to a floating-point number
#docstring
def foo(bar: str) -> float:
    """_summary_

    Args:
        bar (int): _description_

    Returns:
        float: _description_
    
    Raises:
        ValueError: If the user inputs a non-float value
    """
    try:
        x = float(bar)
    except ValueError:
        print("Input must be a float")
        x = -1
    return x
#string methods
s = "hello old"
s.isalpha() #return True if all characters are letters
s.lower() #converts s to all lowercase
s.upper() #converts s to all uppercase
s.capitalize() #capitalizes first character of s
s.title() #capitalizes 1st character of each word in s
s.strip() #removes leading/trailing whitespace
s.lstrip() #removes leading whitespace
s.rstrip() #removes trailing whitespace
s.replace("old", "new") #replaces all instances of 'old' with 'new'
s.split(",") #splits at commas
words = ["Hello","World"]
",".join(string_iterable) #combines all itemsin iterable (must be strings) into one string, separated by ","
s.find('el') #returns lowest index of 'el' in s. Returns -1 if not found.
s.count('ll') #reurns # of non-overlapping occurences of 'll' in s
s.startswith("hel") #returns true if s starts with 'hel'
s.endswith('old')
s.isdigit() #returns True if all characters in s are digits
s.isalnum() #returns True if all characters are alphanumeric
s.isspace() #returns True if all characters are whitespace
#slicing
s[::] #start defaults to 0, stop defaults to end, step defaults to 1
s[::-1] #start defaults to end, stop defaults to beginning
s[3::-1] #goes backwards from 3 to beginning
s[-3:] #last three characters
#lists
l=[1,2,3,4,5]
list(iterable) #returns elements of iterable in list
l.extend(iterable) #appends items from iterable
l.insert(i, x) #inserts x at index i
l.remove(x) #removes first instance of x
l.pop(i=-1) #removes ith term from list
l.clear() #removes everything from list
l.index(item, start=0, end=len(l)) #returns index of item in l[start:end]. Raises Error if not found
l.count(x) #returns number of times x appears in list
l.sort(key=None, reverse=False)
l.reverse() #in place
l.copy() #returns shallow copy
#unpacking operator (*)
*l = iterable #converts iterable to list
f,*r,l = "unpack a string" # f='u', r=['n',p','a',...,'n'], l='g'
#enumeration
enumerate(iterable) #returns iterable of tuples (index, val)
enumerate(['a','b','c']) #returns iterable containing (0,'a'), (1,'b'), (2,'c')
#tuples
tuple(iterable) #returns tuple with items of iterable
tuple(1,2) #raises Error
x = (1) #x is an int
x = (1,) #x is a tuple
x[0] = 2 #not allowed

bar = lambda baz,qux,quux=0: baz + qux + quux #quux has default value 0
filter(func, iterable) #returns 'filter object' iteratable containing the items x of iterable satisfying func(x)
#reduce
reduce(func, iterable, initializer) #applies func repeatedly to elements of iterable, starting w. initializer
reduce(func, iterable) #applies func repeatedly to elements of iterable, starting with first element
reduce(lambda x, y: x + y, [1,2,3,4,5], 7) #returns 7 + 1 + 2 + 3 + 4 + 5
reduce(lambda x, y: x + y, [1,2,3,4,5]) #returns 1 + 2 + 3 + 4 + 5
#list comprehension
[i for i in iterable]
[i for i in iterable if condition(i)] #list of elements of i satisfying condition(i)
[(x,y) for x in iterable_1 for y in iterable_2 if condition(x,y)]












    
	

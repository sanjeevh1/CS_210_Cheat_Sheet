from typing import List, Tuple
def foo(bar: int, baz: int = 1) -> Tuple[int, int, str]:
assert condition, "qux" #raises AssertionError w. message “qux” if condition is False
float("2.5") #converts string to a floating-point number
#string methods
s.isdigit() #returns True if all characters in s are digits
s.isalnum() #returns True if all characters are alphanumeric
s.isspace() #returns True if all characters are whitespace
s.isalpha() #return True if all characters are letters
s.lower(), s.upper() #converts s to all upper/lowercase
s.capitalize() #capitalizes first character of s
s.title() #capitalizes 1st character of each word in s
s.lstrip(), s.rstrip(), s.strip() #removes leading/trailing/both whitespace
s.replace("old", "new", c=-1) #replaces up to c instances (or all if c = -1) of 'old' w. 'new'
s.split(",", m=-1) #splits at ',' at most m times, or all occurences if m = -1
','.join(string_iterable) #combines all strings in iterable into 1 string, separated by ','
s.find('el') #returns lowest index of 'el' in s. Returns -1 if not found.
s.count('ll') #reurns # of non-overlapping occurences of 'll' in s
s.startswith("hel"), s.endswith('old') #returns true if s starts/ends with 'hel'
#slicing
s[::] #start defaults to 0, stop defaults to end, step defaults to 1
s[::-1] #start defaults to end, stop defaults to beginning
s[3::-1] #goes backwards from 3 to beginning
s[-3:] #last three characters
#lists
list(iterable) #returns elements of iterable in list
my_list.extend(iterable) #appends items from iterable
my_list.insert(i, x) #inserts x at index i
my_list.remove(x) #removes first instance of x
my_list.pop(i=-1) #removes ith term from list
my_list.clear() #removes everything from list
my_list.index(x, start=0, end=len(l)) #returns index of x in l[start:end]. Error if not found
my_list.count(x) #returns number of times x appears in list
my_list.sort(key=None, reverse=False)
my_list.reverse() #in place
my_list.copy() #returns shallow copy
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
#lambda/filter
bar = lambda baz,qux,quux=0: baz + qux + quux #quux has default value 0
filter(fun, iterable) #returns iteratable containing items x of old iterable satisfying fun(x)
#reduce
reduce(fun, iterable, initializer) # fun(...fun(fun(initializer,iterable[0]),iterable[1])...)
reduce(fun, iterable) #applies fun repeatedly to elements of iterable, starting w. 1st element
reduce(lambda x, y: x + y, [1,2,3,4,5], 7) #returns 7 + 1 + 2 + 3 + 4 + 5
reduce(lambda x, y : x + y, [1,2,3,4,5]) #returns 1 + 2 + 3 + 4 + 5
#list comprehension
[i for i in iterable if condition(i)] #list of elements of i satisfying condition(i)
[(x,y) for x in iterable_1 for y in iterable_2 if condition(x,y)]
#generator
g = (item for item in iterable) #g is a generator object
next(generator, default) #returns next item in generator, or default if no more items
#file IO
with open("foo.txt", 'w') as file:
    file.write("Hello\n") #no '\n' -> next write will start on same line
    file.write("Something")
file = open("foo.txt")
s = file[0] #includes newline if file[0] not last line
file.close() #'open' w/o 'with' -> must call close at end
print("Yes") if condition else print("No") #ternary
#dict
my_dict.get(key, default) # returns my_dict[key] if it exists, otherwise returns default
my_dict = dict.fromkeys(iterable, 10) # {key : 10 for key in iterable}
my_dict.keys(), my_dict.values(), my_dict.items() #returns iterable of keys/vals/tuples
#if key not in my_dict, then my_dict[key] returns None
my_dict = dict(iterable) # {key : val for (key, val) in iterable}
del my_dict['a'] #if no key 'a', raises KeyError; otherwise, deletes key 'a'
val = my_dict.pop(key, default) #removes/rets my_dict[key] if exists, otherwise rets default
#defaultdict
from collections import defaultdict
int_dict = defaultdict(int) #all vals for any key initialized to 0
list_dict = defaultdict(list) #all vals are empty list
list_dict['a'].append(1), int_dict['a'] += 1
#Counter
from collections import Counter
counter = Counter([1,2,3]) 
counter.elements() #returns iterator of elements, where each element x appears counter[x] times
counter.most_common(n) #returns n most common elements (equal count -> goes by 1st occurence)
counter.subtract(iterable) #subtracts y from counter[x] for (x,y) in iterable 
counter.subtract(Counter({1: 1, 4: 1, 2: 3}))
counter.update(iterable) #same as subtract but instead adds; must be iterable, not element
counter.update(1) #not allowed
counter.update([1]) #allowed
counter.total() #sum of counts
counter.clear() #removes all elements from counter
counter.copy() #shallow copy of counter














    
	

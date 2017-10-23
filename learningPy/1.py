from array import array

#array
a = [2, 0, 6, 5, 4, 3, 1, 6, 9, 5]
print(a[0])

b = [["X","O","X"], ["O","O","X"], ["X","X","O"]]
print(b[1][1])



# Create an int array of three elements.
a = array("i", [10, 20, 30])

# Display elements in array.
for value in a:
    print(value)


## list
student = ["Name", "Cindy", "Age", 20]
print(student[1])
print (student.count('Name'))
print len(student[1])

mynames = ["Sam", "Pit", "Misch"]
for n in mynames:
    print "HELLO ", n

values = ["meow", "bark", "chirp"]
for pair in enumerate(values):
    # The pair is a 2-tuple.
    print(pair)

#tuple to list
odds = (9, 5, 11)
# Convert tuple to list and sort.
list1 = list(odds)
list1.sort(reverse=True)
print(list1)


#dictionary
style = {"Monet": "impressionist", "Rembrandt": "Baroque"}
style['pytho']= 'pycharm'
print(style["pytho"])


#tuples
a = ()
b = ("one",)
c = ("one", "two")
(x, y) = (5, 3)
coordinates = (x, y)
dimensions = (8, 5.0, 3.14)
print coordinates
print dimensions

#in keyword
pair = ("dog", "Cat")
# Search for a value.
if "cat" in pair:
    print("Cat found")

# slices
values = (1, 3, 5, 7, 9, 11, 13)
print(values[:])
print(values[1:])
print(values[:1])
print(values[2:4])

#index
items = ("cat", "dog", "bird")
index = items.index("dog")
print(index, items[index])

#count
values = (1, 2, 2, 3, 3, 3)
print(values.count(1))
print(values.count(3))


value = "abcdefgh"
pairs = []
for i in range(1, len(value), 2):
    one = value[i - 1]
    two = value[i]
    pairs.append((one, two))
    print pairs

# Display list of tuple pairs.
for pair in pairs:
    print(pair)



# range
r1 = range(11)
r3 = range(4,21,2)
print r1
print r3

#function
def area(b,h):
    A = b * h
    return A

print(area(2,3))

def peri(l):
    P = 4 * l
    return P

print(peri(2))

age = input("What is your age? ")
print "Your age is: ", age

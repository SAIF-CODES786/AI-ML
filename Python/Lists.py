marks = [85, 92, 78, 96, 88]
print(marks) # list are mutuable
print(len(marks)) # 5
marks[2] = 80 # changing the value at index 2
print(marks) # [85, 92, 80, 96, 88]
print(marks[0:3]) # [85, 92, 80]

#methods of list
marks.append(90) # adding an element at the end of the list
print(marks) # [85, 92, 80, 96, 88, 90]
marks.insert(2, 75) # adding an element at index 2
print(marks) # [85, 92, 75, 80, 96, 88, 90]
marks.sort() # sorting the list in ascending order
print(marks) # [75, 80, 85, 88, 90, 92, 96]
marks.reverse() # reversing the list
print(marks) # [96, 92, 90, 88, 85, 80, 75]


#loops
x = 96
idx = 0
for mark in marks:
    if (mark == x):
        print(f"Found {x} at index {idx}")
        break
    idx += 1
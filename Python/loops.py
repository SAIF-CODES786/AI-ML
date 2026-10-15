count = 1
while(count<=5):
    print("hello world")
    count +=1
















# for loops -sequential

string = "hello"
if 'o' in string:
    print("o exists in string")

# in => mmembership operator
for var in string:
    print(var)


# for i in range(5):
#     print(i)

word = "artificial intelligence"
ans = 0
for var in word:
    if(var=='i'):
        ans +=1

print(ans)


# vowels count
word = "artifical intelligence"
count = 0
for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count += 1
print("ans = ", count)


# range of loop
for i in range(1,10,2):
    print(i)

sum = 0
for i in range(1,6):
     sum += i

print(sum)
def hello():
    print("hello")

hello()

# fn definition
def sum(a,b): # parameter
    s = a+b
    return s



# fn call
ans=sum(3,4) # argument
print(ans)

# calc avg
def calc_avg(a,b,c=3):  # default parameter
    sum = a+b+c
    return sum/3

print(calc_avg(5,6,7))



# lambda fn - higher order fn which has () or return
sum = lambda a,b: a+b
print(sum(4,5))

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
       fact=fact*i
    return fact

n = int(input("enter n"))
print(calc_fact(n))
     

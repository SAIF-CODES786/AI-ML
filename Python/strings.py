word="python"
word2="programming"
sentence = word + " is a great language for " + word2 + "."
print(sentence)
print(word[0]) # p
print(word[1]) # y
print(word[2]) # t
print(len(word)) # 6


word = "python"
for ch in word:
    print(ch)

word[2] = 'T' # TypeError: 'str' object does not support item assignment

# strings are immutable in python

# slicing
word = "python"
print(word[0:3]) # pyt
print(word[2:5]) # tho
print(word[::2]) # pto


print(word[::-1]) # nohtyp


# string formatting

# format() method
name = "John"
age = 25
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)
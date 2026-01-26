# here is the code for string slicing

#h
'''  
to slice string we should use these command
a="harry"
print(a[0:5])where 0 included and 5 is not included
string counting starts form zer0
output(harry)

another example
print(a[0:-3]) here -3 will be changed to 2
output[har]

another example
print(a[-4:-3]) here -4 will be changed to 1 and -3 will be changed to 2
so it will be [1:2]



'''

#here is string methods
 # changing case
'''
a="harry welcome"

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())
'''

#searching and counting
'''
text = "hello world, hello python"
print(text.count("hello"))
print(text.find("world"))
print(text.index("python"))
print(text.startswith("hello"))
print(text.endswith("python"))'''

#modifying and cleaning
'''
text = "   python is fun   "
print(text.strip())
print(text.rstrip())
print(text.lstrip())
print(text.replace("fun","mast"))

words = "apple,banana,grape"
print(words.split())

word_list = ['I', 'love', 'Python']
print(" ".join(word_list))'''
#checking content
'''
text1 = "Python"
text2 = "12345"
text3 = "Python3"
text4 = "   "
print(text1.isalpha())
print(text1.isalnum())
print(text2.isdigit())
print(text4.isspace())
print("Hello World".istitle())'''

#formating

name = "Bishal"
age = 17

'''
print("my name is {} and my age is {}".format(name,age))
print(f"my name is {name} and my age is {age}")
num="5"
print(num.zfill(3)) '''
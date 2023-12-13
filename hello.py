colors = "red,blue,green,orange"
thislist = ["apple", "banana", "cherry"]

transform = colors.split(",", 2)

print(transform)
print(thislist)
print("Hello Drew")
print("More \ntext")


# simply iterate through the list to see what is in it
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#iterate through a string
word = "Testytesterson"
for x in word:
   print(x)

#add a simple condition
fruits = "apple", "banana", "cherry"
for x in fruits:
  if x == "banana":
    break  
  print(x)

# PS C:\Users\Drew\Desktop\dev\python\flask_postgres> py hello.py

# https://www.python-engineer.com/posts/string-methods-python/

# Create new github repo > get url for repo > git init > git add > git commit -m "" > 
# git remote add origin <url> > set upstream > git push

a = 200
b = 33
i = 1

#if statement
if a > b: print("a is greater than b")

#if elseif else long version
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#while loop

while i < 6:
  print(i)
  i += 1


# iterate list backwards
for c in reversed(fruits):
     print(c)


print("you are here")
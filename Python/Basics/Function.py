###
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

##global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
###
print("second")
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) ## x is have still the value (fantastic) becouse of global
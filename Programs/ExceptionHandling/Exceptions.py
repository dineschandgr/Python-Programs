#The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")



try:
  10 / 0
except:
  print("divide by 0 error")


#multiple exceptions
print("enter a divisor")
a = int (input())
try:
  10 / a
except ZeroDivisionError:
  print("divide by 0 error")
else:
  print("other error")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Hello World")
  except:
    print("Something went wrong when writing to the file")
  finally:
    print("finally always works")
    f.close()
except:
  print("Something went wrong when opening the file")
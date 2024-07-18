print(x)

#The try block will generate an exception, because x is not defined:
try:
  print(x)
except Exception as e:
  #print("An exception occurred ",e.with_traceback())
  print("An exception occurred ",e)



try:
  10 / 0
except Exception as e:
  print("divide by 0 error : ", e)


#multiple exceptions
print("enter a divisor")
a = int (input())
print(a)
try:
  10 / a
except ZeroDivisionError as ze:
  print("divide by 0 error : ", ze)
except Exception as e:
  print("exception ", e)
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
  f = open("demofile.txt",'w')
  try:

    f.write("Hello World")
  except Exception as e:
    print("Something went wrong when writing to the file : ",e)
  finally:
    print("finally always works")
    f.close()
except:
  print("Something went wrong when opening the file")
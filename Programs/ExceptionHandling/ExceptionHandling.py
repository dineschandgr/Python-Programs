
def exception_test(divisor):
   try:
    a =  10 / divisor
   except:
       print("error in  function")

exception_test(0)


def exception_test1(divisor):
    a = 10 / divisor

try:
    exception_test1(0)
except:
    print("error in caller")

def exception_test(divisor):
   try:
    a =  10 / divisor
   except Exception as e:
       print("error in  function : ", e)

exception_test(0)


def exception_test1(divisor):
    a = 10 / divisor

try:
    exception_test1(0)
except:
    print("error in caller")

exception_test1(0)
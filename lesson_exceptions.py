      
   
def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b)

try:  
    additoin(10, 20)
except NameError as error :
     print("the name",error.name,"is not defined")
else :
    print("the operation is successful")
class Greator_operator:  
    def __init__(self, X):  
        self.X = X  
    def __gt__(self, U):  
        if(self.X > U.X):  
            return True  
        else:  
            return False
          
i=int( input( print ("Please enter the value: ")))  
h=int (input( print("Please enter the value: "))) 
x = Greator_operator(i)
y = Greator_operator(h) 
if(x > y):  
    print ("The x is greater than y")  
else:  
    print ("The y is greater than x")
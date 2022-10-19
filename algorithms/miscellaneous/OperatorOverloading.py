class E_1:  
    def __init__(self, X):  
        self.X = X  
    def __lt__(self, U):  
        if(self.X < U.X):  
            return "object_1 is less than object_2"  
        else:  
            return "object_2 is less than object_1"  
    def __eq__(self, U):  
        if(self.X == U.X):  
            return "Both the objects are equal"  
        else:  
            return "Objects are not equal"  
                   
object_1 = E_1(int( input( print ("Please enter the value: "))))  
object_2 = E_1(int( input( print ("Please enter the value: "))))  
print (": ", object_1 < object_2)  
   
object_3 = E_1(int( input( print ("Please enter the value: "))))  
object_4 = E_1(int( input( print ("Please enter the value: "))))  
print (": ", object_3 == object_4) 

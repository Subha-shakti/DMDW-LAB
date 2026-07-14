class Employee:
    def __init__(self):
         self.empid = int(input("enter employee id "))
         self.name = input("enter employee name ")
         self.basicpay = float(input("enter basic pay "))
         self.ta = float(input("enter ta "))
         self.da = float(input("enter da "))

   
        
    def calc(self):
        self.grosspay = self.basicpay + (0.10 * self.ta) + (0.40 * self.da)

   
    def disp(self):
        print("\nEmployee Details")
        
        print("Employee ID ", self.empid)
        print("Name  ", self.name)
        print("Basic Pay ", self.basicpay)
        print("ta ", self.ta)
        print("da", self.da)
        print("Gross Pay ", self.grosspay)



emp = Employee()
emp.calc()
emp.disp()

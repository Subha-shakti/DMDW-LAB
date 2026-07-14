class Product:
    def input(self):
        self.pno = int(input("enter product number: "))
        self.pname = input("enter product name: ")
        self.cost = float(input("enter product cost: "))
        self.quty = int(input("enter product quantity: "))

    def calculate(self):
        self.tamount = self.cost * self.quty

    def display(self):
        print("product Number :", self.pno)
        print("product Name   :", self.pname)
        print("product Cost   :", self.cost)
        print("quantity       :", self.quty)
        print("total Amount   :", self.tamount)



products = []

for i in range(5):
    print("\n enter product", i+1)
    p = Product()
    p.input()
    p.calculate()
    products.append(p)


highest = products[0]

for p in products:
    if p.tamount > highest.tamount:
        highest = p

print("product with Highest Total Amount")
highest.display()

class Customer:
    Name = ""
    Lastname = ""
    Age = 0

    fathername = ""
    faterLastname = ""
    fatherAge = 0

    motherrName = ""
    motherLastname = ""
    motherAge = 0


    def AddSinovac(self):
        print("Added Sinovac to",self.Name,self.Lastname,self.Age)
        print("Added Sinovac to", self.fathername, self.faterLastname, self.fatherAge)
        print("Added Sinovac to", self.motherrName, self.motherLastname, self.motherAge)

customer1 = Customer()
customer1.Name ="Prayut"
customer1.Lastname ="J"
customer1.Age=67
customer1.fathername ="Prawit"
customer1.faterLastname ="T"
customer1.fatherAge=75
customer1.motherrName ="Parena"
customer1.motherLastname ="k"
customer1.motherAge=45
customer1.AddSinovac()
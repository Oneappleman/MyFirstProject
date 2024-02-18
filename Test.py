class Soda:
    drink1 = "Cola"
    drink2 = "Sprite"
    drink3 = "Dobryi"
    drink4 = "Pepsi"
    #dobavka1 = input("Write dobavku: ")
    #dobavka2 = input("Write dobavku: ")
    #dobavka3 = input("Write dobavku: ")
    #dobavka4 = input("Write dobavku: ")


    def __init__(self, dobavka):
        self.dobavka = dobavka

    def show_my_drink(self):
        if self.dobavka == "":
            print("Regular Soda")
        else:
            print("Flavour Soda")

dobavka1 = Soda("Lime")

print(dobavka1)
#dobavka2 = Soda(input("Write dobavku: "))
#dobavka3 = Soda(input("Write dobavku: "))
#dobavka4 = Soda(input("Write dobavku: "))

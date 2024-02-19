class Soda:
    drink1 = "Soda"
    def __init__(self, dobavka):
        self.dobavka = dobavka

dobavka1 = Soda(input("Write dobavku: "))
def show_my_drink():
    if dobavka1.dobavka == "":
        print("Regular Soda")
    else:
        print(Soda.drink1 + " with flavour:" + dobavka1.dobavka)
show_my_drink()





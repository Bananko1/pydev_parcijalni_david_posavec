import json
from datetime import date

# TODO: Dodati type-hinting na sve funkcije!


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offer: str, products: str, customers: str) ->None:
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    new_offer_customers = customer_select(customers)
    today_date = date.today()
    today_date = today_date.strftime("%y-%m-%d")
    new_offer_products = product_select(products)
    offer.append(new_offer_append(offer, new_offer_customers, today_date, new_offer_products).copy())


    
        
def customer_select(customers: str) ->str:
    print("Molimo unesite kupca iz liste postojecih.")
    num = 1

    for index in customers:
        print(f"{num}\t", end = '')
        if len(index['name']) >= 20:
            print(f"Ime: {index['name']}\t", end = '')
        else:
            print(f"Ime: {index['name']}\t\t", end = '')

        if len(index['email']) >= 25:
            print(f"Email: {index['email']}\t", end = '')
        else:
            print(f"Email: {index['email']}\t\t", end = '')
        
        print(f"VAT ID: {index['vat_id']}")
        num += 1

    while True:
        choice = input("Izbor: ")

        if int(choice) <= num and int(choice) >= 1:
            return (customers[int(choice)-1]['name'])

        else:
            print("Krivi izbor. Try Again.")

def product_select(products: str) ->list:
    new_offer_products = []
    new_offer_dict ={
    }
    
    for index in products:
        max_index = index['id']

    print("Molimo unesite proizvod iz liste postojecih.")

    while True:
        while True:
            for index in products:
                print(f"{index['id']}. Ime: {index['name']}. Opis: {index['description']}. Cijena: {index['price']}")
                
            try:
                choice = int(input("Izbor: "))-1
            except:
                print("Krivi izbor. Samo brojevi")

            if int(choice) <= max_index-1 and int(choice) >= 0:
                while True:
                    #new_offer_dict = products[choice]
                    new_offer_dict['product_id'] = products[choice]['id']
                    new_offer_dict['product_name'] = products[choice]['name']
                    new_offer_dict['description'] = products[choice]['description']
                    new_offer_dict['price'] = products[choice]['price']
                    try:
                         new_offer_dict['quantity'] = int(input("Unesite kolicinu: "))
                    except:
                        print("Nemoguc unos. Samo brojevi.")
                    new_offer_dict['item_total'] = choice * new_offer_dict['price']
                    new_offer_products.append(new_offer_dict)
                    break
                while True:
                    try:
                        if int(input("Zelite li dodati jos jedan proizvod u kosaricu?\n1. Da\n2. Ne\nIzbor: ")) == 2:
                            return new_offer_products
                        else:
                            break
                    except: 
                        print("Krivi izbor. Try Again.")

            else:
                print("Krivi izbor. Unesite broj unutar raspona..")

def new_offer_append(offers: str, new_offer_customers: str, today_date: str, new_offer_products: str) ->dict:
    
    tax = 0.1
    new_offer = {
        "offer_number": 0,
        "customer": "None",
        "date": "None",
        "items": [],
        }
    

    new_offer['offer_number'] = len(offers) + 1
    new_offer['customer'] = new_offer_customers
    new_offer['date'] = today_date
    new_offer['items'] = new_offer_products
    sub_total = 0
    for index in new_offer['items']:
        sub_total += index['item_total']
    new_offer['sub_total'] = sub_total
    new_offer['tax'] = new_offer['sub_total'] * tax
    new_offer['total'] = new_offer['sub_total'] + new_offer['tax']
    
    return new_offer


    


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products: str) ->list:
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke

    
    while True: 
        print("Dodavanje i azuriranje proizvoda")
        print("1. Dodavanje proizvoda")
        print("2. Azuriranje postojećeg proizvoda")
        print("3. Završi")
        choice = input("Izbor: ")

        if choice == '1':
            for index in products:
                max_index = index['id']
            
            while True:
                while True:
                    new_name = input("Unesite ime proizvoda: ")
                    if new_name == '':
                        print("Ime proizvoda ne moze biti prazno: ")
                    else:
                        break
                while True:
                    new_description = input("Unesite opis proizvoda: ")
                    if new_description == '':
                        print("Opis proizvoda ne moze biti prazan: ")
                    else:
                        break
                while True:
                    new_price = input("Unesite cijenu proizvoda: ")
                    if new_price == '':
                        print("Cijena proizvoda ne moze biti prazna: ")
                    else:
                        break
                new_product = {
                    "id": (max_index + 1),
                    "name": new_name,
                    "description": new_description,
                    "price": new_price,
                }
                print(f"Potvrdite unos. Ime: {new_name}. Opis: {new_description}. Cijena: {new_price}")
                choice = input("Potvrdite dodavanje.\n1. Dodaj proizvod.\n2. Ponovi unos.\nIzbor: ")
                if choice == '1':
                    products.append(new_product)
                    while True:
                        print(new_product)
                        choice = input("Želite li dodati još jedan proizvod?\n1. Dodaj još proizvoda.\n2. Završi unos.\nIzbor: ")
                        if choice == '1':
                            break
                        if choice == '2':
                            print(new_product)
                            return products
                        elif choice != '2' and choice != '1':
                            print("Krivi unos.")
                            
        elif choice == '2':
            while True:
                for index in products:
                    max_index = index['id']
                print("Izmjena postojecih proizvoda.")
                for index in products:
                    print(f"{index['id']}. Ime: {index['name']}. Opis: {index['description']}. Cijena: {index['price']}")
                choice = input("Izbor: ")
                if int(choice) <= max_index and int(choice) >= 1:
                    while True:
                        index = choice
                        choice = input("Sto zelite izmjeniti.\n1. Ime.\n2. Opis.\n3. Cijenu.\nIzbor: ")
                        if choice == '1':
                            while True:
                                new_name = input("Unesite novo ime proizvoda: ")
                                if new_name == '':
                                    print("Ime proizvoda ne moze biti prazno: ")
                                else:
                                    products[int(index) - 1]['name'] = new_name
                                    break
                        if choice == '2':
                            while True:
                                new_description = input("Unesite novi opis proizvoda: ")
                                if new_description == '':
                                    print("Opis proizvoda ne moze biti prazan: ")
                                else:
                                    products[int(index) - 1]['description'] = new_description
                                    break
                        if choice == '3':
                            while True:
                                new_price = input("Unesite novu cijenu proizvoda: ")
                                if new_price == '':
                                    print("Cijena proizvoda ne moze biti prazna: ")
                                else:
                                    products[int(index) - 1]['price'] = new_price
                                    break
                        choice = input("Izmjeni jos nesto od proizvoda?\n1. Da.\n2. Ne.")
                        if choice == '2':
                            break
                        elif choice != '2' and choice != '1':
                            print("Krivi unos. Try again.")
                    choice = input("Izmjeni jos jedan proizvod?\n1. Da.\n2. Ne.")
                if choice == '2':
                    break
                elif choice != '2' and choice != '1':
                    print("Krivi unos. Try again.")
                    return products
        elif choice == '3':
            break       


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers:str)->list:
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca

    while True: 
        print("Dodavanje i pregled kupaca")
        print("1. Dodavanje kupaca")
        print("2. Pregled svih kupaca")
        print("3. Izlaz.")
        choice = input("Izbor: ")

        if choice == '1':
            while True:
                while True:
                    new_name = input("Unesite ime kupca: ")
                    if new_name == '':
                        print("Ime kupca ne moze biti prazno: ")
                    else:
                        break

                while True:
                    new_email = input("Unesite email kupca: ")
                    if new_email == '':
                        print("Email moze biti prazan: ")
                    else:
                        break

                while True:
                    new_vat_id = input("Unesite VAT ID kupca: ")
                    if new_vat_id == '':
                        print("VAT ne moze biti prazan: ")
                    else:
                        break

                new_customer = {
                    "name": new_name,
                    "email": new_email,
                    "vat_id": new_vat_id,
                }
                print(f"Potvrdite unos. Ime: {new_name}. Email: {new_email}. VAT ID: {new_vat_id}")
                choice = input("Potvrdite dodavanje.\n1. Dodaj novog kupca.\n2. Ponovi unos.\nIzbor: ")
                if choice == '1':
                    customers.append(new_customer)
                    while True:
                        print(new_customer)
                        choice = input("Želite li dodati još jednog kupca?\n1. Dodaj još kupaca.\n2. Završi unos.\nIzbor: ")
                        if choice == '1':
                            break
                        if choice == '2':
                            print(new_customer)
                            return customers
                        elif choice != '2' and choice != '1':
                            print("Krivi unos.")
        elif choice == '2':
            num = 1
            for index in customers:
                print(f"{num}. Ime: {index['name']}. Email: {index['email']}. VAT ID: {index['vat_id']}")
                num += 1
        elif choice == '3':
            break            
   


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offer: dict)->None:
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    while True:
        print("Ponude\n1. Ispisi sve ponude.\n2. Ponude za odredjeni mjesec.\n3. Potrazi ponudu pomocu ID-a\n4. Završi")
        choice = input("Izbor: ")
        if choice == '1':
            for index in offer:
                print_offer(index)
        elif choice == '2':
            while True:
                month_choice = input("Unesite zeljeni mjesec: ")
                if int(month_choice) >= 1 and int(month_choice) <= 12:
                    for index in offer: 
                        if index['date'][5 : 7] == month_choice:
                            print_offer(index)

                else:
                    print("Krivi unos. Again.")
        elif choice == '3':
            while True:
                choice = input("Unesite ID ponude: ")
                for index in offer:
                    if int(choice) == index['offer_number']:
                        print(index)
                        break
                    else:
                        print("Please try again.")
        elif choice == '4':
            break
                            


                

# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offer = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offer, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offer)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offer)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()

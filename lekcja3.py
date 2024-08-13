imiona = ["Arkadiusz","Wilola","Piotrek"]

imie = input("Podaj imię: ")
imie= imie.capitalize

if(imie in imiona):
    print("Masz dostęp do tajnych informacji")
else:
    print("Brak dostępu")
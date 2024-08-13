imiona = ["Piotrek", "Ola", "Arek", "Kuba", "Ania"]
liczby = [1,2,3,4]

print(len(imiona)) # długość tabeli

imiona.append("Tomasz") #doddaje nam do tabeli
print(imiona)

liczby.extend([5,6,7,]) #szybkie rozszerzenie listy
print(liczby)

liczby.insert(0,9) #Wsawiay do listy gdzie chcemy
print(liczby)

imiona.index("Ola") # szukamy elementu mozna to printować

liczby.sort(reverse=True) #sortuje
print(liczby)

print(max(liczby)) #najwieksza wartosc w liczbie
print(min(liczby)) #najmniejsza wawrtość w liczie

imiona.count("Piotrek") #liczy ile dany element razy jest w tablicy

imiona.pop() #usuwanie ostatniego elemetu
imiona.remove()#usuwa pierwszy element
imiona.clear()#usuwanie danch z listy
imiona.reverse() #odwrwaca liste od konca do przeodu
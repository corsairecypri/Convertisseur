
#Note : les cours de la bourse utilisés sont ceux qui étaient en vigueur durant la journée du 4 octobre 2021


print("Bonjour sur mon convertisseur de monnaie...")
print("Choisissez une devise...")


#Choix de la monnaie

monnaie = int(input("Euros = 1; Dollars US = 2; Livres Sterling = 3; Yens = 4 et Yuans = 5  : "))


if monnaie == 1:

	euros = int(input("Quel est le nombre d'euros à convertir ?  "))

    #Conversion des euros

	eurosDollars = euros * 1.16
	eurosLivres = euros * 0.85
	eurosYens = euros * 129.25
	eurosYuans = euros * 7.5

	print(f"{euros} euros vaut {eurosDollars} dollars US, {eurosLivres} livres sterlings, {eurosYens} yens et {eurosYuans} yuans")

	exit(0)

elif monnaie == 2:

    dollars = int(input("Quel est le nombre de dollars US à convertir ?  "))

	#Conversion des dollars

    dollarsEuros = dollars * 0.86
    dollarsLivres = dollars * 0.73
    dollarsYens = dollars * 111.20
    dollarsYuans = dollars * 6.45

    print(f"{dollars} dollars US vaut {dollarsEuros} euros, {dollarsLivres} livres sterlings, {dollarsYens} yens et {dollarsYuans} yuans")

    exit(0)

elif monnaie == 3:

	livres = int(input("Quel est le nombre de livres Sterling à convertir ?  "))

    #Conversion des livres sterling

	livresEuros = livres * 1.17
	livresDollars = livres * 1.36
	livresYens = livres * 151.45
	livresYuans = livres * 8.78

	print(f"{livres} livres Sterling vaut {livresEuros} euros, {livresDollars} dollars US, {livresYens} yens et {livresYuans} yuans")

	exit(0)

elif monnaie == 4:

	yens = int(input("Quel est le nombre de yens à convertir ?  "))

    #Conversion des yens

	yensEuros = yens * 0.0077
	yensDollars = yens * 0.0090
	yensLivres = yens * 0.0066
	yensYuans = yens * 0.058

	print(f"{yens} yens vaut {yensEuros} euros, {yensDollars} dollars US, {yensLivres} livres Sterling et {yensYuans} yuans")

	exit(0)

elif monnaie == 5:

	#Conversion des yuans

	yuans = int(input("Quel est le nombre de yuans à convertir ?  "))

	yuansEuros = yuans * 0.13
	yuansDollars = yuans * 0.16
	yuansLivres = yuans * 0.11
	yuansYens = yuans * 17.53

	print(f"{yuans} yuans vaut {yuansEuros} euros, {yuansDollars} dollars US, {yuansLivres} livres Sterling et {yuansYens} yens")

	exit(0)

else:

	print("ERREUR")
	exit(1)




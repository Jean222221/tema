# Împarte șirul în două părți egale.
text = "Un fragment cu scriere cuneiformă, vechi de 2.700 de ani, rescrie, istoria, relațiilor, dintre, Regatul? Iuda! și Imperiul Asirian"
mijloc = len(text) // 2
partea1 = text[:mijloc]
partea2 = text[mijloc:]
#Transformă toate literele în majuscule.
partea1 = partea1.upper()
#Elimină toate spațiile goale de la începutul și finalul șirului.
partea1 = partea1.strip()
#Pe a doua parte
#Inversează ordinea caracterelor.
partea2 = partea2[::-1]
#Transformă prima literă în majusculă.
partea2 = partea2.capitalize()
#Elimină toate caracterele de punctuație (., ,, !, ?) din această parte.
punctuatie = "?!,."
for char in punctuatie:
    partea2 = partea2.replace(char, "")
#Combină cele două părți și afișează rezultatul.
x = partea1 + partea2
print(x)
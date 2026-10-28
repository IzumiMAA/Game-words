import random

print ("Game Hangman")
print ("-"*15)
print ("Input 1 - Start Game")
print ("Input 2 - Leave Game")

StartOrLeave = int(input())
alphabet = ["А","Б","В","Г","Д","Е","Є","Ж","З","И","І","Й","К","Л","М","Н","О","П",
"Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ь","Ю","Я"]

words = [
    "шибениця", "програма", "пайтон", "компютер", "алфавіт", "скрипт",
    "інтернет", "ноутбук", "клавіатура", "монітор", "процесор", "сервер",
    "база", "пароль", "мережа", "код", "робот", "алгоритм", "екран",
    "ведмідь", "вовк", "лисиця", "заєць", "дельфін", "лелека", "сокіл",
    "дерево", "квітка", "сонце", "хмара", "океан", "річка", "озеро",
    "гора", "ліс", "пустеля", "планета", "зірка", "космос", "земля",
    "будинок", "кімната", "вікно", "двері", "стіл", "стілець", "диван",
    "кухня", "книга", "зошит", "ручка", "олівець", "телефон", "годинник",
    "дзеркало", "картина", "ключ", "замок", "світло", "тепло",
    "яблуко", "банан", "апельсин", "хліб", "молоко", "кава", "чай",
    "борщ", "вареник", "пиріг", "цукерка", "шоколад", "лимон", "сир",
    "машина", "автобус", "поїзд", "літак", "корабель", "метро", "вокзал",
    "вулиця", "місто", "село", "дорога", "міст", "парк", "театр",
    "життя", "радість", "усмішка", "дружба", "любов", "перемога", "мрія",
    "школа", "музика", "пісня", "спорт", "гра", "час", "робота"
]


slovo = random.choice(words)
kilkist = len(slovo)
i = int(kilkist)
a = int(kilkist)
listeri = list(slovo)
i2 = int(kilkist)
ckilkist = int(kilkist)

n = 1
vuk = 0

z = 0
if (StartOrLeave == 1):
	print ("Start Game")
	print ("="*10,"Generation word","="*10)
	print ("Alphabet Ukraine:")
	print (" ".join(alphabet))
	print ("!!!У вас є 8 СПРОБ щоб вгадати всі літери слова!!!")
	print (" "*10,"WORD"," "*10)
	print ("_"*kilkist)

	slovomasuv = [0]*a
	vukbykv = [0]*10000

	while slovomasuv != listeri:
		intf = 0
		i = ckilkist
		i = i-1
		z = i
		print ("Введіть літеру що в вас зараз на думці: ")
		bukva = input()
		if bukva in vukbykv:
			print ("Ви вже використовували цю літеру!!!")
			continue
		while i >= 0:
			if  slovo[i] == bukva:
				print ("Ви вгадали літеру",i+1,"=",bukva)
				b = a-(i+1)
				slovomasuv [i] = bukva
				vukbykv [vuk] = bukva
				i = i-1
			else:
				i = i - 1
				intf = intf + 1
				vukbykv [vuk] = bukva
			vuk = vuk+1

		slovores = " ".join("_" if x == 0 else str(x) for x in slovomasuv)
		print (slovores,"\n")

		if intf == ckilkist:
			match n:
				case 1:
					print ("	|	")
					print ("	|	")
					print ("	|	")
					print ("	|	")
					print ("        |       ")
				case 2:
					print ("   _____	")
					print ("	|	")
					print ("	|	")
					print ("	|	")
					print ("	|	")
					print ("        |       ")
				case 3:
					print ("   _____        ")
					print ("  |     |       ")
					print ("  O     |       ")
					print ("        |       ")
					print ("        |       ")
					print ("        |       ")
				case 4:
					print ("   _____        ")
					print ("  |     |       ")
					print ("  O     |       ")
					print ("  |     |       ")
					print ("        |       ")
					print ("        |       ")
				case 5:
					print ("   _____        ")
					print ("  |     |       ")
					print ("  O     |       ")
					print (" /|     |       ")
					print ("        |       ")
					print ("        |       ")
				case 6:
					print ("   _____        ")
					print ("  |     |       ")
					print ("  O     |       ")
					print (" /|]    |       ")
					print ("        |       ")
					print ("        |       ")
				case 7:
					print ("   _____        ")
					print ("  |     |       ")
					print ("  O     |       ")
					print (" /|]    |       ")
					print (" |      |       ")
					print ("        |       ")
				case 8:
					print ("   _____        ")
					print ("  |     |       ")
					print ("  O     |       ")
					print (" /|]    |       ")
					print (" | |    |       ")
					print ("        |       ")
					print ("П О Р А З К А =(")
					break

			n = n + 1
		else:
			print (" ")

	x = "".join(listeri)
	print ("Слово: ",x)


elif (StartOrLeave == 2):
	print ("Leave Game")
	exit()
else:
	print ("Error")
	exit()




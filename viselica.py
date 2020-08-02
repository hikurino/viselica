import random as ra

word_list = ["ПЕСНЯ", "СКАЗКА", "ПУШКА", "ГОНКА", "ВЕЩЬ", "СМОРОДИНА", "БИССЕКТРИСА", "ДОДЕКАЭДР", "ГОЛУБЬ"]

def get_word(word):
	return ra.choice(word)

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
	word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
	guessed = False                    # сигнальная метка
	guessed_letters = []               # список уже названных букв
	guessed_words = []                 # список уже названных слов
	tries = 6                          # количество попыток
	print("Го скатанем в Виселицу!")
	k = [i for i in word_completion]
	print(*k)
	while tries > 0 or guessed == True:
		x = input("Введи 1 букву КиРиЛлИцЫ").upper()
		if x == "STOP":
			print("Сайонара")
			break
		if x not in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ" or len(x) > 1:
			print("Я же ***** написал, 1 долбанную букву")
			continue
		if x in guessed_letters:
			print("Лол, тебя в детстве роняли? Ты уже писал эту букву!")
			continue
		if x in word and x not in guessed_letters:
			count = 0
			for i in word:
				if i == x:
					if count == len(word)-1:
						word_completion = word_completion[:count] + i
					elif count == 0:
						word_completion = i + word_completion[1:]
					else:
						word_completion = word_completion[:count] + i + word_completion[count+ 1:]
				count+= 1
			print(word_completion, "Красава, есть пробитие!")
			guessed_letters.append(x)
			if word_completion == word:
				print("Виннер, виннер, чикен динер! Умеешь, могешь!")
				guessed = True
				break
			continue
		
		if x not in word and x not in guessed_letters:
			tries -= 1
			print(display_hangman(tries))
			print("Опана, в молоко!", word_completion)	
		if tries == 0:
			print("Лох, это судьба! Пока на!")
y = ""
while y != "stop":
	print("В любой момент, если хочешь закончить это насилие, напиши 'stop'")
	y = input("Хочешь катануть?").upper()
	if y == "STOP" or y == "NO" or y == "НЕТ" or y == "stop":
		print("Чао Какао!")
		break
	else:
		play(get_word(word_list))
class RomanNumeralInterpreter:
    def __init__(self):
        # Словник, що відображає римські цифри у їх арабські еквіваленти
        self.roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def interpret(self, roman_numeral):
        # Ініціалізація змінних для обрахунку суми
        total = 0
        last_value = 0  # Значення попередньої цифри, початково 0
        # Проходження по римському числу у зворотньому порядку
        for numeral in reversed(roman_numeral):
            value = self.roman_numerals[numeral]  # Значення поточної цифри
            # Додавання або віднімання від суми в залежності від значень цифр
            if value < last_value:
                total -= value
            else:
                total += value
            last_value = value  # Оновлення попереднього значення
        return total

# Використання
interpreter = RomanNumeralInterpreter()
roman_numeral = 'XVI'
arabic_numeral = interpreter.interpret(roman_numeral)
# Виведення результату перетворення римського числа у арабському форматі
print(f'Римське число "{roman_numeral}" у арабському форматі: {arabic_numeral}')


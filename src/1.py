name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

# format()
output_format = "Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.".format(name, surname, age)
print(output_format)

# f-string
output_fstring = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
print(output_fstring)

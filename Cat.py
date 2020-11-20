from pet import Cat

cat1 = Cat("Барон", "Мальчик", "2 года")

print("Первого кота зовут ", cat1.getName())
print("Пол Барона ", cat1.getGender())
print("Возраст Барона = ", cat1.getAge())

print("---------")

cat2 = Cat("Сэм", "Мальчик", "2 года")

print("Второго кота зовут ", cat2.getName())
print("Пол Сэма ", cat2.getGender())
print("Возраст Сэма = ", cat2.getAge())
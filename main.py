# Импортируем функции из других модулей
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызываем обе функции с одинаковыми аргументами
result_fake = fake_divide(10, 0)
result_true = true_divide(10, 0)

# Выводим результаты
print("Результат деления через fake_math:", result_fake)
print("Результат деления через true_math:", result_true)



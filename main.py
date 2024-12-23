# module_4_1.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide


def main():
    try:
        result_fake = fake_divide(42, 0)
        print(f'Результат от fake_divide: {result_fake}')
    except Exception as e:
        print(f'Ошибка в fake_divide: {e}')

    try:
        result_true = true_divide(42, 0)
        print(f'Результат от true_divide: {result_true}')
    except Exception as e:
        print(f'Ошибка в true_divide: {e}')


if __name__ == "__main__":
    main()




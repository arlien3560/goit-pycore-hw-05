import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, який ідентифікує та повертає всі дійсні числа з тексту.
    Дійсні числа повинні бути чітко відокремлені пробілами з обох боків.

    Args:
        text: Рядок тексту для аналізу
    Yields:
        float: Дійсні числа, знайдені в тексті
    """
    pattern = r'(?:^| )(\d+(?:\.\d+)?)(?= |$)'
    matches = re.finditer(pattern, text)

    for match in matches:
        yield float(match.group(1))


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]):
    """
    Обчислює загальну суму всіх дійсних чисел в тексті.

    Args:
        text: Рядок тексту для аналізу
        func: Функція-генератор для отримання чисел з тексту

    Returns:
        float: Загальна сума всіх чисел
    """
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох " \
        "частин: 1000.01 як основний дохід, доповнений додатковими " \
        "надходженнями 27.45 і 324.00 доларів."

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

    print("\n--- Додаткові тести ---")

    # Тест 1: Число на початку рядка (НЕ повинно враховуватись)
    text1 = "100 гривень отримано"
    print(f"Тест 1 (число на початку): {sum_profit(text1, generator_numbers)}")

    # Тест 2: Число в кінці рядка (НЕ повинно враховуватись)
    text2 = "Отримано 200"
    print(f"Тест 2 (число в кінці): {sum_profit(text2, generator_numbers)}")

    # Тест 3: Числа відокремлені пробілами з обох боків
    text3 = "Надходження: 1500 та 250.50 та ще 100.00 гривень"
    print(f"Тест 3 (правильні числа): {sum_profit(text3, generator_numbers)}")

    # Тест 4: Змішаний тест
    text4 = "123 початок, середина 456 та 78.9 кінець, і ще 10.5 тут"
    print(f"Тест 4 (змішаний): {sum_profit(text4, generator_numbers)}")

    # Демонстрація роботи генератора
    print("\n--- Демонстрація генератора ---")
    text5 = "Значення: 10.5 та 20 та 30.75 результат"
    print(f"Текст: '{text5}'")
    print("Числа, знайдені генератором:")
    for number in generator_numbers(text5):
        print(f"  {number}")

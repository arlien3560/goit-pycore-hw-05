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
    pattern = r'\b\d+\.\d+\b|\b\d+\b'
    matches = re.finditer(pattern, text)
    
    for match in matches:
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму всіх дійсних чисел в тексті.
    
    Args:
        text: Рядок тексту для аналізу
        func: Функція-генератор для отримання чисел з тексту
        
    Returns:
        float: Загальна сума всіх чисел
    """
    # Використовуємо генератор для отримання всіх чисел та підсумовуємо їх
    return sum(func(text))


# Приклад використання:
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    
    # Додаткові тести
    print("\n--- Додаткові тести ---")
    
    # Тест 1: Тільки цілі числа
    text1 = "Продано товарів на суму 100 200 300 гривень."
    print(f"Тест 1: {sum_profit(text1, generator_numbers)}")  # 600.0
    
    # Тест 2: Тільки дробові числа
    text2 = "Ціни: 10.50 20.75 30.25"
    print(f"Тест 2: {sum_profit(text2, generator_numbers)}")  # 61.5
    
    # Тест 3: Змішані числа
    text3 = "Надходження: 1500 та 250.50 та ще 100.00"
    print(f"Тест 3: {sum_profit(text3, generator_numbers)}")  # 1850.5
    
    # Тест 4: Порожній текст
    text4 = "Немає чисел в цьому тексті"
    print(f"Тест 4: {sum_profit(text4, generator_numbers)}")  # 0.0
    
    # Тест 5: Демонстрація роботи генератора
    print("\n--- Демонстрація генератора ---")
    text5 = "Числа: 10.5 20 30.75 40"
    print("Числа, знайдені генератором:")
    for number in generator_numbers(text5):
        print(f"  {number}")
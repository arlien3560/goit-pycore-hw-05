import sys
from typing import Dict, List
from pathlib import Path


def parse_log_line(line: str) -> Dict[str, str]:
    try:
        # Розділяємо рядок на частини
        parts = line.strip().split(' ', 3)

        if len(parts) >= 4:
            return {
                'date': parts[0],
                'time': parts[1],
                'level': parts[2],
                'message': parts[3]
            }
        else:
            # Якщо формат неправильний, повертаємо порожній словник
            return {}
    except Exception as e:
        print(f"Помилка при парсингу рядка: {line}. Помилка: {e}")
        return {}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []

    try:
        # Перевіряємо, чи існує файл
        if not Path(file_path).exists():
            print(f"Помилка: Файл '{file_path}' не знайдено.")
            return logs

        # Читаємо файл та парсимо кожен рядок
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Пропускаємо порожні рядки
                if line.strip():
                    parsed_line = parse_log_line(line)
                    if parsed_line:  # Додаємо тільки коректно розпарсені рядки
                        logs.append(parsed_line)

        return logs

    except PermissionError:
        print(f"Помилка: Недостатньо прав для читання файлу '{file_path}'.")
        return logs
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str):
    filtered = filter(
        lambda log: log.get('level', '').upper() == level.upper(),
        logs
        )
    return list(filtered)


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня логування.
    Args: logs: Список логів
    Returns: dict: Словник з кількістю записів для кожного рівня
    """
    counts = {}

    for log in logs:
        level = log.get('level', 'UNKNOWN')
        counts[level] = counts.get(level, 0) + 1

    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """Виводить статистику логів у вигляді таблиці.
    Args:
        counts: Словник з кількістю записів для кожного рівня
    """
    print("\nРівень логування | Кількість")
    print("-----------------|----------")

    for level in sorted(counts.keys()):
        print(f"{level:<16} | {counts[level]}")


def display_filtered_logs(logs: List[Dict[str, str]], level: str) -> None:
    """
    Виводить деталі логів для певного рівня.
    Args:
        logs: Список відфільтрованих логів
        level: Рівень логування
    """
    print(f"\nДеталі логів для рівня '{level.upper()}':")

    if not logs:
        print(f"Записів з рівнем '{level.upper()}' не знайдено.")
        return

    for log in logs:
        # Виводимо у форматі: дата час - повідомлення
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    """
    Головна функція скрипту.
    """
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) < 2:
        print("Використання:python main.py <шлях_до_файлу> [рівень_логування]")
        print("Приклад: python main.py logfile.log")
        print("Приклад з фільтром: python main.py logfile.log error")
        sys.exit(1)

    # Отримуємо шлях до файлу
    file_path = sys.argv[1]

    # Отримуємо рівень логування (якщо вказаний)
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    # Завантажуємо логи
    print(f"Завантаження логів з файлу: {file_path}")
    logs = load_logs(file_path)

    if not logs:
        print("Логи не завантажено або файл порожній.")
        sys.exit(1)

    # Підраховуємо кількість записів за рівнями
    counts = count_logs_by_level(logs)

    # Виводимо загальну статистику
    display_log_counts(counts)

    # Якщо вказано рівень логування, виводимо детальну інформацію
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        display_filtered_logs(filtered_logs, log_level)


if __name__ == "__main__":
    raise SystemExit(main())

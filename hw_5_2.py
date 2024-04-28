import re
from typing import Callable

text = """Загальний дохід працівника складається з декількох частин:
1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів.
"""

def generator_numbers(text:str):
    '''Генератор який ітерує по всім дійсним числам у тексті'''
    # Використання регулярних виразів для ідентифікації дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    matches = re.findall(pattern, text)
    
    # Створення генератора з ітераціею по всіх дійсних числах у тексті 
    for match in matches:
        yield float(match)
    
def summ_profit(text:str, func: Callable) -> float:
    '''Обчислює загальну суму чисел утворених генератором''' 
    return sum(func(text))

# приклад використання
total_profit = summ_profit(text, generator_numbers) 
print(f'Загальний дохід: {total_profit: .2f}') 

# calculator.py
def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b

def main():
    print("Добро пожаловать в калькулятор!")
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        result = add(num1, num2)
        print(f"Результат сложения: {result}")
        
    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа!")

if __name__ == "__main__":
    main()

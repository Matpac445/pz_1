# test_calculator.py
import calculator

def test_addition():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    print("Все тесты сложения прошли успешно!")

if __name__ == "__main__":
    test_addition()

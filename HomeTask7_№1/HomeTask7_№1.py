def calculate_bmi(weight, height):
    try:
        bmi = weight / (height / 100) ** 2
        return bmi
    except ZeroDivisionError:
        raise ValueError("Рост не может быть равен нулю.")
    except Exception as e:
        raise ValueError(f"Ошибка при расчете ИМТ: {e}")


def interpret_bmi(bmi):
    if 18.5 <= bmi < 25:
        return "Нормальный вес"
    elif 25 <= bmi < 30:
        return "Избыточный вес (предожирение)"
    elif bmi >= 30:
        return "Ожирение"
    else:
        return "Недостаточный вес"


try:
    weight = float(input("Введите вес в килограммах: "))
    height = float(input("Введите рост в сантиметрах: "))

    if weight <= 0 or height <= 0:
        raise ValueError("Вес и рост должны быть положительными числами.")

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"Индекс массы тела (ИМТ): {bmi:.2f}")
    print(f"Оценка: {interpretation}")
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
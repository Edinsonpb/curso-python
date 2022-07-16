from pickle import FALSE


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % 1 == 0:
            divisors.append(i)
    return divisors

# def run():
#     try:
#         num = int(input("Ingresa un numero: "))
#         print(divisors(num))
#         print("terminó mi programa")
#     except ValueError:
#         print("Debes ingresar un numero")

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("terminó mi programa")
        
        if num < 0:
            raise ValueError("No se permiten numeros negativos")
        return num
    except ValueError as nn:
        print(nn)
        return FALSE



if __name__ == '__main__':
    run()
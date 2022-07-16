def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % 1 == 0:
            divisors.append(i)
    return divisors

def run():
        num = int(input("Ingresa un numero: "))
        assert num > 0, "Debes ingresar un numero positivo"
        print(divisors(num))
        print("terminó mi programa")

if __name__ == '__main__':
    run()
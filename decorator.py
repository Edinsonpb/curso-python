from unittest import result


PASSWORD = "12345"

def password_requiered(func):
    def wrapper():
        password = input("cual es tu contraseña? ")

        if password == PASSWORD:
            return func()
        else:
            print("La contraseña no es correcta ")

    return wrapper

@password_requiered
def needs_password():
    print("La contraseña es correcta")


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    return "Hola, {}".format(name)


if __name__ == '__main__':
#    needs_password()
    print(say_my_name("David"))

#    say_my_name()
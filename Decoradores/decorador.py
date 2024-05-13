from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la funcion")
        result = func(*args, **kwargs)
        print("Despues de llamar a la funcion")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Funcion para saludar a alguine"""
    return(f"Hola {name}!").upper()

# Llama a la funcion decorada
print(greet("Fabricio"))

# Accede a los metadatos de la funcion original
print(greet.__name__)

# Ouput: greet
print(greet.__doc__)

# Ouput: funcion para saludar a alguien

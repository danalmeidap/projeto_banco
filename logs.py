from datetime import datetime
import functools


def log_operação(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        agora = datetime.now()
        data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Operação de {func.__name__} iniciada em {data_hora_formatada}")
        resultado = func(*args, **kwargs)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"{data_hora_formatada} - {func.__name__} executada\n")
        print(f"Operação de {func.__name__} finalizada em {data_hora_formatada}")
        return resultado

    return wrapper

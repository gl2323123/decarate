import os
from datetime import datetime




def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('myfunc.log', 'a', encoding= 'utf-8') as f:
            f.write( f'Запуск функции: {old_function.__name__}\n'
                        f'Дата запуска функции {old_function.__name__}: {datetime.now()}\n'
                        f'Aргументы функции {old_function.__name__}: {args,kwargs}\n'
                        f'Результат функции {old_function.__name__}: {result}\n')
        return result
    return new_function

path = 'generate.log'
if os.path.exists(path):
    os.remove(path)

@logger
def get_employees(a,b):
    print(f'Работало сотрудников в этом месяце: {a} до {b}')
    return a + b



if __name__ == '__main__':
    get_employees(3,6)
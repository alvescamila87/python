#args + kwargs

def teste_args_kwargs(arg1, arg2, arg3):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)

args = ('um', 2, 3)
teste_args_kwargs(*args)

kwargs = {'arg1': 'um', 'arg2': 2, 'arg3': 'três'}
teste_args_kwargs(**kwargs)
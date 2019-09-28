# args* and kwargs** support multiple parameter function Übergabe

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = (2,3,"5")
test_args_kwargs(*args)

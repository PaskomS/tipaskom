from contextlib import ContextDecorator
import time


a=1

def n_dec(func):
    print("1")

    def exec():
        print("2")
        func()
        print("3")
    return exec


@n_dec
def add():
    print("444")


add()


a=1
pass

class mycontext(ContextDecorator):
    def __init__(self, kto):
        self.kto = kto
        #print("1111 init")
        a=1

    def __enter__(self):
        print('4444  Starting после with self')

    def __exit__(self, *exc):
        print('666  Finishing')

    def __call__(self, func):

        #print("22222 call")

        def xdcfgxdhf():
            print("333 тут вызов когда реально функция, со значениями xdc")

            with self:
                print("555  внутри xdc with self")
                return func()

        return xdcfgxdhf

a=1


@mycontext("запрос в истор")
def function(param):
    fff = param/0
    print("САМА функ", param)



class Greeter(ContextDecorator):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Hello {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"See you later, {self.name}")




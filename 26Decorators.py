def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this fumction")

    return mfx


@greet
def Hello():
    print("Hello World")

def add(a, b):
    print(a+b)

Hello()






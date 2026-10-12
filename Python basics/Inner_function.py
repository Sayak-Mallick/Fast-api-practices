def outer():
    print("Im outer")

    def inner(num):
        print(f"Im inner {num}")

    return inner

something = outer()
something(5)
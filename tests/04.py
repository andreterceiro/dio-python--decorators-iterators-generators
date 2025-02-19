def test(*args, **kwargs):
    print("printing args")
    for parameter in args:
        print(parameter)

    print("\nprinting kwargs")
    for key, parameter in kwargs.items():
        print(f"{key}: {parameter}")

test(1, "a", True, cassio=1, fagner=2, garro=10)

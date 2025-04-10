import rspx


def main():
    print(f"rs module: {rspx.__all__}")
    print(f"rs doc: {rspx.__doc__}")
    print(f"rust sum: {rspx.sum(1, 1)}")
    print(f"rust fib: {rspx.fib(10)}")


if __name__ == "__main__":
    main()

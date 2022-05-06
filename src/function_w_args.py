import sys


def get_name(name, age):
    print(name + ":" + age)


if __name__ == "__main__":
    get_name(sys.argv[1], sys.argv[2])

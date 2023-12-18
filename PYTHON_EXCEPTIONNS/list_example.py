#!/usr/bin/python3
List = [1, 2, 3]


if __name__ == '__main__':
    try:
        print("{}".format(Lst[3]))
    except IndexError as Ind:
        print(Ind)
    except NameError as Err:
        print(Err)

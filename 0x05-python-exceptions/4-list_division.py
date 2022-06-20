#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        result = [i / j for i, j in zip(my_list_1, my_list_2)]
    except ZeroDivisionError:
        print("division by 0")
    except ValueError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return result
    print("")

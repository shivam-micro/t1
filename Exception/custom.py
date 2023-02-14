class ValueNotInRangeError(Exception):
        message = "value not in range(15,20)"

a = int(input("enter the number: "))
if not 15 < a < 20:
        raise ValueNotInRangeError(a)




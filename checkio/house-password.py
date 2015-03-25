# import re


def checkio(data):
    digit = False
    lower = False
    upper = False

    if len(data) >= 10:
        for d in data:
            if str.isdigit(d):
                digit = True

            if str.islower(d):
                lower = True

            if str.isupper(d):
                upper = True

    if digit == True and lower == True and upper == True:
        return True
    else:
        return False

#Python string has several useful methods -- str.isdigit(c), str.islower(c) and str.isupper(c

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

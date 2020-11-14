arr1 = [1,2,3,4,5,6,7,8,9]
arr1 = [11,12,13,14,15,16,17,18,19]
arr1 = [31,32,33,34,35,36,37,38,39]

def printer_plus_1(arr):
def printer_minus_1(arr):
def printer_mult_1(arr):
    for i in arr:
        print(i - 1)
        print(i + 1)
        print(i * 1)
    return True

if __name__ == "__main__":
    printer_minus1(arr1)
    printer_plus_1(arr1)
    printer_mult_1(arr1)
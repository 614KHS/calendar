input_count=input('好きな数を入れてね:')
count = int(input_count)

while True:
    if count >= 1900 and count <= 1911:
        print("明治" + str(33+count-1900) + "年です")
        break
    elif count == 1912:
        print("大正元年です")
        break
    elif count >= 1913 and count <= 1925:
        print("大正" + str(1+count-1912) + "年です")
        break
    elif count == 1926:
        print("昭和元年です")
        break
    elif count >= 1927 and count <= 1988:
        print("昭和" + str(1+count-1926) + "年です")
        break
    elif count == 1989:
        print("平成元年です")
        break
    elif count >= 1990 and count <= 2018:
        print("平成" + str(1+count-1989) + "年です")
        break
    elif count == 2019:
        print("令和元年です")
        break
    elif count >= 2020 and count <= 2050:
        print("令和" + str(1+count-2019) + "年です")
        break
    else:
        input_count = input('好きな数を入れてね:')
        count = int(input_count)
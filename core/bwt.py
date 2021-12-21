def encode(string):
    print("* Start BWT encoding, input:")
    print(string)
    # chèn ký tự đánh dấu ($) vào cuối và chuyển chuỗi thành mảng các ký tự
    str_list = list(string + "$")

    # xoay vị trí các ký tự trong mảng => thu được mảng 2 chiều với mỗi dòng là 1 mảng xoay của chuỗi ban đầu
    cyclic_suffix_array = get_cyclic_suffix_array(str_list)

    # sắp xếp lại các mảng ký tự theo thứ tự từ điển
    sorted_suffix_array = sorted(cyclic_suffix_array)

    # lấy ký tự cuối cùng của mảng con của mảng đã sắp xếp
    transform = []
    for i in sorted_suffix_array:
        transform.append(i[-1])

    # chuỗi mã hóa sử dụng BWT
    encoded = ''.join(transform)
    print("* Encoded string:")
    print(encoded)

    return encoded


def decode(encoded_string):
    print("* Start BWT decoding, input:")
    print(encoded_string)

    # chiều dài chuỗi
    n = len(encoded_string)

    table = [[]] * n

    # tái tạo lại mảng 2 chiều chứa các mảng xoay của chuỗi ban đầu
    for x in range(n):
        # mỗi lần lặp sẽ chèn 1 ký tự vào mỗi cột
        for y in range(n):
            table[y] = list(encoded_string[y]) + table[y]

        # sắp xếp lại mảng 2 chiều theo thứ tự từ điển đối với mỗi dòng
        table = sorted(table)

    # tìm mảng có ký tự cuối cùng là kỳ tự đánh dấu ($)
    i = 0
    for row in table:
        if row[-1] == "$":
            i = table.index(row)
            break

    # nối các ký tự trong mảng lại và bỏ đi ký tự đánh dấu
    decoded = ''.join(table[i][:-1])

    print("* Decoded string:")
    print(decoded)

    return decoded


def get_cyclic_suffix_array(str_list):
    cyclic_suffix_array = []
    str_len = len(str_list)
    for i in range(str_len):
        cyclic_suffix_array.append(str_list[(str_len - i):] + str_list[:(str_len - i)])
    return cyclic_suffix_array


def encode_file(infile, outfile):
    fi = open(infile, "r").read()
    encoded = encode(fi)
    fo = open(outfile, "w")
    fo.write(encoded)
    fo.close()


def decode_file(infile, outfile):
    print(infile)
    fi = open(infile, "r").read()
    fo = open(outfile, "w")
    fo.write(decode(fi))
    fo.close()


# encode_file("../tests/test.txt", "../tests/test.txt.bwt")
# decode_file("../tests/test.txt.bwt", "../tests/test.txt.decoded")

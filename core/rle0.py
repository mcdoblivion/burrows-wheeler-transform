def encode(input_array):
    output_array = []

    # duyệt mảng và thay thế chuỗi lặp 0 bằng [0, số lần lặp], ví dụ: 0, 0, 0 => 0, 3
    for index, number in enumerate(input_array):
        if number == 0:
            last_number = input_array[index - 1]
            if last_number != 0:
                output_array.append(0)
                output_array.append(1)
            else:
                count = output_array.pop()
                output_array.append(count + 1)
        else:
            output_array.append(number)

    print(f"* RLE0 encode output:\n{output_array}\n")
    return output_array


def decode(input_array):
    output_array = []

    # duyệt mảng và thay thế [0, số lần lặp] bằng số phần tử 0 tương ứng, ví dụ: 0, 3 => 0, 0, 0
    for index, number in enumerate(input_array):
        if number == 0:
            loop_count = input_array[index + 1]
            for i in range(loop_count):
                output_array.append(0)
        elif input_array[index - 1] != 0:
            output_array.append(number)

    print(f"* RLE0 decode output:\n{output_array}\n")
    return output_array


# encode([97, 110, 0, 0, 0, 99, 0, 2, 39, 1, 0, 0, 0])
# decode([97, 110, 0, 3, 99, 0, 1, 2, 39, 1, 0, 3])

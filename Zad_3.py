"""
напишите функцию, которая открывает на чтение созданные файлы с числами и именами.
Перемножьте пары чисел. в новый файл сохраните имя и произведение.
если рез-т усножение отриц. - сохраните имя записанное строчными и произедением по модулю
если положительный - о сохраните прописными и произведением округленным до целого
в результирубщем файле должно быть столько же строк, сколько в длинном файле
При достижении конца более короткого файла,
возвращайтесь в его начало
"""


def read_line_or_begin(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def process_files(file_numbers, file_names, file_res):
    with open(file_numbers, 'r', encoding='utf-8') as f_num:
        with open(file_names, 'r', encoding='utf-8') as f_names:
            with open(file_res, 'w', encoding='utf-8') as f_res:
                lenght1 = len(f_num.readlines())
                lenght2 = len(f_num.readlines())
                lenght = max(lenght1, lenght2)
                for i in range(lenght):
                    line_num = read_line_or_begin(f_num)
                    line_name = read_line_or_begin(f_names)
                    a, b = line_num.split('|')
                    a = int(a)
                    b = float(b)
                    res = a*b
                    if res < 0:
                        res *= -1
                        line_name = line_name.lower()
                    else:
                        res = round(res)
                        line_name = line_name.upper()
                    f_res.write(f'{line_name} {res}')
                    f_res.write('\n' if i < lenght - 1 else '')


if __name__=='__main__':
    process_files('data.txt', 'data_names.txt', 'res.txt')
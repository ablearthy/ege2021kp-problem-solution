"""
(Б.С. Михлин) В текстовом файле k7-m5.txt находится цепочка из прописных (заглавных) символов латинского алфавита A, B,
C. В исходной цепочке замените все найденные C-подцепочки на подцепочки, содержащие длину текущей С-подцепочки с
последующей текущей C-подцепочкой с замененными символами «С» большими на «с» маленькие.
В ответе в трех строчках выведите:
    1) количество C-подцепочек;
    2) левые 15 символов, пробел и правые 15 символов исходной цепочки;
    3) левые 15 символов, пробел и правые 15 символов преобразованной цепочки.
"""
import re
from typing import NamedTuple


class Result(NamedTuple):
    total: int
    original: str
    modified: str

    def __str__(self):
        return "\n".join(map(str, [self.total, self.original, self.modified]))


def modify(s):
    return f"{s.end() - s.start()}{s[0].lower()}"


def fmt_str(s):
    return f"{s[:15]} {s[-15:]}"


def solve(s: str):
    pattern = re.compile("C*C")
    total = len(re.findall(pattern, s))
    modified = re.sub(pattern, modify, s)

    return Result(total=total, original=fmt_str(s), modified=fmt_str(modified))

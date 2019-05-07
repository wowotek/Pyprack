import itertools
import hashlib
import numpy as np
from multiprocessing import Pool

class charset:
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    TOKENS = "~`!@#$%^&*()_+-={}[]:\";'<>?,./|\\ "
    NUMERIC = "0123456789"


def hash_literal(param):
    return "".join(param), hashlib.sha1(bytes("".join(param), "utf-8")).hexdigest()

def get_hash(length: int, charset=charset.LOWERCASE + charset.NUMERIC, length_type="Fixed"):
        if length_type.lower() == "fixed":
            with Pool(8) as worker:
                return np.array(worker.map(hash_literal, itertools.product(charset, repeat=length)))
        elif length_type.lower() == "iterate":
            with Pool(16) as worker:
                hash_list = []
                for i in range(1, length+1):
                    hash_list.append(np.array(worker.map(hash_literal, itertools.product(charset, repeat=i))))
                
                return np.array(hash_list)


def compare(data: list):
    if len(data.shape) == 1:
        for i in data:
            for j in i:
                print(j)
    if len(data.shape) > 1:
        for i in data:
            print(i)


if __name__ == "__main__":
    compare(get_hash(4, length_type="fixed"))
    

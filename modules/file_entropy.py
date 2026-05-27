import math

def check_entropy(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    if not data: return 0
    entropy = 0
    for i in range(256):
        p_x = float(data.count(i)) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy 
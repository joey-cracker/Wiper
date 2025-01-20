from argparse import ArgumentParser
import random

parser = ArgumentParser()
parser.add_argument('-d', '--device', required=True)
parser.add_argument('-b', '--block_size', default='512B')
args = parser.parse_args()
device = args.device
block_size = args.block_size
size = int(block_size[:-1])
#assert block_size[-1].isalpha()
unit = block_size[-1].upper()
assert unit in ['B', 'K', 'M']
multiplier = size if unit=='B' else (1024 * size if unit=='K' else 1024**2 * size)
num_bytes = 0

with open(device, 'wb') as f:
    while True:
        data = random.choices(range(2**8), k=multiplier)
        try:
            diff = f.write(bytes(data))
            if diff == 0:
                break
            num_bytes += diff
        except OSError:
            break
        giga_num = num_bytes // 1024**3
        rem = num_bytes % (1024**3)
        mega_num = rem // 1024**2
        rem = rem % (1024 ** 2)
        kilo_num = rem // 1024
        rem = rem % 1024
        print(f'{giga_num:4d} GiB, {mega_num:4d} MiB, {kilo_num: 4d} KiB and {rem:4d} bytes written.', end='\r')

print()

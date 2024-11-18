import multiprocessing
import time
import threading
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    file_ = open(name, 'r')
    while True:
        i = file_.readline()
        if not i: break
        all_data.append(i)






filenames = [f'./file {number}.txt' for number in range(1, 5)]
# # Линейный вызов
start_ = datetime.now()
for i in filenames:
    read_info(i)
end_ = datetime.now()
print(end_ - start_)

# Многопроцессный

# if __name__ == '__main__':
#     with Pool(4) as p:
#         start_ = datetime.now()
#         p.map(read_info, filenames)
#         end_ = datetime.now()
#         print(end_ - start_)


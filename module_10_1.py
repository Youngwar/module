from threading import Thread
from time import sleep
from datetime import datetime
def write_words(word_count, file_name):

    i = 1.
    file_ = open(file_name, 'a', encoding='UTF-8')
    for j in range (1, (word_count + 1)):
        file_.write(f'Какое-то слово № {j}\n')
        sleep(0.1)
        i += 1
    file_.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()
time_ = time_stop - time_start
print(time_)


the_first = Thread(target = write_words, args = (10, 'example5.txt'))
the_second = Thread(target = write_words, args = (30, 'example6.txt'))
the_third = Thread(target = write_words, args = (200, 'example7.txt'))
the_fourth = Thread(target = write_words, args = (100, 'example8.txt'))

time_start = datetime.now()

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()

time_stop = datetime.now()
time_ = time_stop - time_start
print(time_)





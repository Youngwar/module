import time

class User:
    def __init__(self, nickname,  password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

    # def __str__(self):
    #     return f'{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}'



class UrTube():
    current_user = None
    def __init__(self):

        self.users = {}
        self.videos = {}



    def add (self, *video):
        for i in video:
            if i.title not in self.videos:
                self.videos[i.title] = i.duration, i.time_now, i.adult_mode
                #print(self.videos)

    def get_videos(self, name):
        list_ = []
        for i in self.videos.keys():

            if str.lower(name) in str.lower(i):
                list_.append(i)
        return list_

    def log_in(self, nickname, password):
        if nickname in self.users:
            p = self.users[nickname]
            if hash(password) == p[0]:
                self.current_user = nickname

    def register(self, nickname,  password, age):
        if __name__ == '__main__':

            user = User(nickname,  password, int(age))
            if nickname not in self.users.keys():
                self.users[user.nickname] = (user.password, user.age)
                #print(self.users)
                self.current_user = user.nickname
            else: print(f'Пользователь {nickname} уже существует')
            #print(self.users)

    def log_out(self):
        self.current_user = None

    def watch_video(self, title):
        if self.current_user != None:
            #print(self.current_user)

            if title in self.videos:
                v = self.videos[title]

                for current_user in self.users:
                    i = self.users.get(self.current_user)
                    k = v[2]
                    #print(i, k)
                    if i[1] < 18 and k == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')

                    else:
                        i = 0
                        while i < v[0]:
                            time.sleep(1)
                            i += 1
                            print('\r', i, end = '')
                        print('\n', 'Конец видео')
                        break



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)


v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
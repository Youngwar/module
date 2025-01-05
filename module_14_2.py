import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Users('
               'id INTEGER PRIMARY KEY,'
               'username TEXT NOT NULL,'
               'email TEXT NOT NULL,'
               'age INTEGER,'
               'balance INTEGER NOT NULL)')
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}', ))
cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))
cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()
# print(count)

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()
# print(total_balance)

print(total_balance[0]/count[0])

cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()
print(avg_balance[0])

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
for user in users:
    print(user)
connection.commit()
connection.close()
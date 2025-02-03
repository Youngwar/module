from fastapi import FastAPI, Path, HTTPException
from typing import Annotated





app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admin_page():
    return {"message": 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def get_user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example= 1)]):
    return {"message": f'Вы вошли как пользователь № {user_id}'}


@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username", example= 'UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= '24')]):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст {age}"}

users = []
@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username", example= 'UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= '24')]):
    user_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {'id': user_id, 'username': username, "age": age}
    users.append(new_user)

    return {'message': f'User {user_id} is registered'}


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username", example= 'UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= '24')]):
    for user in users:
        if user["id"] == user_id:
            user["username"] = username
            user['age'] = age
            return {'message': f'User {user_id} has been updated'}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="User ID", example= '1')]):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {'message': f"Пользователь {user_id} удален"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

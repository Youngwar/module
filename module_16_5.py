from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# @app.get("/user/admin")
# async def get_admin_page():
#     return {"message": 'Вы вошли как администратор'}

@app.get(path="/user/{id}", response_class=HTMLResponse)
async def get_user(request: Request, id: int):
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# @app.get("/user/{username}/{age}")
# async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username", example= 'UrbanUser')],
#                         age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= '24')]):
#     return {'message': f"Информация о пользователе. Имя: {username}, Возраст {age}"}


@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username", example= 'UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= '24')]):
    user_id = max(user["id"] for user in users) + 1 if users else 1
    User = {'id': user_id, 'username': username, "age": age}
    users.append(User)

    return User


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9_-]+$", description="Enter username", example= 'UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= '24')]):
    for user in users:
        if user["id"] == user_id:
            user["username"] = username
            user['age'] = age
            return {'message': f'User {user_id} has been updated'}
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="User ID", example= '1')]):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {'message': f"Пользователь {user_id} удален"}
    raise HTTPException(status_code=404, detail="User was not found")

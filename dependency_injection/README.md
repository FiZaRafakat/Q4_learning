# FastAPI Dependency Injection Example 📚

This repository demonstrates how to use **Dependency Injection** in **FastAPI**. Dependency Injection helps us organize code in a clean and reusable way, making our APIs more maintainable. 

We’ll go over **Path Parameters**, **Query Parameters**, **Multiple Dependencies**, and a **Comprehensive Example** using classes and object dependencies.

## 1. Imports and Dependencies 📥

```python
from fastapi import FastAPI, Depends, Query
from typing import Annotated
```
- **FastAPI:** The main FastAPI class to create the app and define routes.
- **Depends:** This is the core of Dependency Injection in FastAPI. It allows you to inject dependencies into your path operations.
- **Query:** Used for query parameters in FastAPI to capture values from the URL.
- **Annotated:** Helps you to specify the type of dependencies in FastAPI.

## 2. Dependency Injection Basics ⚙️

### What is Dependency Injection?

Dependency Injection is a design pattern where you inject a function or object that another function or class depends on. Instead of manually creating instances, FastAPI manages and provides dependencies automatically. This reduces code repetition and improves maintainability.

## 3. Path Parameter Dependency Example 🚀

```def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response
```
- `Path Parameter Dependency:` Here, we define a dependency function get_goal that takes a username and returns a goal message.
- `Depends(get_goal):` We use Depends to automatically pass the result of get_goal as the response parameter in the get_my_goal endpoint.

**Explanation:**
 
 When the client hits /get-goal, FastAPI will inject the result of get_goal into the response variable. This allows us to reuse the logic of fetching goals easily without repeating it in the route itself.

## 4. Query Parameter Dependency Example 🔑

```
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user
```
- `Query Parameter Dependency:` The dep_login function checks the username and password query parameters from the URL.
- `Depends(dep_login):` Here, FastAPI automatically calls dep_login with query parameters and injects the returned value into the user variable in the login_api route.

**Explanation:**

This endpoint expects the user to send username and password as query parameters, and then we check if they match specific values ("admin" in this case). The dependency function handles the logic of authentication, so we don't need to repeat it in each endpoint.

## 5. Using Multiple Dependencies 🔄


### Without Dependency Injection:

```
@app.get("/main/{num}")
def get_main(num: int):
    num1 = depfunc1(num)
    num2 = depfunc2(num)
    total = num + num1 + num2
    return f"Pakistan {total}"
```

### With Dependency Injection:

```
@app.get("/main_dependency/{num}")
def get_main(num: int, num1: Annotated[int, Depends(depfunc1)], num2: Annotated[int, Depends(depfunc2)]):
    total = num + num1 + num2
    return f"Pakistan {total}"
```
**Multiple Dependency Functions:**
- `depfunc1 and depfunc2` are two functions that perform simple arithmetic on a number.
- In the second example, we inject these functions using Depends(depfunc1) and Depends(depfunc2), letting FastAPI manage them.

**Explanation:**

In the `non-injection` version, we manually call depfunc1 and depfunc2 inside the route.

In the `dependency-injection` version, FastAPI automatically injects the results of these functions, making the code more modular and reusable.

## 6. Comprehensive Example with Classes and Dependency Injection 🏗️

In this example, we use classes to handle dependencies, which can be useful when you need to share state or perform more complex logic.
Blog Dependency Example:
```
class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj
```
### Class-Based Dependency Injection:
- `GetObjectOr404` is a class that fetches an object by ID from a model (either blogs or users).
- If the object is not found, it raises a 404 error.

**Explanation:**

Using classes for dependencies is helpful when you need to encapsulate complex logic or shared state. In this example, the GetObjectOr404 class manages fetching data and handling errors in a centralized manner, which we can reuse in multiple places.

## 7. Handling User and Blog Dependency Example 👥
```
blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

# ******

user_dependency = GetObjectOr404(users)

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name
```
- `Blog Dependency :` We create a blog_dependency for fetching blog details by the ID from a users dictionary.

- `User Dependency :` Similar to the blog example, we create a dependency for fetching user details by ID from a users dictionary.

- `Depends(user_dependency):` FastAPI will automatically inject the result of the user_dependency when the endpoint is called.

**Explanation:**

By using dependency injection, we avoid repeating the logic of fetching a user and handling 404 errors in every endpoint. Instead, we define it once in a reusable class and inject it where needed.

# Conclusion 🎉
- FastAPI's Dependency Injection system helps you organize code, making it reusable, modular, and clean.

- Dependencies can be functions, classes, or even simple logic encapsulated in objects.

- Using query parameters, path parameters, multiple dependencies, and class-based dependencies makes your code more maintainable and easier to manage.



_**Happy Coding 🤗**_
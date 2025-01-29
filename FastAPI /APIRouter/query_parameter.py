# # When you declare other function parameters that are not part of the path parameters,
# # they are automatically interpreted as "query" parameters.

# # The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.

# # For example, in the URL:

# # https://fastapi.tiangolo.com/tutorial/query-params/?h=query
# # http://127.0.0.1:8000/items/?skip=0&limit=10
# # ...the query parameters are:

# # skip: with a value of 0
# # limit: with a value of 10
# # As they are part of the URL, they are "naturally" strings.

# # But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

# # All the same process that applied for path parameters also applies for query parameters:

# # Editor support (obviously)
# # Data "parsing"
# # Data validation
# # Automatic documentation

# # from fastapi import FastAPI

# # app = FastAPI()

# # fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# # @app.get("/items/")
# # async def read_item(skip: int = 0, limit: int =8):
# #     return fake_items_db[skip : skip + limit]

# ###############################

# #Query parameter type conversion

# # from fastapi import FastAPI

# # app = FastAPI()


# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str, q: str | None = None, short: bool = False):
# #     item = {"item_id": item_id}
# #     if q:
# #         item.update({"q": q})
# #     if not short:
# #         item.update(
# #             {"description": "This is an amazing item that has a long description"}
# #         )
# #     return item

# ###################################
# #Multiple path and query parameters

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
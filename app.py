from  fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from dotenv import load_dotenv
from services import Query,Mutation
import os
import logging


load_dotenv()

host=os.getenv("HOST")
port=os.getenv("PORT")

app=FastAPI()

schema = strawberry.Schema(query=Query,mutation=Mutation)


@app.get("/")
def root():
    return {"message": "Welcome to GraphQL API"}

app.add_route("/graphql", GraphQL(schema))

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Server is running on http://{host}:{port}/graphql")
    uvicorn.run(app, host=host, port=int(port))
    print(f"Server is running on http://{host}:{port}/graphql")
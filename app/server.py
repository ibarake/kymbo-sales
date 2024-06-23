from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from shopping_assistant.agent import agent_executor as shopping_assistant_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, shopping_assistant_chain, path="/hello")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

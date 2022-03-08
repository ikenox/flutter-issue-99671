from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="build/web", html=True))

count = 0

@app.middleware("http")
async def middleware(request: Request, call_next):

    if request.url.path == "/assets/fonts/MaterialIcons-Regular.otf":
        global count
        count += 1
        # Returns an error only first 2 requests
        if count <= 2:
            return Response(status_code=500, content="Temporary Error")
    return await call_next(request)

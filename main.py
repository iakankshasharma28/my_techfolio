from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Mount static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up template directory
templates = Jinja2Templates(directory="app/templates")

# Route for the home page
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

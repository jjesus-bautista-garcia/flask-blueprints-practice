"""Application entry point"""
from app_practice import init_app
app = init_app()

print("__name__: ", __name__)

if __name__ == "__wsgi__":
    print(__name__, " being executed...")
    app.run(host="127.0.0.1")
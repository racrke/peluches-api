from app.View import router
from waitress import serve

if __name__ == "__main__":
    serve(router.app, host='0.0.0.0', port=5000)
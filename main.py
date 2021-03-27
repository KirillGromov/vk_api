from app import app
import view
from auth.auth import auth
from app import db

app.register_blueprint(auth)

if __name__ == "__main__":
    app.run()
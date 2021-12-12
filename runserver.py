from api import create_app
from api.config.config import config_dict


app=create_app(config=config_dict['production'])

if __name__ == "__main__":
    app.run()
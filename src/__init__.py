from src.Application import flask_app
from threading import Thread
from src.imageProcessing.Main import Main

if __name__ == "__main__":
    Thread(target=flask_app.app.run(host='127.0.0.1', port=80, debug=True)).start()
    Thread(target=Main()).start()

    # Main()
    # app.run(host='127.0.0.1', port=80, debug=True)


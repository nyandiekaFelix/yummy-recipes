from yummy_recipes import APP
from waitress import serve

if __name__ == "__main__":
    # APP.run(debug=False)
    serve(APP, port=8080)
    
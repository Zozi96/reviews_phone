from app import create_app
from app.core import environment

develop = environment.get('develop')

app = create_app(develop)

if __name__ == '__main__':
    app.run()

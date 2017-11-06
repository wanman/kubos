from flask import Flask
from flask_graphql import GraphQLView

from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=False
    )
)


app.add_url_rule(
    '/graphiql',
    view_func=GraphQLView.as_view(
        'graphiql',
        schema=schema,
        graphiql=True
    )
)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)

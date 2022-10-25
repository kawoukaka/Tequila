import falcon.asgi


def create_app(config=None):
    app = falcon.asgi.App()

    return app
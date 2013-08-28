class Server(object):
    """
    A simple object to contain the data for a server as returned by the
    view_servers and find_servers api calls.

    We replace any hyphens used in tag names with underscores to make things
    easier for the client.

    e.g server.overview-url is exposed as server.overview_url
    """
    def __init__(self, properties={}):
        super(Server, self).__init__()
        for k, v in properties.items():
            setattr(self, k.replace('-', '_'), v)

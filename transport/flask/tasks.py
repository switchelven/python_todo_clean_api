import importlib

from flask import url_for, jsonify

from modules.sqlite_init import db


class TasksTransport:
    app = None
    _METHODS = ['get', 'post', 'delete', 'put']

    @staticmethod
    def init_db(task_transport):
        db.init_app(task_transport)

    @staticmethod
    def register(task_transport):
        TasksTransport.app = task_transport
        TasksTransport.init_db(task_transport)

        @task_transport.route('/', methods=['GET'])
        def main_route():
            """
            Default Routes
            """
            return jsonify({'hello': 'world new test'})

        @task_transport.route('/ping', methods=['GET'])
        def ping_pong_route():
            """
            Default Routes
            """
            return jsonify({'pong': 'No db yet'})

        @task_transport.route('/routes', methods=['GET'])
        def list_routes():
            import urllib
            output = {}
            for rule in task_transport.url_map.iter_rules():
                options = {}
                for arg in rule.arguments:
                    options[arg] = '[{0}]'.format(arg)
                methods = set(rule.methods)
                if 'OPTIONS' in methods:
                    methods.remove('OPTIONS')
                if 'HEAD' in methods:
                    methods.remove('HEAD')
                methods = ','.join(methods)
                url = url_for(rule.endpoint, **options)
                k = urllib.parse.unquote('[{}] {}'.format(methods, url))
                output[k] = rule.endpoint
            return jsonify(output), 200

        # Loading modules
        importlib.import_module('transport.flask.endpoints')

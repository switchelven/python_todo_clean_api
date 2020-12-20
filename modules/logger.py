import logging

from modules.registry import Registry


class Logger(object):
    logger = None
    LOG_LEVEL = 'ERROR'

    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        conf = Registry.registered('config')
        if conf:
            Logger.LOG_LEVEL = conf.get('log', 'level')

        self.logger.setLevel(Logger.LOG_LEVEL)

        self.set_handler(self.new_handler(logging.StreamHandler()))

    @staticmethod
    def new_handler(base_handler):
        formatter = logging.Formatter(
            """
=============== [%(name)s :: %(asctime)s :: %(levelname)s] ===============
message: %(message)s
user: %(username)s
role: %(role)s
app: %(app)s
version: %(version)s
path: %(path)s
=============== ==============================   ===============
            """,
            datefmt='%d/%m/%Y - %H:%M:%S'
        )

        base_handler.setFormatter(formatter)
        return base_handler

    def set_level(self):
        self.logger.setLevel(Logger.LOG_LEVEL)

    def set_handler(self, handler):
        handler.setLevel(Logger.LOG_LEVEL)
        self.logger.addHandler(handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

    def error(self, msg, *args, **kwargs):
        self.logger.error(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

    def exception(self, msg, *args, **kwargs):
        self.logger.exception(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

    def log(self, msg, *args, **kwargs):
        self.logger.log(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

    def info(self, msg, *args, **kwargs):
        self.logger.info(
            msg,
            extra={
                'username': Registry.registered('current-user-name', 'system'),
                'role':     Registry.registered('current-role-name', 'undefined'),
                'app':      Registry.registered('app-id', 'undefined'),
                'version':  Registry.registered('app-version', 'undefined'),
                'path':     Registry.registered('current-request-path', 'undefined')
            },
            *args, **kwargs
        )

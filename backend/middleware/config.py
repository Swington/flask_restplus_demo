import yaml

CONFIG = None
APP = None


def _read_config(config_path):
    with open(config_path, 'rb') as f:
        config = yaml.load(f)
    return config


def _load_config(config_path):
    global CONFIG
    CONFIG = _read_config(config_path)
    return CONFIG


def get_config():
    global CONFIG
    return CONFIG


def save_app(app):
    global APP
    APP = app


def get(name, default=None):
    global CONFIG
    if not name:
        raise TypeError('get expected at least 1 arguments, got 0')

    return CONFIG.get(name, default)


def setdefault(name, default=None):
    global CONFIG
    if not name:
        raise TypeError('setdefault expected at least 1 arguments, got 0')

    return CONFIG.setdefault(name, default)


def load_config_by_name(name):
    env_names = ('dev', 'test', 'prod')
    if name not in env_names:
        raise TypeError(f'env name should be in: {env_names}')
    config_by_name = dict(
        dev='config.dev.yml',
        test='config.test.yml',
        prod='config.prod.yml',
    )
    CONFIG = _read_config(config_by_name[name])
    return CONFIG

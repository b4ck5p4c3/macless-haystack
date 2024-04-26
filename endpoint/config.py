import logging
import os
import configparser


CONFIG_PATH = "data"
CONFIG_FILE = "auth.json"
CERT_FILE = "certificate.pem"  # optional
KEY_FILE = "privkey.pem"  # optional


def getConfigPath():
    script_path = os.path.abspath(__file__)
    return CONFIG_PATH if os.path.isabs(CONFIG_PATH) else os.path.dirname(script_path) + '/' + CONFIG_PATH


config = configparser.ConfigParser()
config.read(getConfigPath() + '/config.ini')


def getAnisetteServer():
    if os.environ['ANISETTE_URL']:
        return os.environ['ANISETTE_URL']
    value = config.get('Settings', 'anisette_url')
    if not value:
        return 'http://anisette:6969'
    return value


def getPort():
    value = config.get('Settings', 'port')
    if not value:
        return '6176'
    return int(value)


def getBindingAddress():
    value = config.get('Settings', 'binding_address')
    if not value:
        return '0.0.0.0'
    return value


def getUser():
    if os.environ['APPLE_ID']:
        return os.environ['APPLE_ID']
    return config.get('Settings', 'appleid', fallback=None)


def getPass():
    if os.environ['APPLE_ID_PASS']:
        return os.environ['APPLE_ID_PASS']
    return config.get('Settings', 'appleid_pass', fallback=None)


def getConfigFile():
    return getConfigPath() + '/' + CONFIG_FILE


def getCertFile():
    return getConfigPath() + '/' + config.get('Settings', 'cert', fallback=CERT_FILE)


def getKeyFile():
    return getConfigPath() + '/' + config.get('Settings', 'priv_key', fallback=KEY_FILE)


def getEndpointUser():
    if os.environ['ENDPOINT_USER']:
        return os.environ['ENDPOINT_USER']
    return config.get('Settings', 'endpoint_user', fallback=None)


def getEndpointPass():
    if os.environ['ENDPOINT_PASS']:
        return os.environ['ENDPOINT_PASS']
    return config.get('Settings', 'endpoint_pass', fallback=None)


def getLogLevel():
    if os.environ['LOGLEVEL']:
        return os.environ['LOGLEVEL']
    logLevel = config.get('Settings', 'loglevel', fallback='INFO')
    return logging.getLevelName(logLevel)

logging.basicConfig(level=getLogLevel(),
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Suppress http-log
logging.getLogger('urllib3').setLevel(logging.INFO)

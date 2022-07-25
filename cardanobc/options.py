# General imports
from pathlib import Path
from aylluiot.utils.path_utils import set_working_path
from aylluiot.devices import DeviceExecutors
from aylluiot.aws.thing import IotCore
from aylluiot.aws.service import Runner
from cardanopythonlib import base as cardanopy # type: ignore


REPO_NAME = 'ayllu-cardano-backend'

_base_path = str(Path(__file__)).split('/')
_filter_path = ['/'.join(_base_path[:i]) for i in  range(1, len(_base_path)) \
    if REPO_NAME not in _base_path[:i]][-1]

BACKEND_PATH = f"{_filter_path}/{REPO_NAME}"

_conf = f"{BACKEND_PATH}/config"
_cardano_conf = f"{_conf}/cardano_config.json"

node = cardanopy.Node(config_path=_cardano_conf)
keys = cardanopy.Keys(config_path=_cardano_conf)

def _aws():
    set_working_path(BACKEND_PATH)
    _aws_conf = f"{_conf}/aws_config.json"
    device_cardano = DeviceExecutors('iot-cardano', [node, keys])
    _thing_instance = IotCore(device_cardano, _aws_conf)
    return Runner(_thing_instance)

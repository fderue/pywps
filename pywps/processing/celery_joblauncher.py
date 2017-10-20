from celery import Celery
import os

amqp_user = os.getenv('AMQP_USER', 'guest')
amqp_password = os.getenv('AMQP_PASSWORD', 'guest')
amqp_hostname = os.getenv('AMQP_HOST', 'localhost')
amqp_port = os.getenv('AMQP_PORT', '5672')

app = Celery('joblauncher', broker='pyamqp://'+amqp_user+':'+amqp_password+'@'+amqp_hostname+':'+amqp_port+'//')


class Req(object):
    body = None
    registry_url = None
    dockerim_name = None
    dockerim_version = None
    input_data = {}
    param_as_envar = True
    volume_mapping = {}

    def __init__(self, _b=None, _url=None, _imname=None, _ver=None, _indata={}, volume_mapping={}, param_as_envar=True):
        self.body = _b
        self.registry_url = _url
        self.dockerim_name = _imname
        self.input_data = _indata
        self.dockerim_version = _ver
        self.param_as_envar = param_as_envar
        self.volume_mapping = volume_mapping


def get_env_cmd(envar=dict()):
    env_cmd = "".join([" -e WPS_INPUT_{0}={1}".format(key.upper(), val) for key, val in envar.items()])
    return env_cmd

def get_double_dash_cmd(envar=dict()):
    double_dash_cmd = "".join([" --{0} {1}".format(key, val) for key, val in envar.items()])
    return double_dash_cmd

def get_volume_mapping(volume_mapping=dict()):
    volume_mapping_cmd = "".join([" -v {0}:{1}".format(host_dir, container_dir) for host_dir, container_dir in volume_mapping.items()])
    return volume_mapping_cmd

def run_image(req):
    if req.param_as_envar:
        cmd = "docker run --rm {volume} {env_variable} {image}:{version}".format(
            env_variable=get_env_cmd(req.input_data),
            image=req.dockerim_name,
            version=req.dockerim_version,
            volume=get_volume_mapping(req.volume_mapping),
        )
    else:
        cmd = "docker run --rm {volume} {image}:{version} {double_dash_param}".format(
            double_dash_param=get_double_dash_cmd(req.input_data),
            image=req.dockerim_name,
            version=req.dockerim_version,
            volume=get_volume_mapping(req.volume_mapping),
        )

    print "cmd = "+cmd

    retcode = os.system(cmd)
    print("retcode={}".format(retcode))
    return retcode


@app.task
def task_joblauncher(req):
    print 'Task launched by celery worker'
    from collections import namedtuple
    req_object = namedtuple('Req', req.keys())(*req.values())

    run_image(req_object)
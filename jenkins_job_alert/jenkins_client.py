import requests
import time
from requests.auth import HTTPBasicAuth
from pprint import pprint

from jenkins_job_alert.config import Config
CONTENT_TYPE = 'application/json'

RUNNING_STATUSES = [
    'IN_PROGRESS',
    'PENDING',
]


def get_job_status(job: str, build: str, config: Config):
    job_link = _get_job_link(job=job, jenkins_host=config['jenkins_host'])
    headers = {'Content-Type': CONTENT_TYPE}
    last_status = ''
    while True:
        resp = requests.get(
            url=job_link,
            auth=HTTPBasicAuth(config['jenkins_user'], config['jenkins_token']),
            headers=headers,
        )
        status = resp.json()
        for current_build in status:
            if current_build['id'] == build:
                if current_build['status'] not in RUNNING_STATUSES:
                    return current_build
                continue
        time.sleep(5)


def get_active_builds(job: str, config: Config):
    job_link = _get_job_link(job=job, jenkins_host=config['jenkins_host'])
    headers = {'Content-Type': CONTENT_TYPE}
    resp = requests.get(
        url=job_link,
        auth=HTTPBasicAuth(config['jenkins_user'], config['jenkins_token']),
        headers=headers,
    )
    status = resp.json()
    return [(b['id'], b['status']) for b in status if b['status'] in RUNNING_STATUSES]


def _get_job_link(job, jenkins_host):
    url = f"{jenkins_host}/job/{job}/wfapi/runs"
    return url

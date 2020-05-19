import json


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.jenkins_host = None
        self.jenkins_user = None
        self.jenkins_token = None
        self.last_jobs = []
        self.config = self.get_config()

    def get_config(self):
        try:
            with open(self.config_file, mode='r') as conf:
                config = json.load(conf)
                self.jenkins_host = config.get('jenkins_host')
                self.jenkins_user = config.get('jenkins_user')
                self.jenkins_token = config.get('jenkins_token')
                self.last_jobs = config.get('last_jobs') or []
                return config
        except FileNotFoundError:
            return None

    def update_config_procedure(self):
        self.jenkins_host = input("Jenkins host (eq: https://host.com/jenkins): ")
        self.jenkins_user = input("Jenkins user: ")
        self.jenkins_token = input("Jenkins token: ")
        if not all([self.jenkins_token, self.jenkins_user, self.jenkins_host]):
            raise ValueError('Not valid data')
        self._save_config()
        return True

    def _save_config(self):
        with open(self.config_file, mode='w') as conf:
            json.dump(
                obj={
                    "jenkins_host": self.jenkins_host,
                    "jenkins_user": self.jenkins_user,
                    "jenkins_token": self.jenkins_token,
                    "last_jobs": self.last_jobs
                },
                fp=conf
            )

    def add_job(self, job):
        if job not in self.last_jobs:
            self.last_jobs.append(job)
            self._save_config()

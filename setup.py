from setuptools import setup, find_packages

from jenkins_job_alert import __version__, __author__, __email__


setup(
    name='jenkins_job_alert',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/k4m454k/JenkinsJobAlert/tree/master/jenkins_job_alert',
    packages=find_packages(),
    python_requires='>3.6',
    install_requires=open('requirements.txt').read().split(),
    entry_points={
        'console_scripts': [
            'jenkins_job_alert = jenkins_job_alert.entrypoint:run',
            'jja = jenkins_job_alert.entrypoint:run',
        ],
    },
)
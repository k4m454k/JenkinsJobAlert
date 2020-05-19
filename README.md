# **Python Jenkins Job Alerter for MacOS**


## Requirements:

- Python 3.7+
- PyInquirer
- pyobjc

## Installation

``` bash
$ pip3 install git+https://github.com/k4m454k/JenkinsJobAlert@master
```

## Configure
``` bash
$ jenkins_job_alert --configure
```

## Usage
``` bash
$ jenkins_job_alert job_name
```
jenkins_job_alert checks job for in progress builds and you can choice build


``` bash
$ jenkins_job_alert job_name/820
```
Specified build number
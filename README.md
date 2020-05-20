# **Python Jenkins Job Alerter for MacOS**

- Uses a native alert system for makos.
- Remembers the jobs of recent launches
- Checks for multiple active builds

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
### `jenkins_job_alert` checks job for in progress builds and you can choice build

``` bash
$ jenkins_job_alert job_name
```

### Specified build number
``` bash
$ jenkins_job_alert job_name/820
```

### `jenkins_job_alert` will offer you a choice of job

``` bash
$ jenkins_job_alert job_name
```

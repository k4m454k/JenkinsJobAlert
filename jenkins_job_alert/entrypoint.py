import argparse
from pathlib import Path
from os.path import expanduser
from jenkins_job_alert import __version__
from jenkins_job_alert.config import Config
from jenkins_job_alert.jenkins_client import get_job_status, get_active_builds
from jenkins_job_alert.menu import make_choice_selector
from jenkins_job_alert.macos_notification import notify

config = Config(Path(expanduser("~"))/Path("jenkins_job_alert.json"))


def argument_parser(argv=None):
    parser = argparse.ArgumentParser(
        description="MacOs Jenkins jobs alerter")
    parser.add_argument('job', nargs='*', default=None, type=str, help="Jenkins job name. \
                                                            eg: my-jenkins-job or my-jenkins-job/234")
    parser.add_argument("--configure", action='store_true', default=False, help="Add configuration")
    parser.add_argument('--version', action='version',
                        version='%(prog)s {0}'.format(__version__))
    args = parser.parse_args(argv)
    return args


def run():
    job = ""
    build = ""
    raw_job = []
    args = argument_parser()
    if args.configure:
        config.update_config_procedure()
        return
    if not config.jenkins_host:
        print("Config file error! Please run \njenkins_job_alert --configure")
        return
    if args.job:
        raw_job = args.job[0]

    if raw_job:
        if "/" in raw_job:
            job, build, *_ = raw_job.split("/")
        else:
            job = raw_job
        config.add_job(job=job)
    else:
        job_answer = make_choice_selector("Jobs", "Select job", config.last_jobs)
        job = job_answer['Jobs']
    if not build:
        builds = get_active_builds(job=job, config=config.config)
        if len(builds) > 1:
            answer = make_choice_selector("Builds", "Select build", [b for b, _ in builds])
            build = answer['Builds']
        elif len(builds) == 1:
            build = builds[0][0]
            print(f"Found 1 active build. Checking {job}/{build}")
        else:
            print("Not found started builds")
            return
    build_status = get_job_status(job=job, build=build, config=config.config)
    notify(title=job, subtitle=f"Build {build_status['status']}", info_text="", sound=True)


if __name__ == '__main__':
    run()

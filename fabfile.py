from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm


env.hosts = ['gdevine@puma.nerc.ac.uk']
env.activate = 'source /home/gdevine/web/prod/cf_checker/venv/bin/activate'

def gitupdate():
    local("git add .")
    local("git add -u")
    local("git commit")
    local("git push")


def deploy():
    proj_code_dir = '/home/gdevine/web/prod/cf_checker'
    app_code_dir = '/home/gdevine/web/prod/cf_checker/cf_checker'
    with settings(warn_only=True):
        if run("test -d %s" % proj_code_dir).failed:
            run("git clone git@github.com:gerarddevine/cf_checker.git %s" % proj_code_dir)
    with cd(proj_code_dir):
        run("pwd")
        run("ls -la")
        run("git pull")
        # explicit use of python executable set up by Ros (cdat_lite version)
        run("virtualenv --no-site-packages -p /home/ros/software/CDAT-5.2-cdms/bin/python venv")
        run(env.activate + " && pip install -r requirements.txt")
    with cd(app_code_dir):
        run(env.activate + " && mkdir db")
        run(env.activate + " && python manage.py syncdb --noinput")
        run(env.activate + " && chmod 777 db/cf_checker.sqlite")


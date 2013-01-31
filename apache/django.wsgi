# This application object is used by the development server
# as well as any WSGI server configured to use this file.
#
# See http://jmoiron.net/blog/deploying-django-mod-wsgi-virtualenv/


import os
import sys
import site

vepath = '/home/gdevine/web/prod/cf_checker/venv/lib/python2.5/site-packages'

# Remember original sys.path.
prev_sys_path = list(sys.path)

# add the site-packages of our virtualenv as a site dir
site.addsitedir(vepath)

# Add each new site-packages directory.
for directory in vepath:
  site.addsitedir(directory)

# add the app's directory to the PYTHONPATH
sys.path.append('/home/gdevine/web/prod/cf_checker')
sys.path.append('/home/gdevine/web/prod/cf_checker/cf_checker')

# add paths to udunits and cdat
sys.path.append('/home/ros/software/udunits-2.1.19/lib')
sys.path.append('/home/ros/software/CDAT-5.2-cdms/lib/python2.5/site-packages')


# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

for x in sys.path:
    print x

# import from down here to pull in possible virtualenv django install
os.environ['DJANGO_SETTINGS_MODULE'] = 'cf_checker.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()




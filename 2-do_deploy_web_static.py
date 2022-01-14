#!/usr/bin/python3
'''
fabric script to distribute an archive to my 2 web servers
'''

from fabric.api import put, run, env
from os.path import exists


env.hosts = ['34.75.15.70', '34.231.122.233']


def do_deploy(archive_path):
    '''distributes an archive to my web servers'''
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        '''Uploads the archive to the tmp folder'''
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        '''Uncompress the archive to the folder specified'''
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        '''Delete the archive from the web server'''
        run('rm -rf /tmp/{}.tgz'.format(file_name))


        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        '''Delete the previously generated symbolic link'''
        run('rm -rf /data/web_static/current')

        '''Creates a new the symbolic link'''
        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False

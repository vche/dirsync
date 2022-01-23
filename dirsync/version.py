"""
Project versionning info
"""

import subprocess
import os

__pkg_name__ = 'dirsync'

__version_info__ = (2, 3, 6, 'alpha', 0)


def get_version(version=__version_info__):

    dev_st = {'alpha': 'a', 'beta': 'b', 'rc': 'c', 'final': ''}

    assert len(version) == 5
    assert version[3] in dev_st.keys()

    n = 2 + (version[2] != 0)
    version_str = '.'.join([str(v) for v in version[:n]])

    if version[3] == 'final':
        return version_str

    if version[3:] == ('alpha', 0):
        return '%s.dev0+%s' % (version_str, get_git_chgset())
    else:
        return ''.join((version_str, dev_st[version[3]], str(version[4])))


def get_git_chgset():
    try:
        gitpath = os.path.join(os.getcwd(), ".git")
        if os.path.exists(gitpath):
            return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'],
                                           universal_newlines=True).strip()[:-1]
    except Exception as e:
        return str(e)
    return '?'


__version__ = get_version()

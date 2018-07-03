from packagea.package_A import PackageA
import pkg_resources  # part of setuptools

# https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/
# https://github.com/UofTCoders/studyGroup/blob/gh-pages/lessons/python/packages/lesson.md
# https://github.com/jladan/package_demo/blob/master/setup.py


class PackageB(PackageA):
    def __init__(self):
        pass

    # def get_version(self):
    #     # require = lower(name) -> name='PackageB',
    #     version = pkg_resources.require("packageb")[0].version
    #     return version

    def print_version(self):
        super().print_version()
        version = pkg_resources.require("packageb")[0].version
        print('Package_B: {}'.format(version))

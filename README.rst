===================
Header 1
===================

**Header 2**

- create a virtual environment
    python3 -m venv /Users/xxxxxx/envs/PackageB
    source activate PackageB

- install the chosen tag version (thru the PyCharm Terminal)
    pip install -e git://github.com/dmyanster/test_pkg_A.git@v0.0.4#egg=PackageA.egg-info

- python setup.py develop
- git tag v0.0.1
- git push --tags

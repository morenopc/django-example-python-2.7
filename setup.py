import os
from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
    name='Python27', version='1.0.1',
    description='OpenShift Python-2.7 Community Cartridge based application',
    author='Moreno Cunha', author_email='moreno.pinheiro@gmail.com',
    url='https://github.com/morenopc/django-example-python-2.7',
    # Instalation setup
    packages=find_packages(),
    include_package_data=True,
    install_requires=open(
        '%swsgi/openshift/requirements.txt' % os.environ.get(
            'OPENSHIFT_REPO_DIR', PROJECT_ROOT)).readlines(),
)

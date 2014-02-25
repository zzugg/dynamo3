""" Setup file """
import os
import sys

from setuptools import setup, find_packages
from dynamo3_version import git_version, UpdateVersion


HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.rst')).read()

REQUIREMENTS = [
    'botocore',
    'six',
]

TEST_REQUIREMENTS = [
    'nose',
]

if sys.version_info[:2] < (2, 7):
    TEST_REQUIREMENTS.append('unittest2')

if __name__ == "__main__":
    setup(
        name='dynamo3',
        version=git_version('dynamo3'),
        cmdclass={'update_version': UpdateVersion},
        description='Python 3 compatible library for DynamoDB',
        long_description=README + '\n\n' + CHANGES,
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
        ],
        author='Steven Arcangeli',
        author_email='stevearc@stevearc.com',
        url='http://github.com/stevearc/dynamo3',
        keywords='aws dynamo dynamodb',
        include_package_data=True,
        packages=find_packages(exclude=('tests',)),
        entry_points={
            'nose.plugins': [
                'dynamolocal=dynamo3.testing:DynamoLocalPlugin',
            ],
        },
        install_requires=REQUIREMENTS,
        tests_require=REQUIREMENTS + TEST_REQUIREMENTS,
    )
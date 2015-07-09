from setuptools import setup, find_packages

setup(
    name="pdserver",
    version="0.1",
    author="Paradrop Labs",
    description="Paradrop wireless virtualization",
    install_requires=['twisted', 'pymongo', 'docopt', 'txmongo', 'validate_email', 'bcrypt'],
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'pdserver=pdserver.core.main:main',
        ],
    },
)

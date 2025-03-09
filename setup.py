from setuptools import setup, find_packages

setup(
    name='cyber_ttl',
    version='0.2.1',
    description='A package for Modbus communication and gas concentration calculation',
    author='Karel Matějovský',
    author_email='karel@matejovsky.org',
    url='https://github.com/KodzghlyCZ/cyber_ttl_python',
    packages=find_packages(),
    install_requires=[
        'pyserial',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

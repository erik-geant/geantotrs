from setuptools import setup, find_packages

setup(
    name="geantotrs",
    version="0.1",
    description="otrs experiments",
    packages=find_packages(),
    install_requires=[
        "python-otrs",
    ]
)

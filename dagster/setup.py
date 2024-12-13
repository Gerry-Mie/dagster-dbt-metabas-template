from setuptools import find_packages, setup

setup(
    name="tick",
    packages=find_packages(exclude=["tick_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

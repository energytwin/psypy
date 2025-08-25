from setuptools import setup, find_packages

setup(
    name="psypy",
    version="0.1.3+et1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="MIT",
    description="Fork of psypy with EnergyTwin fixes",
    author="EnergyTwin",
)
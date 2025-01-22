from setuptools import setup, find_packages

setup(
    name="dns_poisoning_detector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "scapy",
        "reportlab",
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "dns_poisoning_detector=main:main",
        ],
    },
)

from setuptools import setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="curriculum",
    version="0.1.0",
    install_requires=["app"],
    author="Eric dos Santos",
    author_email="ericshantos13@gmail.com",
    description="currículo atualizado em tempo real",
    long_description=long_description,
    url="https://github.com/ericshantos/curriculum",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: General",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

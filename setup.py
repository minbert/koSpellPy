import setuptools


setuptools.setup(
    name="kospellpy",
    version="0.0.2",
    license="MIT",
    author="decyma",
    author_email="soos3121@gmail.com",
    description="Korean Spell Checker",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kangsukmin/koSpellPy",
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

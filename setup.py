from setuptools import setup, find_packages

setup(
    name="gradient_engine",
    version="0.1.0",
    author="eliird",
    author_email="irdali1996@gmail.com",
    description="Library to visualize backprop in a graph",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eliird/tara",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'graphviz'
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    include_package_data=True,
    package_data={

    },
)

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyBannerGenie",
    version="1.0.0",
    author="Irmiya Malgwi",
    author_email="godofnoor@protonmail.com",
    description="A versatile Python tool for generating high-quality Fancy Square Banners.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XchixoGhostHatkX/PyBannerGenie",  # Replace with your repo URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyfiglet",
        "colorama",
        "Pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pybannergenie = PyBannerGenie:main',  # Corrected entry point
        ],
    },
)

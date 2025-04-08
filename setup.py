from setuptools import setup, find_packages

setup(
    name="facelock",  # Package name
    version="0.1.0",  # Version number
    author="Ranuja Pinnaduwage",
    author_email="Ranuja.Pinnaduwage@gmail.com",
    description="A plug-and-play facial recognition package in python",  # Package description
    long_description=open('README.md').read(),  # Read long description from README file
    long_description_content_type="text/markdown",  # Markdown format for README
    url="https://github.com/Ranuja01/pyprofilerai",
    packages=find_packages(where="src"),  # Locate all packages under src/
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use MIT License
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Specify Python version requirement
    install_requires=[  # Dependencies
        "onnxruntime",
        "insightface",
        "opencv-python"
    ],
    include_package_data=True,  # Ensure non-Python files (like README.md) are included
    zip_safe=False,  # Indicate if the package can be reliably used as a .egg file
)
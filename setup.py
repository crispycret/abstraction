import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()
    
   
setuptools.setup(
    name="abstraction-bnadeau", # Replace with your own username
    version="0.1.1",
    author="Brandon Nadeau",
    author_email="",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crispycret/abstraction",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',    
)
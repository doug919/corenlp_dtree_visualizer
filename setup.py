import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="corenlp-vdep", # Replace with your own username
        version="0.1.0",
        author="doug919",
        author_email="doug919@gmail.com",
        description="A dependency tree visualizer for Stanford CoreNLP",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/doug919/corenlp_dtree_visualizer",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        python_requires='>=3.6',
        )

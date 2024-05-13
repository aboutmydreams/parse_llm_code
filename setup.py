import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parse_llm_code",
    version="0.1.27",
    author="aboutmydreams",
    author_email="aboutmydreams@163.com",
    description="a lib to parse llm answer to code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aboutmydreams/parse_llm_code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

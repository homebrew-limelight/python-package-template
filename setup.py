import setuptools
import re

# hacky way of reading version from __init__
# stolen from discord.py
version = ""
with open("package/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("version is not set")

with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="package-name-for-pypi",
    version=version,
    author="Your Name Here",
    author_email="you@email.com",
    description="Short project description",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/homebrew-limelight/repo-url",
    packages=setuptools.find_packages(),  # or list like in discord.py
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)

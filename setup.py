from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

NAME = "tllm"
VERSION = "0.0.0.1"
AUTHOR = "InquestGeronimo"
EMAIL = "rcostanl@gmail.com"
LD_CONTENT_TYPE = "text/markdown"
DESCRIPTION = "LLM Trainer for Fine-tuning and RL"
LICENSE = "MIT license"
PACKAGES = find_packages()
PACKAGE_DATA = {"tllm": ["scripts/*", "utils/*"]}
DEPENDENCIES = [
    "accelerate>=0.27.0",
    "bitsandbytes>=0.42.0",
    "datasets>=2.17.0",
    "peft>=0.8.2",
    "transformers>=4.37.2",
    "wandb>=0.16.3",
    "scipy>=1.11.4"
]
KEYWORDS = ["llms", "training", "fine-tuning", "LLM", "NLP"]
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
]

setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type=LD_CONTENT_TYPE,
    long_description=LONG_DESCRIPTION,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    include_package_data=True,
    install_requires=DEPENDENCIES,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
)

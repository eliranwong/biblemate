from setuptools import setup
from setuptools.command.install import install
import os, shutil, platform, sys

version = "0.2.56"
with open(os.path.join("biblemate", "version.txt"), "w", encoding="utf-8") as fileObj:
    fileObj.write(version)

# package name
package_name_0 = "package_name.txt"
with open(package_name_0, "r", encoding="utf-8") as fileObj:
    package = fileObj.read()
package_name_1 = os.path.join(package, "package_name.txt") # package readme
shutil.copy(package_name_0, package_name_1)

# update package readme
latest_readme = os.path.join("..", "README_pypi.md") # github repository readme
package_readme = os.path.join(package, "README.md") # package readme
shutil.copy(latest_readme, package_readme)
with open(package_readme, "r", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

# get required packages
install_requires = []
with open(os.path.join(package, "requirements.txt"), "r") as fileObj:
    for line in fileObj.readlines():
        mod = line.strip()
        if mod:
            install_requires.append(mod)

# make sure config.py is empty
open(os.path.join(package, "config.py"), "w").close()

# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
setup(
    name=package,
    version=version,
    python_requires=">=3.10, <3.13",
    description=f"BibleMate AI - Automate Your Bible Study",
    long_description=long_description,
    author="Eliran Wong",
    author_email="support@marvel.bible",
    packages=[
        package,
        f"{package}.core",
        f"{package}.ui",
        f"{package}.api",
        f"{package}.etextedit",
        f"{package}.etextedit.plugins",
        #f"{package}.data",
        #f"{package}.data.bibles",
    ],
    package_data={
        package: ["*.*"],
        f"{package}.core": ["*.*"],
        f"{package}.ui": ["*.*"],
        f"{package}.api": ["*.*"],
        f"{package}.etextedit": ["*.*"],
        f"{package}.etextedit.plugins": ["*.*"],
        #f"{package}.data": ["*.*"],
        #f"{package}.data.bibles": ["*.*"],
    },
    license="GNU General Public License (GPL)",
    install_requires=install_requires,
    extras_require={
        'genai': ["google-genai>=1.46.0"],  # Dependencies for running Vertex AI
    },
    entry_points={
        "console_scripts": [
            f"bm={package}.main:main",
            f"{package}={package}.main:main",
            f"{package}mcp={package}.biblematemcp:mcp",
        ],
    },
    keywords="mcp agent biblemate ai anthropic azure chatgpt cohere deepseek genai github googleai groq llamacpp mistral ollama openai vertexai xai",
    url="https://biblemate.ai",
    project_urls={
        "Source": "https://github.com/eliranwong/biblemate",
        "Tracker": "https://github.com/eliranwong/biblemate/issues",
        "Documentation": "https://github.com/eliranwong/biblemate/wiki",
        "Funding": "https://www.paypal.me/MarvelBible",
    },
    classifiers=[
        # Reference: https://pypi.org/classifiers/

        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 3.8',
        #'Programming Language :: Python :: 3.9',
        # currently, fastmcp supports 3.10-3.12
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)

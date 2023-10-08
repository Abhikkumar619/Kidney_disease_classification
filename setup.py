import setuptools

with open("README.md","r") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="Kidney_disease_classification"
AUTHOR_USER_NAME= "Abhikkumar619"
SRC_REPO='cnn_classifier'
AUTHOR_EMAIL="abisheky194@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    #It specifies the directory where setuptools should start looking for packages. "src" directory.
    packages=setuptools.find_packages(where="src")
    )

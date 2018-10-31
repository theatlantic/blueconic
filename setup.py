from setuptools import setup, find_packages
import blueconic

setup(
    name="blueconic",
    version=blueconic.__version__,
    description="Blueconic is a library for dealing with the blueconic.com API",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/theatlantic/blueconic",
    packages=find_packages(),
    python_requires='>=3',
    install_requires=["requests_oauthlib==1.0.0"]
)

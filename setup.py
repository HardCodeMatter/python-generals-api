from setuptools import setup
from src.main import app


setup(
    name=app.title,
    version=app.version,
    description='General Game API',
    author='HardCodeMatter',
    install_requires=[
        'fastapi==0.105.0',
        'SQLAlchemy==2.0.23',
        'uvicorn==0.25.0',
    ],
)

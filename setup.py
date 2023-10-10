from setuptools import setup

setup(
    name='adastratask',
    version='0.1.0',
    packages=['.'],
    install_requires=[
        'pandas>=1.2.0',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'car_analyzer=Task:main',
        ],
    },
)

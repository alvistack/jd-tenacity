from setuptools import setup

setup(
    name='tenacity',
    version='9.2.0',
    description='Retry code until it succeeds',
    author_email='Julien Danjou <julien@danjou.info>',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Utilities',
    ],
    extras_require={
        'doc': [
            'reno',
            'sphinx',
        ],
        'test': [
            'pytest',
            'tornado>=6.0',
        ],
    },
    packages=[
        'tenacity',
        'tenacity.asyncio',
    ],
)

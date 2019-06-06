import setuptools


setuptools.setup(
    name='metabot.calendars.google',
    version='0.2',
    author='Daniel Reed',
    author_email='nmlorg@gmail.com',
    description='Google Calendar loader for metabot.',
    url='https://github.com/nmlorg/metabot.calendars.google',
    packages=setuptools.find_packages(include=('metabot', 'metabot.*')),
    python_requires='>=3.5',
    install_requires=[
        'google-api-python-client',
        'metabot >= 0.2',
        'oauth2client',
    ])

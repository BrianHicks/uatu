from setuptools import setup, find_packages

setup(
    name = 'Uatu',
    version = '0.0.1',
    packages = find_packages(),

    install_requires = [
        'pyyaml',
    ],

    # testing
    test_suite = 'nose.collector',
    tests_require = [
        'nose',
    ],

    # metadata for PyPi and others
    author = 'Brian Hicks',
    author_email = 'brian@brianthicks.com',
    description = 'Uatu - the watcher',
    license = 'TODO',
    url = 'https://github.com/BrianHicks/uatu',
    download_url = 'https://github.com/BrianHicks/uatu',
    scripts = ['uatu/bin/uatu'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],

    long_description = open('README.md').read(),
)

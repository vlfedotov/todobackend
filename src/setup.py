from setuptools import setup, find_packages


setup (
    name                 = 'todobackend',
    version              = '0.1.0',
    description          = 'Todobackend Django REST service',
    packages             = find_packages(),
    include_package_data = True,
    scripts              = ['manage.py'],
    install_requires     = ['Django>=1.11.5',
                            'django-cors-headers>=2.1.0',
                            'djangorestframework>=3.6.4',
                            'mysqlclient>=1.3.12',
                            'uwsgi>=2.0', ],
    extras_require       = {
                             'test': [
                               'colorama>=0.3.9',
                               'coverage>=4.4.1',
                               'django-nose>=1.4.5',
                               'nose>=1.3.7',
                               'pinocchio>=0.4.2', 
                             ]
                           }
)


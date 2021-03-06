from setuptools import find_packages, setup

setup(
    name='example_app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'plotly',
        'pandas',
        'dash',
        'dash-bootstrap-components'
    ],
)

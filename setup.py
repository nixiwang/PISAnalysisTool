from distutils.core import setup

setup(
    name='PISAnalysisTool',
    version='0.1.0',
    author='Nixi Wang',
    author_email='nixiwang@uw.edu',
    packages=['PISAnalysisTool', 'PISAnalysisTool.tests'],
    url='http://pypi.python.org/pypi/PISAnalysisTool/',
    license='LICENSE.txt',
    description='An analysis tool of multi-level modeling for PISA dataset',
    long_description=open('README.md').read(),
    install_requires=[
      "appdirs==1.4.3",
      "appnope==0.1.0",
      "asn1crypto==0.24.0",
      "astroid==2.0.4",
      "attrs==18.2.0",
      "Automat==0.7.0",
      "backcall==0.1.0",
      "bleach==3.0.0",
      "certifi==2018.10.15",
      "cffi==1.11.5",
      "chardet==3.0.4",
      "conda==4.5.11",
      "constantly==15.1.0",
      "cryptography==2.3.1",
      "cycler==0.10.0",
      "decorator==4.3.0",
      "entrypoints==0.2.3",
      "h5py==2.8.0",
      "html5lib==1.0.1",
      "hyperlink==18.0.0",
      "idna==2.7",
      "incremental==17.5.0",
      "ipykernel==5.0.0",
      "ipython==7.0.1",
      "ipython-genutils==0.2.0",
      "ipywidgets==7.4.2",
      "isort==4.3.4",
      "jedi==0.13.1",
      "Jinja2==2.10",
      "joblib==0.13.0",
      "jsonschema==2.6.0",
      "jupyter==1.0.0",
      "jupyter-client==5.2.3",
      "jupyter-console==6.0.0",
      "jupyter-core==4.4.0",
      "kiwisolver==1.0.1",
      "lazy-object-proxy==1.3.1",
      "MarkupSafe==1.0",
      "matplotlib==3.0.0",
      "mccabe==0.6.1",
      "mistune==0.8.3",
      "mkl-fft==1.0.6",
      "mkl-random==1.0.1",
      "nbconvert==5.3.1",
      "nbformat==4.4.0",
      "notebook==5.7.0",
      "numpy==1.15.2",
      "pandas==0.23.4",
      "pandocfilters==1.4.2",
      "parso==0.3.1",
      "patsy==0.5.1",
      "pexpect==4.6.0",
      "pickleshare==0.7.5",
      "prometheus-client==0.4.0",
      "prompt-toolkit==2.0.5",
      "ptyprocess==0.6.0",
      "pyasn1==0.4.4",
      "pyasn1-modules==0.2.2",
      "pycosat==0.6.3",
      "pycparser==2.19",
      "Pygments==2.2.0",
      "pylint==2.1.1",
      "pymer4==0.6.0",
      "pyOpenSSL==18.0.0",
      "pyparsing==2.2.2",
      "PySocks==1.6.8",
      "python-dateutil==2.7.3",
      "pytz==2018.5",
      "pyzmq==17.1.2",
      "qtconsole==4.4.1",
      "requests==2.19.1",
      "rpy2==2.9.4",
      "ruamel-yaml==0.15.46",
      "scipy==1.1.0",
      "seaborn==0.9.0",
      "Send2Trash==1.5.0",
      "service-identity==17.0.0",
      "simplegeneric==0.8.1",
      "six==1.11.0",
      "terminado==0.8.1",
      "testpath==0.4.2",
      "tornado==5.1.1",
      "tqdm==4.28.1",
      "traitlets==4.3.2",
      "typed-ast==1.1.0",
      "tzlocal==1.5.1",
      "urllib3==1.23",
      "wbdata==0.2.7",
      "wcwidth==0.1.7",
      "webencodings==0.5.1",
      "widgetsnbextension==3.4.2",
      "wrapt==1.10.11",
      "zope.interface==4.5.0"
    ],
)
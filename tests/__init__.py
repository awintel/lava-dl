try:
    __import__('pkg_resources').declare_namespace(__name__)
except:  # noqa E722
    print('Error')
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
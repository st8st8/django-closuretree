from pkg_resources import get_distribution, DistributionNotFound

try:
    __VERSION__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

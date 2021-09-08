import tzlocal


def localize(timezone_unaware):
    return tzlocal.get_localzone().localize(timezone_unaware)

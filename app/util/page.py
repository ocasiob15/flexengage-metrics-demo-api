
class PageRequest:
    def __init__(self, page: int, page_size: int):
        self.page = page
        self.page_size = page_size


def default_page_request() -> PageRequest:
    return PageRequest(0, 20)


def get_pagination_request_from_args(query_params) -> PageRequest:
    try:
        page_size: int = int(query_params.get("page_size"))
    except Exception as e:
        print(e)
        return default_page_request()

    try:
        page: int = int(query_params.get("page"))
    except Exception as e:
        print(e)
        return default_page_request()

    if page_size is None:
        return default_page_request()
    if page is None:
        return default_page_request()

    return PageRequest(page, page_size)

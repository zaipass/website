from rest_framework.pagination import PageNumberPagination


class NewsListPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response


class GoodsListPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['range_pages'] = [num for num in range(1, self.page.paginator.num_pages + 1)]
        response.data['total_pages'] = self.page.paginator.num_pages
        return response

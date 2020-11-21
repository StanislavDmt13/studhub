from rest_framework.pagination import PageNumberPagination


class SimplePagePagination(PageNumberPagination):
    max_page_size = 500

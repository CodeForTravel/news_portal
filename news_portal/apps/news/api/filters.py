from rest_framework import filters



class TopHeadlineFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_dict = {}
        home_page = request.query_params.get("home_page")
        if home_page or not request.user.is_authenticated:
            return queryset

        user = request.user
        country_of_news = [s.lower() for s in user.country_of_news]
        if country_of_news:
            filter_dict["source__country__in"] = country_of_news

        if user.news_sources.all():
            filter_dict["source__in"] = user.news_sources.all()

        if filter_dict:
            queryset = queryset.filter(**filter_dict)
        return queryset
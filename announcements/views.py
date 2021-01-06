from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Announcement
from .permissions import IsAnnouncementAuthorOrReadOnly
from .serializers import AnnouncementListCreateSerializer
from .serializers import AnnouncementRetrieveSerializer
from .mixins import AnnouncementsMixin
from .mixins import AnnouncementsMapMixin


class AnnouncementListCreateAPIView(ListCreateAPIView):
    """Список всех объявлений/Создание объявления."""

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AnnouncementRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """Получение/удаление объявления."""

    queryset = Announcement
    serializer_class = AnnouncementRetrieveSerializer
    permission_classes = (IsAnnouncementAuthorOrReadOnly, )


class UserAnnouncementsListAPIView(AnnouncementsMixin,
                                   ListAPIView):
    """Объявления пользователя с указанным user_id."""

    def get_queryset(self):
        return Announcement.objects.filter(
            user_id=self.kwargs.get(self.lookup_url_kwarg))


class FeedForUserListAPIView(AnnouncementsMixin,
                             ListAPIView):
    """Лента объявлений для пользователя с указанным user_id."""

    def get_queryset(self):
        return Announcement.objects.exclude(
            user_id=self.kwargs.get(self.lookup_url_kwarg))


class AnnouncementsMapListAPIView(AnnouncementsMapMixin,
                                  ListAPIView):
    """Карта всех объявлений."""

    queryset = Announcement.objects.all()


class AnnouncementsMapForUserListAPIView(AnnouncementsMapMixin,
                                         ListAPIView):
    """
    Карта объявлений \
    (без объявлений, созданных пользователем с указанным user_id).
    """

    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return Announcement.objects.exclude(
            user_id=self.kwargs.get(self.lookup_url_kwarg))

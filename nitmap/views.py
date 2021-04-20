from django.shortcuts import get_object_or_404
from geojson import Feature, FeatureCollection, Point, dumps
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .models import Points, Lines, Instance, Client, Equipment
from dal import autocomplete
from django.db.models import Q


class PointAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if not self.request.user.is_authenticated:
            return Client.objects.none()
        qs = Points.objects.all()
        if self.q:
            qs = qs.filter(Q(street__name__icontains=self.q) | Q(number__icontains=self.q))
        return qs


class HomePageView(TemplateView):
    template_name = 'index.html'


def main_view(request):
    return render(request, 'index.html')


def points_dataset(request):
    """Выбор всех точек и подключений на них"""
    my_collection = []
    points = Points.objects.all()

    for i in points:
        props = {'point': '', 'info': []}  # Словарь точек и доп. информации о них
        inst = Instance.objects.filter(point=i.id).values()  # Выбираем все подключения на каждой точки
        my_point = Point(i.points)
        props['point'] = str(i)

        for j in inst:
            # Выбираем информацию о клиенте в каждом подключении
            client = Client.objects.get(id=j['client_id'])
            client_id = client.id
            client_name = str(client)

            # добавляем дополнительную информацию в словарь с данными о точках
            props['info'].append(
                [client_name + '<br>' + j['lan'] + '/' + str(j['lan_mask']) + '\n', client_id, j['id']])

        my_feature = Feature(geometry=my_point, properties=props)
        my_collection.append(my_feature)

    return HttpResponse(dumps(FeatureCollection(my_collection)), content_type='json')


def bspd_circle(request):
    polygons = serialize('geojson', Points.objects.filter(with_circle=True))
    return HttpResponse(polygons, content_type='json')


def lines_dataset(request):
    lines = serialize('geojson', Lines.objects.all())
    return HttpResponse(lines, content_type='json')


def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    equipments = Equipment.objects.filter(client=client_id)

    return render(request, 'client_detail.html', {'client': client, 'equip': equipments})

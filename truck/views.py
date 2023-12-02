from django.core.exceptions import ValidationError
from django.db.models.expressions import RawSQL
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from truck.forms import UploadCSVForm
from truck.models import Truck
from truck.utils import load_data_from_csv


class FoodTruckListAPIView(View):
    """Main page and data query handler"""
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # Get latitude, longitude and no of results from query parameters
        latitude = self.request.GET.get('latitude')
        longitude = self.request.GET.get('longitude')
        results = self.request.GET.get('results')
        # clean results
        try:
            results = int(results)
        except:
            results = 5
        results = 0 if results < 0 else results

        # Validate inputs
        if not latitude or not longitude:
            context = {
                'foodtrucks': Truck.objects.none(),
                'lat': None,
                'lng': None,
                'missing_data': not Truck.objects.all().exists()
            }
        else:
            # Calculate distance using Haversine formula
            gcd_formula = "6371000 * acos(least(greatest(\
                cos(radians(%s)) * cos(radians(latitude)) \
                * cos(radians(longitude) - radians(%s)) + \
                sin(radians(%s)) * sin(radians(latitude)) \
                , -1), 1))"

            distance_raw_sql = RawSQL(
                gcd_formula,
                (latitude, longitude, latitude)
            )

            # Order by distance and limit to at least 5 results
            queryset = Truck.objects.annotate(distance=distance_raw_sql).order_by('distance')[:results]

            context = {
                'foodtrucks': queryset,
                'lat': latitude,
                'lng': longitude
            }
        context['segment'] = 'home'
        return render(request, self.template_name, context)


class UploadCSVView(View):
    """Csv file upload handler"""
    template_name = 'upload_csv.html'

    def get(self, request, *args, **kwargs):
        """Render csv upload page"""
        form = UploadCSVForm()
        context = {
            'segment': 'upload_csv',
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """Handle uploaded csv and load data to Truck model"""
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # load data to model
                uploaded_file = form.cleaned_data['csv_file']
                load_data_from_csv(uploaded_file)
                # Redirect to index page
                return redirect(reverse('index'))
            except ValidationError as e:
                form.add_error('csv_file', e)

        return render(request, self.template_name, {'form': form})

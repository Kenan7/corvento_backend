from django.views import View
from sheets_api.utils import get_data_from_sheets


class SheetView(View):
    write_data = get_data_from_sheets

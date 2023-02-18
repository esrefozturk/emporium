from datetime import datetime, timezone

from django.core.management.base import BaseCommand
from pandas import read_csv

from backend.models import Project, Company, WTG


class Command(BaseCommand):

    def handle(self, *args, **options):

        Project.objects.all().delete()
        Company.objects.all().delete()
        WTG.objects.all().delete()

        project_raw_table = read_csv('Project_raw_table.csv')
        records = project_raw_table.to_dict('records')
        for record in records:
            if type(record['acquisition_date']) != str:
                del record['acquisition_date']
            else:
                record['acquisition_date'] = datetime.strptime(record['acquisition_date'], '%d/%M/%Y').astimezone(
                    timezone.utc)

            Company.objects.get_or_create(id=record['company_id'])

            Project.objects.create(**record)

        wtg_raw_table = read_csv('WTG_raw_table.csv')
        records = wtg_raw_table.to_dict('records')
        for record in records:


            try:
                WTG.objects.create(**record)
            except Exception:
                pass

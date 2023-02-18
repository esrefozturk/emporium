from datetime import datetime, timezone

from rest_framework import serializers

from backend.models import Project, WTG


class ProjectSerializer(serializers.ModelSerializer):
    WTG_numbers = serializers.SerializerMethodField()
    total_kW = serializers.SerializerMethodField()
    months_acquired = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_WTG_numbers(self, project):
        return WTG.objects.filter(project=project).count()

    def get_total_kW(self, project):
        return sum([float(w.kW) for w in WTG.objects.filter(project=project)])

    def get_months_acquired(self, project):
        if project.acquisition_date:
            return (datetime.utcnow().astimezone(
                timezone.utc) - project.acquisition_date).days // 30  # TODO: this is estimation
        else:
            return None

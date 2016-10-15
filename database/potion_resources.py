from database.models import *
from flask_potion import ModelResource


class CampaignResource(ModelResource):
    class Meta:
        model = Campaign

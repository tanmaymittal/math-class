from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
# from django.contrib.postgres.fields import JSONField


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'genderMath'
    players_per_group = None
    num_rounds = 1
    bg_template = 'genderMath/bg.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    initialRanks = models.StringField() # should collect 25 ranks 
    initialAvgs = models.StringField() # should collect 10 ranks 
    FinalAvgs = models.StringField() # should collect 10 new ranks 
    # ir = JSONField(db_index=True)
    pass

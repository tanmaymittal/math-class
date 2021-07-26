from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import (models)
import csv 
from django.db import models

# with open ('/Users/tan/Desktop/projects/LEEEPS/mathBias/genderMath/experiment_data_25sampled.csv') as f:
#     reader = csv.reader(f)
#     for row in reader: 
#         obc = objects.get_or_create(
#         first_name = row[0],
        
#         )


class background(Page):
    "This page introduces the experiment"
    pass


class classroom(Page):
    "This page introduces the assigned class to the subject with flashcards"
    "Rank the students with fill in the blanks as ranks"
    pass
    # form_model = 'player'
    # # form_fields = ['name', 'age']
    # # form_model = models.Player
    # form_fields = ['ir']
    # def get_form_fields(self):
    #     pass
        # if self.player.num_bids == 3:
        #     return ['bid_1', 'bid_2', 'bid_3']
        # else:
        #     return ['bid_1', 'bid_2']
    


    # def vars_for_template(self):
    #     choice_one = self.player.ir 
    #     return dict(
    #         c = [choice_one]
    #     )
    pass


class studentAverages(Page):
    "This page shows student averages accross the whole group, then asks to rate"
    pass


class trueAvgs(Page):
    "This page shows true values of flashcard ranks and then asks to fill"
    "in the blanks for average scores again"
    pass


class IAT(Page):
    pass

class exitSurvey(Page):
    pass


page_sequence = [
    background, 
    classroom, # will have flashcards 
    studentAverages, # will have avg values and fill in the blanks
    trueAvgs, # will show Flashcards with values and then fill blanks again
    # IAT, 
    exitSurvey 
]

"""
page_sequence = [
    background, 
    classroom, 
    studentAverages, 
    trueAvgs, 
    exitSurvey 
]

classroom 
25 x fill in the blanks 
show data from csv 

studentAvereages 
10x fill in the blanks 

TrueAvgs 
10x fill in the blanks 



"""
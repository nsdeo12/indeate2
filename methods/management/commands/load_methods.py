from collections import OrderedDict
from optparse import make_option
from datetime import datetime

from django.core.management import BaseCommand

import pandas as pd
import numpy as np

from methods.models import Domain, TBL_Scope, Definitions, Indicators, Procedures

from load_definitions import fetch_tbl_scopes, fetch_tbl_scope
from methods.models import Methods

class Command(BaseCommand):


    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return:
        """


        df = pd.read_csv("methodsall.csv")

        for i in range(0, len(df.index)):
            row = df.loc[i].to_dict()

            data_dict = {}
            data_dict['name'] = row['Method']
            data_dict['problem'] = row['Problem']

            data_dict['stage'] = row['Stage']
            data_dict['lcp'] = row['LCP']
            data_dict['activity'] = row['Activity']
            data_dict['domain'] = row['Domain']
            data_dict['time_scale'] = row['Time_Scale']
            data_dict['prerequisite'] = row['Prerequisites']
            data_dict['description'] = row['Description']
            data_dict['input'] = row['Input']
            data_dict['procedure'] = row['Procedure']
            data_dict['output'] = row['Output']
            data_dict['key_benefits'] = row['Key_Benefits']
            data_dict['shortcomings'] = row['Shortcomings']
            data_dict['example'] = row['Examples']
            data_dict['external_link'] = row['External']
            data_dict['sources'] = row['Sources']

            tbl = fetch_tbl_scopes(row['TBL'])
            if tbl is not None:
                if len(tbl) > 0:
                    data_dict['tbl_scope']=tbl[0]
                else:
                    data_dict['tbl_scope']= None
            else:
                data_dict['tbl_scope'] = None
            from django.db import connection
            connection.connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")

            Methods.objects.create(**data_dict)



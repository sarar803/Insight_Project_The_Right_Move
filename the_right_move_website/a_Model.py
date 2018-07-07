import pandas as pd
import numpy as np
from sklearn.externals import joblib

pred_all = joblib.load('flaskexample/prob_18.pkl')
counts_all = joblib.load('flaskexample/X_17_counts.pkl')


def predict_vio(apt_site):
    num_slash = apt_site.count('/')
    if num_slash<4:
        answer1 = "This is not a valid StreetEasy URL"
        answer2 = ""
        answer3 = ""
        answer4 = ""
        answer5 = ""
        answer6 = ""
        answer = [answer1,answer2,answer3,answer4,answer5,answer6]
    else:
        apt = (apt_site.split('/')[4])
        apt_upper = apt.upper()
        building_low = apt_upper.replace('-', ' ')
        building_low1 = building_low.replace('_', ' ')
        manhattan1 = "BROOKLYN"
        manhattan2 = "QUEENS"
        manhattan3 = "STATEN ISLAND"
        manhattan4 = "BRONX"
        manhattan_building1 = building_low1.find(manhattan1)
        manhattan_building2 = building_low1.find(manhattan2)
        manhattan_building3 = building_low1.find(manhattan3)
        manhattan_building4 = building_low1.find(manhattan4)
        non_manhattan=max(manhattan_building1,manhattan_building2,manhattan_building3,manhattan_building4)
        if non_manhattan>-1:
            answer1 = "I don't think this building is in Manhattan... want to try again?"
            answer2 = ""
            answer3= ""
            answer4 = ""
            answer5 = ""
            answer6=""
            answer = [answer1,answer2,answer3,answer4,answer5,answer6]

        else:
            address_low2=building_low1.replace("MANHATTAN", '')
            address_low3=address_low2.replace("NEW YORK", '')
            address_upper1 = address_low3.upper()
            address_upper2 = address_upper1.rstrip()
            #print(address_upper2)
            building_row = pred_all.loc[pred_all['Address'] == address_upper2]
            building_row_counts = counts_all.loc[counts_all['Address'] == address_upper2]
            if len(building_row)==0:
                answer1="I don't know anything about this building"
                answer2 = ""
                answer3= ""
                answer4 = ""
                answer5 = ""
                answer6=""
                answer = [answer1,answer2,answer3,answer4,answer5,answer6]

            else:
                vio_heat_cat = building_row.iloc[0][3]
                vio_noise_cat = building_row.iloc[0][1]
                vio_ele_cat = building_row.iloc[0][7]
                ele_buildings = building_row.iloc[0][5]
                heat_17_counts = building_row_counts.iloc[0][1]
                noise_17_counts = building_row_counts.iloc[0][2]
                ele_17_counts = building_row_counts.iloc[0][0]
                if ele_buildings==0:
                    answer1 = "likelihood of a heat problem: "+ str(vio_heat_cat.upper())+"."
                    answer2 = "likelihood of a noise problem: "+ str(vio_noise_cat.upper())+"."
                    answer3= "this building doesn't have an elevator."
                    answer4 = "heat complaints in 2017: "+ str(heat_17_counts)
                    answer5 = "noise complaints in 2017: "+ str(noise_17_counts)
                    answer6=""
                    answer = [answer1,answer2,answer3,answer4,answer5,answer6]
                else:
                    answer1 = "likelihood of a heat problem: "+ str(vio_heat_cat.upper())+"."
                    answer2 = "likelihood of a noise problem: "+ str(vio_noise_cat.upper())+"."
                    answer3 = "likelihood of an elevator problem: "+ str(vio_ele_cat.upper())
                    answer4 = "heat complaints in 2017: "+ str(heat_17_counts)
                    answer5 = "noise complaints in 2017: "+ str(noise_17_counts)
                    answer6 = "elevator complaints in 2017: "+ str(ele_17_counts)
                    answer = [answer1,answer2,answer3,answer4,answer5,answer6]
    return(answer)


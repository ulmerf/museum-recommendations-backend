__author__ = "HS"

import os
import pandas as pd
import numpy as np
import json
import random

random.seed(10)


def create_mockup_data():
    VISITORS = 10
    data = []

    data.append({'id_vis': 0,
                    'name_vis': 'TBD',
                    'processed': False,
                    'art':[{'id_art': 1, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 2, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 3, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 4, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)}
                           ]})

    for i in range(1, VISITORS):
      data.append({'id_vis': i,
                    'name_vis': 'TBD',
                    'processed': True,
                    'art':[{'id_art': 1, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 2, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 3, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 4, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 5, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 6, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 7, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 8, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 9, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},
                            {'id_art': 10, 'name_art': 'TBD', 'joy': random.randint(1,5), "inpiration": random.randint(1,5), 'excitement': random.randint(1,5), "percieved time": random.randint(1,5), "clicks": random.randint(1,20)},]
                                    })
      
    #print(json.dumps(data, indent=4))

    out_file = open("visitors.json", "w") 
    json.dump(data, out_file, indent = 4) 
    out_file.close() 

def main():
    # get current visitor art profile

    # set dev variables 
    #CURRENT_VISITOR_ID = 0
    #CURRENT_VISITOR = df.loc[df["id_vis"] == CURRENT_VISITOR_ID]

    df = pd.read_json('visitors.json')

    # TODO for
    CURRENT_VISITOR = df.loc[df["processed"] == False]

    CURRENT_VISITOR_ART = CURRENT_VISITOR["art"]

    #print(CURRENT_VISITOR_ART)

    CURRENT_VISITOR_SCORE = {"joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []}
    for i in CURRENT_VISITOR_ART[0]:
      CURRENT_VISITOR_SCORE["joy"].append(i["joy"]) 
      CURRENT_VISITOR_SCORE["inpiration"].append(i["inpiration"]) 
      CURRENT_VISITOR_SCORE["excitement"].append(i["excitement"]) 
      CURRENT_VISITOR_SCORE["percieved time"].append(i["percieved time"]) 
      CURRENT_VISITOR_SCORE["clicks"].append(i["clicks"])
    CURRENT_VISITOR_SCORE["joy"] = sum(CURRENT_VISITOR_SCORE["joy"])/len(CURRENT_VISITOR_SCORE["joy"])
    CURRENT_VISITOR_SCORE["inpiration"] = sum(CURRENT_VISITOR_SCORE["inpiration"])/len(CURRENT_VISITOR_SCORE["inpiration"])
    CURRENT_VISITOR_SCORE["excitement"] = sum(CURRENT_VISITOR_SCORE["excitement"])/len(CURRENT_VISITOR_SCORE["excitement"])
    CURRENT_VISITOR_SCORE["percieved time"] = sum(CURRENT_VISITOR_SCORE["percieved time"])/len(CURRENT_VISITOR_SCORE["percieved time"]) 
    CURRENT_VISITOR_SCORE["clicks"] = sum(CURRENT_VISITOR_SCORE["clicks"])/len(CURRENT_VISITOR_SCORE["clicks"])
    #print(CURRENT_VISITOR_SCORE)



    # get baseline of art (needed)
    BASELINE_VISITOR = df.loc[df["processed"] != False]
    BASELINE_VISITOR_ART = BASELINE_VISITOR["art"]
    #BASELINE_VISITOR_ART

    BASELINE_ART_SCORE = [
                          {"id_art": 1, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 2, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 3, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 4, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 5, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 6, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 7, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 8, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 9, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []},
                          {"id_art": 10, "joy": [], "inpiration": [], "excitement": [], "percieved time": [], "clicks": []}
                          ]
    for visitor in BASELINE_VISITOR_ART:
      for art_visitor in visitor:
        for art_baseline in BASELINE_ART_SCORE:
          if art_visitor["id_art"] == art_baseline["id_art"]:
            art_baseline["joy"].append(art_visitor["joy"]) 
            art_baseline["inpiration"].append(art_visitor["inpiration"]) 
            art_baseline["excitement"].append(art_visitor["excitement"]) 
            art_baseline["percieved time"].append(art_visitor["percieved time"]) 
            art_baseline["clicks"].append(art_visitor["clicks"])

    for art in BASELINE_ART_SCORE:
      art["joy"] = sum(art["joy"])/len(art["joy"])
      art["inpiration"] = sum(art["inpiration"])/len(art["inpiration"])
      art["excitement"] = sum(art["excitement"])/len(art["excitement"])
      art["percieved time"] = sum(art["percieved time"])/len(art["percieved time"]) 
      art["clicks"] = sum(art["clicks"])/len(art["clicks"])

    #print(BASELINE_ART_SCORE)



    # get recommendation(s)
    recommendation = {}  # art with smallest similarity
    recommendations = []  # art pieces ordered by smallest similarity
    similarity_rec = 9999

    # get current vistor art ids
    CURRENT_VISITOR_ART_IDS = []
    for i in CURRENT_VISITOR_ART:
      for j in i:
        CURRENT_VISITOR_ART_IDS.append(j['id_art'])

    for art in BASELINE_ART_SCORE:
      similarity_joy = abs(art["joy"] - CURRENT_VISITOR_SCORE["joy"])
      similarity_inspiration = abs(art["inpiration"] - CURRENT_VISITOR_SCORE["inpiration"])
      similarity_excitement = abs(art["excitement"] - CURRENT_VISITOR_SCORE["excitement"])
      similarity_time = abs(art["percieved time"] - CURRENT_VISITOR_SCORE["percieved time"])
      similarity_clicks = abs(art["clicks"] - CURRENT_VISITOR_SCORE["clicks"])
      similarity_all = (1/5) * (similarity_joy + similarity_inspiration + similarity_excitement + similarity_time + similarity_clicks)
      #print(similarity_all)
      recommendations.append((similarity_all,{'id_art': art['id_art'] , 'joy': art['joy'], 'inpiration': art['inpiration'], 'excitement': art['excitement'], 'percieved time': art['percieved time'], 'clicks': art['clicks']}))
      if similarity_all < similarity_rec:
         similarity_rec = similarity_all
         recommendation = {'id_art': art['id_art'] , 'joy': art['joy'], 'inpiration': art['inpiration'], 'excitement': art['excitement'], 'percieved time': art['percieved time'], 'clicks': art['clicks']}
      #print(art['id_art'], similarity_all)
    #print(recommendation)
    #print(similarity_rec)
    # sort similarity ascending
    recommendations_sort = sorted(recommendations, key=lambda tup: tup[0])
    #print(len(recommendations_sort))
    #recommendations_sort



    # get unique recommendations aka recommendations of art current user has not been to

    #recommendations_sort_unique
    #print(CURRENT_VISITOR_ART_IDS)
    for i in recommendations_sort:
      #print(i[1]['id_art'])
      if i[1]['id_art'] in CURRENT_VISITOR_ART_IDS:
        #print(i[1]['id_art'])
        recommendations_sort.remove(i) 
        #recommendations_sort_unique.append((similarity_all,{'id_art': art['id_art'] , 'joy': art['joy'], 'inpiration': art['inpiration'], 'excitement': art['excitement'], 'percieved time': art['percieved time'], 'clicks': art['clicks']}))
        #recommendations_sort_unique
    #print(len(recommendations_sort))
    #print(recommendations_sort)



    recommendation_final = []
    for i in recommendations_sort:
      recommendation_final.append((i[1]["id_art"], round(i[0],2)))

    print(recommendation_final)
    return recommendation_final


if __name__ == "__main__":
    main()

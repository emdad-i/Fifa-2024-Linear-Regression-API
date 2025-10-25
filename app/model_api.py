import pickle
from sklearn import linear_model
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

lm = loaded_model = pickle.load(open('model/model_1.pickle', 'rb'))

class Data(BaseModel):
    attacking_heading_accuracy: int
    skill_ball_control: int
    movement_acceleration: int
    movement_agility: int
    movement_reactions: int
    mentality_composure: int
    goalkeeping_kicking: int
    goalkeeping_positioning: int

app = FastAPI()

@app.post('/predict/')
async def predict(data: Data):
    new_data = pd.DataFrame(data={'attacking_heading_accuracy':[data.attacking_heading_accuracy],
                              'skill_ball_control':[data.skill_ball_control],
                              'movement_acceleration':[data.movement_acceleration],
                              'movement_agility':[data.movement_agility],
                              'movement_reactions':[data.movement_reactions],
                              'mentality_composure':[data.mentality_composure],
                              'goalkeeping_kicking':[data.goalkeeping_kicking],
                              'goalkeeping_positioning':[data.goalkeeping_positioning]})
    return str(lm.predict(new_data))

@app.get('/')
async def base():
    return 'Trying Model over api'
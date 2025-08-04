from data_fetching import fetch_movie_metadata
from feature_engineering import transform
import torch
import torch.nn as nn

movie_name = input("Enter movie name: ")
movie_year = int(input("Enter movie year: "))
info = fetch_movie_metadata(movie_name, movie_year)
testVector = transform(info)
testTensor = torch.tensor(testVector, dtype=torch.float32).unsqueeze(0)



class RatingRegressor(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)  # output = predicted rating
        )
        
    def forward(self, x):
        return self.net(x).squeeze()
    

import os

model = RatingRegressor(len(testVector))

parent_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(parent_dir, "data", "model_weights.pth")

model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
model.eval()

with torch.no_grad():
    prediction = model(testTensor)
print(prediction)
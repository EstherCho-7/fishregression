from fastapi import FastAPI
import requests

app = FastAPI()

def lr_api(l):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
    }

    response = requests.get('http://localhost:8001/weight', params=params, headers=headers)    
    j = response.json()
    r = j.get("weight")
    return r

def knn_api(l,w):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
        'weight': w,
    }

    response = requests.get('http://localhost:8002/fish', params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")
    return r

@app.get("/predict")
def predict():
    length=float(input("물고기의 길이를 입력: "))
    # weight 예측 선형회귀 API 호출
    weight = lr_api(length)
    
    # 물고기 분류 API 호출
    fish_class = knn_api(length, weight)

    print(f"length:{length} 물고기는 weight:{weight} 으로 예측되며 종류는 {fish_class}입니다") 

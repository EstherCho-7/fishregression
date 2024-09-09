from fastapi import FastAPI
import pickle
import os

app=FastAPI()

# 1. 빙어, 도미 데이터로 LinearRegression 학습
# 2. (1) 모델을 저장
# 3. API화 -> 도커 패키징 -> 컨테이너 RUN (8001)
# 4. 기존 KNeighborsClassifier API 도커 RUN (8002)
# 5. cli 프로그램 생성 -> input으로 길이 받기 -> (3) 호출 -> 결과(빙어, 도미) 출력

file='model1.pkl'

@app.get("/")
def predict(length):
    with open(file, "rb") as f:
        fish_model=pickle.load(f)
    
    # weight 예측 선형회귀 API 호출
    #weight=lr_api(length)

    # 물고기 분류 API 호출
    #fish_class=knn_api(length, weight)

    """
    물고기 무게 내보내기

    Args:
        length (float): 물고기 길이 (cm)

    Returns:
        weight (float): 물고기 무게 (g)
    """
    

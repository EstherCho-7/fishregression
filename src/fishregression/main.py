from fastapi import FastAPI
import pickle
import os

app=FastAPI()

# 1. 빙어, 도미 데이터로 LinearRegression 학습
# 2. (1) 모델을 저장
# 3. API화 -> 도커 패키징 -> 컨테이너 RUN (8001)
# 4. 기존 KNeighborsClassifier API 도커 RUN (8002)
# 5. cli 프로그램 생성 -> input으로 길이 받기 -> (3) 호출 -> 결과(빙어, 도미) 출력

def get_model_path():
    import os
    dir_name=os.path.dirname(__file__)
    model_path=os.path.join(dir_name, "model1.pkl")

    return model_path
                      
def get_model():
    path=get_model_path()
    with open(path, 'rb') as f:
        fish_model=pickle.load(f)
    return fish_model

@app.get("/weight")
def get_weight(length: float):
    """
    물고기 무게 내보내기

    Args:
        length (float): 물고기 길이 (cm)

    Returns:
        weight (float): 물고기 무게 (g)
    """
    fish_model=get_model()
    weight=fish_model.predict([[length]])[0]
    
    return {
            "length": length,
            "weight": weight
           }

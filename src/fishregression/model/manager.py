def get_model_path():
    import os
    dir_name=os.path.dirname(__file__)
    model_path=os.path.join(dir_name, "model1.pkl")

    return model_path

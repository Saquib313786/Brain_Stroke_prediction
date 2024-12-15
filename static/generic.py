   
def predict(InputData,prediction):
    print(prediction)
    if prediction ==0:
        if InputData[3]>200:
            prediction=1
            print(prediction)
            return prediction
        elif InputData[0]>75 and InputData[1]==1 and InputData[3]>150:
            prediction=1
            return prediction
    else:
        print(prediction)
        return prediction
    

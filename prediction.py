import numpy as np 
import pandas as pd 
from FE import load_pkl, age_feature
from warnings import filterwarnings 

def main(feats):
    x = np.array(feats).reshape(1, -1)
    y = MODEL.predict(x)
    y = 'Customer less likely to unsubscribe' if y == 0 else 'Customer more likely to unsubscribe'
    print()
    print(y)

def get_feats():
    age = int(input('Customer Age (18 - 70): '))
    gender = input('Cutomer gender (m/f) : ')
    gender = 0 if gender.lower()[0] == 'f' else 1
    print(' Choose location (enter opt number) '.center(70, '='))
    print('1) Chicago')
    print('2) Houston')
    print('3) Los Angeles')
    print('4) Miami')
    print('5) New york')
    location = 10
    while location < 0 or location > 4:
        location = int(input('location : '))
    sub_total_month = int(input('Subscription length month : '))
    monthly_bill = float(input('Monthly bill : '))
    total_usage = int(input('Total usage (GB) : '))

    age_group_enc = load_pkl('age_group.pkl')
    feats = [age, gender, location, sub_total_month, monthly_bill, total_usage, age_group_enc.transform([age_feature(age)])[0]]
    return feats

def get_feats_from_csv():
    df = pd.read_csv('test_churn_data.csv').drop(['Churn'], axis = 1)
    return df.sample(1).values.tolist()
    
if __name__ == "__main__":
    filterwarnings('ignore')
    choice = input('Input new data [n] -(or)- Get sample row from test csv [g] (n/g) : ')
    if choice.lower()[0] == 'n':
        try:
            feats = get_feats()
        except Exception as err:
            print(err)
            print('Getting random data from test.csv')
            feats = get_feats_from_csv()
    else:
        feats = get_feats_from_csv()

    # print(feats)
    MODEL = load_pkl('xgb_model.pkl')
    main(feats)
import pandas as pd

def load_and_process(url):
    df1 = (pd.read_csv(url)
        .dropna(axis=0)
        .drop("region", axis=1)
      )
        
    df2 = (df1.assign(smoker=df1["smoker"] == "yes")
            .assign(charges=round(df1["charges"], 2))
            .assign(weightStatus=df1.apply(getWeightStatus, axis=1))
          )
    
    df3 = (df2
            .sort_values("charges")
            .reset_index()
            .drop("index", axis=1)
          )
    df4 = df3[["charges", "bmi", "weightStatus", "smoker", "children", "age", "sex"]]
    return df4

def getWeightStatus(row):
    if row["bmi"] < 18.5:
        return "Underweight"
    elif row["bmi"] >= 18.5 and row["bmi"] < 25.0:
        return "Healthy Weight"
    elif row["bmi"] >= 25.0 and row["bmi"] < 30.0:
        return "Overweight"
    elif row["bmi"] >= 30.0:
        return "Obesity"
    else:
        return "Unknown"
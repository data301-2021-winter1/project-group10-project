import pandas as pd
import seaborn as sns

def load_and_process(url):
    data1 = (
        pd.read_csv(url)
            .drop("children",axis=1)
            .drop("age",axis=1)
            .drop("sex",axis=1)
    )

    data2 = (
        data1.assign(bmi=data1["bmi"].round(0))
            .assign(charges=data1["charges"].round(2))
            .assign(northern=data1["region"].str.contains("north"))
    )
    
    data3 = data2[["charges", "bmi", "smoker","region","northern"]]
    return data3
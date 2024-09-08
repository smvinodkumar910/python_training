import pandas as pd

def createDataframe(student_data: list) -> pd.DataFrame:
    return pd.DataFrame(data=student_data, columns=['student_id','age'])

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]

]
print(createDataframe(student_data))
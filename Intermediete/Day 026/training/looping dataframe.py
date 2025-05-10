import pandas as pd

student_score = {
    "student": ["alex", "bob", "chris"],
    "score": [90, 80, 70]
}

student_df = pd.DataFrame(student_score)

# loop through rows of a data frame
for (index, row) in student_df.iterrows():
    if row.student == "bob":
        print(index)
        print(row)
        print(row.student)
        print(row.score)

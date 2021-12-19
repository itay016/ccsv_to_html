import os
import pandas as pd
from pivottablejs import pivot_ui

def main():
    dir=os.getcwd()
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
       if file.endswith(".csv"):
           try:
               df=pd.read_csv(file)
           except:
               df = pd.read_csv(file, sep="|")
           name=file.split(".")
           filename=name[0]+"_data.html"
           max_k=500
           max_c=20
           dff=df[:max_k][df.columns[:max_c]]
           if len(df) > max_k:
               pivot_ui(dff, rows=list(dff.index), cols=list(dff.columns), outfile_path=name[0]+"_sample_data.html")
               pivot_ui(df, rows=list(df.index), cols=list(df.columns), outfile_path=filename)
           else:
            pivot_ui(df, rows=list(df.index), cols=list(df.columns), outfile_path=filename)


if __name__ == "__main__":
    main()
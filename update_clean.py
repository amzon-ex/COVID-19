import pandas
import os

for root, dirs, files in os.walk("/Amzon/Lab/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"):
    cleanpath = os.path.join(root,"cleaned/")
    print(cleanpath,1)
    for file in files:
        isClean = False
        if file.endswith(".csv") and not file.startswith("01"):
            file_path = os.path.join(root,file)
            for rt,drs,fls in os.walk(cleanpath):
                if file in fls: isClean = True
            if(not isClean):
                df_in = pandas.read_csv(file_path, usecols = [1,3,4,5], index_col=0)
                df_out = df_in.sum(level = 0)
                df_out.to_csv(os.path.join(cleanpath,file));
                print(f"Processed {file}")
    break   # breaks recursion at first level

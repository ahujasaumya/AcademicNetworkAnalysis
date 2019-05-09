import os
import pandas as pd
def GetPublications(concept):
    #create frame list
    frames=[]
    search_string=concept
    for filename in os.listdir('OriginAndEvolutionofConcept/s2_dblp'):
        print(filename)
        df=pd.read_csv('OriginAndEvolutionofConcept/s2_dblp/'+filename)
        #get all rows with concept in title
        df=df[df['title'].str.contains(search_string,case=False)]
        #print(df2)
        #df1=df1.append(df2,ignore_index=True)
        frames.append(df)
    df=pd.concat(frames) #use frames concat instead of directly appending as it takes more ram
    df.to_csv('OriginAndEvolutionofConcept/data/csv/df_concept.csv')

    return

def getsum(num):
    val=1+num
    return val


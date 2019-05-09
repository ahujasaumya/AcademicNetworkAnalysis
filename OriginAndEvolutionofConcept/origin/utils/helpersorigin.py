import os
import pandas as pd
import networkx as nx
def GetPublications(concept):
    #create frame list
    frames=[]
    #df=pd.DataFrame()
    search_string=concept
    directory_path=os.path.expanduser("~")
    for filename in os.listdir(directory_path+'\OriginAndEvolutionofConcept\data\s2_dblp'):
        df=pd.read_csv(directory_path+'\OriginAndEvolutionofConcept\data\s2_dblp\\'+filename)
        #get all rows with concept in title
        df=df[df['title'].str.contains(search_string,case=False)]
        #print(df2)
        #df1=df1.append(df2,ignore_index=True)
        frames.append(df)
    df=pd.concat(frames) #use frames concat instead of directly appending as it takes more ram
    df.to_csv(directory_path+'\OriginAndEvolutionofConcept\data\csv\df_concept.csv')

    return

def CreateGraph(dictoflist):
    return nx.from_dict_of_lists(dictoflist)

def DisplayGraph_SpringLayout(Graph):
    pos_oo_l1 = nx.drawing.layout.spring_layout(Graph)
    nx.draw(Graph,pos=pos_oo_l1)
    
def GetDetailsofReferences(outCitationList):
    #get details of references
    frames=[]
    directory_path=os.path.expanduser("~")
    for filename in os.listdir(directory_path+'\OriginAndEvolutionofConcept\data\s2_dblp'):
        df_oo_l1=pd.read_csv(directory_path+'\OriginAndEvolutionofConcept\data\s2_dblp\\'+filename)
        frames.append(df_oo_l1[df_oo_l1['id'].isin(outCitations_origin)])
    df_reference_details=pd.concat(frames) #use frames concat instead of directly appending as it takes more ram
    df_refernce_details.to_csv(directory_path+'\OriginAndEvolutionofConcept\data\csv\df_reference_details.csv')
    return 

def GetDetailsofAllDFRows(dataframe):
    frame=[]
    #todo:convert o(n*m) to o(m) by passing complete list for all rows at once 
    for index,row in dataframe.iterrows():
        frames=[]  
        #get details of references
        GetDetailsofReferences(dataframe['outCitations'][index])
        df_temp_network=pd.read_csv(directory_path+'\OriginAndEvolutionofConcept\data\outputs\df_reference_details.csv')
        df_temp_network=df_temp_network.append(row)

        #find similarities
        df_temp_network['paperAbstract'] = df_temp_network['paperAbstract'].replace(np.nan, '', regex=True)
        tfidf = vectorizer.fit_transform(df_temp_network['paperAbstract'])
        similarities=((tfidf * tfidf.T).A)[len(df_temp_network.index)-1]
        df_temp_network['similarity']=similarities
        #drop row
        df_temp_network.drop(df_temp_network.loc[df_temp_network['title']==row['title']].index, inplace=True)
        df_temp_network['source']=row['id']
        frame.append(df_temp_network)
    df_NetworkwithSim=pd.concat(frame)
    df_NetworkwithSim.to_csv(directory_path+'\OriginAndEvolutionofConcept\data\csv\df_dfreference_details.csv')
    return
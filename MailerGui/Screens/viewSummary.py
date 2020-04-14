import pandas as pd
import json

class GenerateSummary(object):
    def __init__(self):
        pass
    
    def return_total_recipients(self, df):
        
        if isinstance(df, pd.DataFrame):
            dataframe = df.copy()
            return len(dataframe)
        else:
            return ''
    
    def return_placeholder_text(self, placeholder):
        placeholders = []
        for i in placeholder:
            placeholders.append(i[0])
        return str(",".join(placeholders))

    
        
        
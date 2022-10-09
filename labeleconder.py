from sklearn.preprocessing import LabelEncoder 


class OneHotEcoding(LabelEncoder):
    
    def perform_label_encoding(self, column):
        column_list = column.to_list()
        le = LabelEncoder()
        le.fit(column_list)
        
        classes = le.classes_
        transform = le.transform(column_list)
        
        return classes, transform
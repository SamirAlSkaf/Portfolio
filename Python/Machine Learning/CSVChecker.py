import pandas as pd
import os


file_path = "TestNumbers.csv"

def load_csv(file_path):
    return pd.read_csv(file_path)

#Doppelte Reihen und Zeilen finden
def find_duplicates(dataframe):
    #Zeilen
    duplicate_rows = dataframe[dataframe.duplicated()]
    if not duplicate_rows.empty:
        print("Duplikat-Zeilen gefunden:")
        print(duplicate_rows)
    else:
        print("Keine Duplikat-Zeilen gefunden.")
    
    #Reihen
    transpose_df = dataframe.T
    duplicate_columns = transpose_df[transpose_df.duplicated()]
    if not duplicate_columns.empty:
        print("Duplikat-Reihen gefunden:")
        print(duplicate_columns.T)  
    else:
        print("Keine Duplikat-Reihen gefunden.")

#Leere Zellen, Non-Numbers und Range check
def check_for_issues(dataframe):
    for row_idx, row in dataframe.iterrows():
        for col_idx, value in row.items():
            #Leere Zellen prüfen
            if pd.isnull(value):
                print(f"Leere Zelle gefunden in Zeile {row_idx + 1}, Spalte {col_idx}")
            else:
                #Prüfen, ob der Wert eine Zahl ist
                try:
                    num_value = float(value)
                    #Range check (-1 bis 1)
                    if num_value < -1 or num_value > 1:
                        print(f"Zahl außerhalb des Bereichs [-1, 1] in Zeile {row_idx + 1}, Spalte {col_idx}: {num_value}")
                except ValueError:
                    print(f"Kein numerischer Wert in Zeile {row_idx + 1}, Spalte {col_idx}: {value}")


def main():
    df = load_csv(file_path)  #CSV laden
    find_duplicates(df)       #Duplikate prüfen
    check_for_issues(df)       #Leere Zellen und Non-Numbers prüfen


if __name__ == "__main__":
    main()

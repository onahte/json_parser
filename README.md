# json_parser

Program that parses certain JSON file and converts into CSV, that helps to graph the Data.

To run the following program:
- ```download``` - the following repo
- ```run``` the following command ⬇️
```py
python3 json_parser.py LabeledAllCalls.json
```
- ```toGraph.csv``` newely created with the conerted data

## Using Gephi to Graph

- Open the app
- Click new project
    - Data Labaratory
    - Import Spreadsheet
    - choose toGraph.cvs 
    - Separator: ```comma``` Import as: ```Adjacency List```
    - next & finish
    - Directed & ok
- Click ```Overview```
    - you can select nodes and move them around, to make graph more readable for testing 
- Click ```Preview```
    - Refresh
    - Under Node Labels choose:
        - Show Labels
        - set Outline Size to 10.0 __[for better visual]__

<img src="https://github.com/ppauliuchenka02/json_parser/blob/main/graph.png" alt="output">
<!-- ![Output](https://github.com/ppauliuchenka02/json_parser/blob/main/graph.png) -->
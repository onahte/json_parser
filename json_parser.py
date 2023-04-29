import json
import pandas as pd
import argparse
from pathlib import Path

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    return parser.parse_args()

def findFile(path):
    start = len(path)
    for i in range(len(path) - 1, -1, -1):
        if path[i] == '/':
            start = i + 1
            break
    return path[start:]

def convertToCSV(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)

    source = []
    target = []
    
    # weight = []
    # labels = []

    for key in data:
        affected_calls = data[key]["AffectedCalls"]
        app_calls = data[key]["AppCalls"]
        
        for call in app_calls:
            new_target = [findFile(call["Callee"][1]), call["Callee"][2], call["Callee"][3]]
            new_source = [findFile(call["Caller"][1]), call["Caller"][2], call["Caller"][3]]
            # amount = 1.0

            target.append(new_target)
            source.append(new_source)
            # weight.append(amount)
            # labels.append(new_target)

        for call in affected_calls:
            for cve_code in data[key]["AffectedCalls"][call]:
                for aff_call in data[key]["AffectedCalls"][call][cve_code]:
                    new_source = [findFile(aff_call["Callee"][1]), aff_call["Callee"][2], aff_call["Callee"][3]]
                    new_target = cve_code # edge from cve code to function call
                    # amount = 3.0

                    target.append(new_target)
                    source.append(new_source)
                    # weight.append(amount)
                    # labels.append(new_source)

    dict = {'Source': source, 'Target': target}
    # dict = {'Source': source, 'Target': target, 'Weight': weight, 'Label': labels}
    df = pd.DataFrame(dict)
    df.to_csv('toGraph.csv', index=False, header=False)

if __name__ == '__main__':
    args = _parse_args()
    if args.filepath is None:
        print("Target file does not exist or is not specified")
        raise SystemExit(1)
    target = Path(args.filepath)
    convertToCSV(target)
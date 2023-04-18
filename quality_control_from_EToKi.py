import os,sys,click,numpy as np
import pandas as pd

@click.command()
@click.argument('result')

def main(result):
    list=[]

    with open(result)as fin:
        for line in fin:
            if line.startswith('{'):
                list.append([])
                list[len(list)-1].append(line)
            else:
                list[len(list)-1].append(line)


    df = pd.DataFrame(list)
    df.to_csv('quality_control.txt',sep='\t',index=False,header=False)

if __name__ == '__main__' :
    main()

import os,sys,click,numpy as np
from sklearn.cluster import AgglomerativeClustering as AClister

@click.command()
@click.argument('kssd_out')
@click.argument('threshold',type = float ,default = 0.01)


def main(kssd_out,threshold):
    distance,names = get_distance(kssd_out)
    clust=AClister(n_clusters=None,affinity='precomputed',linkage='single',distance_threshold=threshold).fit(distance)
    name_list = [k for k , v in sorted(names.items(),key=lambda x:x[1])]
    with open("final.txt",'wt') as f:
        for n,cls in zip(name_list, clust.labels_):
            print(n,"\t",cls,file=f)

def get_distance(kssd_out):
    dist,names=[],{}
    with open(kssd_out) as fin:
        fin.readline()
        for line in fin:
            part = line.strip().split('\t')
            if part[0] not in names:
                names[part[0]]=len(names)
                for d in dist :
                    d.append(1.)
                dist.append([1.]*len(names))
            if part[1] not in names:
                names[part[1]] = len(names)
                for d in dist :
                    d.append(1.)
                dist.append([1.]*len(names))
            d = float(part[4])
            dist[names[part[0]]][names[part[1]]] = d
        dist=np.array(dist)
        dist=np.nan_to_num(dist,nan=1)

    return dist,names
#a=get_distance(kssd_out=r'E:\PY\distance3.out')
#print(a)

if __name__ == '__main__' :
    main()









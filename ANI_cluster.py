import os,sys,click,numpy as np
from sklearn.cluster import AgglomerativeClustering as AClister


@click.command()
@click.argument('ani_out')
@click.argument('threshold',type = float ,default = 99.0)

def main(ani_out,threshold):
    d_threshold = 100 - threshold
    distance,names = get_distance(ani_out)
    clust=AClister(n_clusters=None,affinity='precomputed',linkage='single',distance_threshold=d_threshold).fit(distance)
    name_list = [k for k , v in sorted(names.items(),key=lambda x:x[1])]
    with open("99.0.txt",'wt') as f:
        for n,cls in zip(name_list, clust.labels_):
            print(n,"\t",cls,file=f)

def get_distance(ani_out):
    dist,names=[],{}
    with open(ani_out) as fin:

        for line in fin:
            part = line.strip().split('\t')
            if part[0] not in names:
                names[part[0]] = len(names)
                for d in dist:
                    d.append(100.)
                dist.append([100.] * len(names))

            if part[1] not in names:
                names[part[1]] = len(names)
                for d in dist:
                    d.append(100.)
                dist.append([100.] * len(names))
            ANI= float(part[2])
            d=100-ANI
            dist[names[part[0]]][names[part[1]]] = d
        dist = np.array(dist)
    return dist, names

if __name__ == '__main__' :
    main()










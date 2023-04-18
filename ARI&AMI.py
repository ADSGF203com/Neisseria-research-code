from sklearn import metrics
with open(r"UR.csv") as fin:
    labels_true = []
    labels_pred = []
    fin.readline()
    for line in fin :
        part = line.strip().split(',')
        HC = part[0]
        ANI = part[1]
        species = part[2]
        labels_true.append(HC)
        labels_pred.append(species)



print(labels_pred)
print(metrics.adjusted_rand_score(labels_true,labels_pred))
print(metrics.adjusted_mutual_info_score(labels_true,labels_pred))

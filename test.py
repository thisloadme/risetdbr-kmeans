import numpy as np
import random

list_orang = ['Roy','Sintia','Iqbal','Dilan','Ratna','Merry','Rudi','Hafiz','Gede','Christian','Justin','Jesika','Ayu','Siska','Reitama','Ali','Bernard','Chichi','Doni','Erlan']

dataset = np.array([
    [89,90,75],
    [90,71,95],
    [70,75,80],
    [45,65,59],
    [65,75,53],
    [80,70,75],
    [90,85,81],
    [70,70,73],
    [96,93,85],
    [60,55,48],
    [45,60,58],
    [60,70,72],
    [85,90,88],
    [52,68,55],
    [40,60,70],
    [80,75,75],
    [60,75,65],
    [70,80,75],
    [60,70,70],
    [70,70,70]
])

k = 3
idx_terpakai = []
random_cluster_ids = []
# random_cluster_ids = [1, 12, 6]
while len(random_cluster_ids) < 3:
    rand_idx = random.choice(range(len(dataset)))
    if rand_idx not in idx_terpakai:
        random_cluster_ids.append(rand_idx)
    
    idx_terpakai.append(rand_idx)

print('titik cluster awal')
print([list_orang[i] for i in random_cluster_ids])
print()

centroid_data = [dataset[random_cluster_ids[i]] for i in range(len(random_cluster_ids))]

current_iter = 1
group_after = []
group_before = []

while group_before != group_after or current_iter <= 1:
    print('iterasi ke ' + str(current_iter))
    print('=' * 10)

    group_before = [item for item in group_after]

    current_cluster_data = []
    nilai_terrendah_percluster = [float('inf') for _ in range(len(dataset))]
    
    for idx_c, val_c in enumerate(random_cluster_ids):
        print('C' + str((idx_c+1)), centroid_data[idx_c])
        print('jarak dengan C' + str((idx_c+1)))
        # array jarak dengan C
        current_cluster_data.append([])
        val_centroid = centroid_data[idx_c]

        for idx,val in enumerate(dataset):
            array_perhitungan = []
            current_nilai = 0
            for idx_n in range(3):
                current_nilai += np.power(np.abs(val[idx_n] - val_centroid[idx_n]), 2)
                array_perhitungan.append('(' + str(val[idx_n]) + '-' + str(val_centroid[idx_n]) + ')**2')

            current_nilai = np.sqrt(current_nilai)
            print('data ke ' + str((idx+1)), ':', 'sqrt(' + ' + '.join(array_perhitungan) + ') = ' + str(current_nilai))

            current_cluster_data[idx_c].append(current_nilai)

            if current_nilai < nilai_terrendah_percluster[idx]:
                nilai_terrendah_percluster[idx] = current_nilai
        print()
        
    current_cluster_data = [[1 if current_cluster_data[idx_c][idx] == nilai_terrendah_percluster[idx] else 0 for idx,_ in enumerate(dataset)] for idx_c,_ in enumerate(random_cluster_ids)]
    group_after = [item for item in current_cluster_data]
    
    print([('hasil ecludean distance C' + str((i+1)) + ' : ' + (','.join("{0}".format(n) for n in val))) for i,val in enumerate(current_cluster_data)])
    print('hasilnya dengan ecludean distance iterasi sebelumnya', 'sama' if group_after == group_before else 'beda')

    new_centroid_data = []
    for idx_c in range(len(random_cluster_ids)):
        new_centroid_data.append([])
        for idx_ujian in range(3):
            current_ujian_mean = 0
            jml_data = np.count_nonzero(current_cluster_data[idx_c])
            for idx_data, val_data in enumerate(current_cluster_data[idx_c]):
                if val_data == 1:
                    current_ujian_mean += dataset[idx_data][idx_ujian]
            
            current_ujian_mean = current_ujian_mean / jml_data
            new_centroid_data[idx_c].append(current_ujian_mean)
    
    centroid_data = new_centroid_data
    current_iter += 1
    print('=' * 5)
    print()


for idx, cluster in enumerate(group_after):
    print('cluster' + str(idx+1))
    data_cluster = [list_orang[idx_data] for idx_data, val_data in enumerate(cluster) if val_data == 1]
    print(data_cluster)
    print("\n")
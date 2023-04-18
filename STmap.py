import os,sys,click,numpy as np

@click.command()
@click.argument('profile')
@click.argument('database')

def main(profile,database):
    i_dict = get_database(database)
    q_dict = get_profile(profile)

    for i in q_dict :
        if q_dict[i] in i_dict:
            print(i, end="\t")
            print(i_dict[q_dict[i]],end="\t")
            print(q_dict[i])

        else:
            print(i, end="\t")
            print('newST', end="\t")
            print('newST_complex', end="\t")
            print(q_dict[i])




def get_database(database):
    i_dict = {}
    with open(database) as fin:
        fin.readline()
        for line in fin:
            part = line.strip().split(',')

            st_data = part[0]+ '\t'+part[8]

            abcZ_num = part[1]
            adk_num  = part[2]
            aroE_num = part[3]
            fumC_num = part[4]
            gdh_num  = part[5]
            pdhC_num = part[6]
            pgm_num  = part[7]
            st_num = [abcZ_num,adk_num,aroE_num,fumC_num,gdh_num,pdhC_num,pgm_num]
            st_num =' '.join(st_num)
            i_dict[st_num] = st_data
    return i_dict


def get_profile(profile):
    q_dict = {}
    with open(profile) as fin:
        fin.readline()
        for line in fin:
            part = line.strip().split(',')
            genome = part[0]
            abcZ_num = part[1]
            adk_num = part[2]
            aroE_num = part[3]
            fumC_num = part[4]
            gdh_num = part[5]
            pdhC_num = part[6]
            pgm_num = part[7]
            st_num = [abcZ_num, adk_num, aroE_num, fumC_num, gdh_num, pdhC_num, pgm_num]
            st_num = ' '.join(st_num)
            q_dict[genome] = st_num

    return q_dict

if __name__ == '__main__' :
    main()





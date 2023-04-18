import  sys, os, click
@click.command()
@click.argument('table')
def main(table):
    dict = {}
    with open(table) as fin:
        fin.readline()
        for line in fin:
            part = line.strip().split('\t')
            if part[2] not in dict:
                dict[part[2]]=part[0]

    for key, value in dict.items():
        sys.stdout.write(key)
        sys.stdout.write('\t')
        sys.stdout.write(value)
        sys.stdout.write('\n')

if __name__ == '__main__' :
    main()
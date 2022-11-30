import csv
import sys

####################################################################################################################################################

def csv_extract(path,sep):

    """
    extract data from csv file.
    path <- file's location on computer.
    sep <- file's delimitor.
    rows -> rows of csv file.
    """
    
    rows = []
    header = []

    with open(path, encoding='UTF-8') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter = sep)
 
        for row in csv_reader:
            header.append(row)
            break

        header = header[0]

    with open(path, encoding='UTF-8') as csv_file:
    
        reader = csv.DictReader(csv_file, fieldnames=header, delimiter=sep)
    
        for row in reader:
            rows.append(row)

    return rows

def csv_write(rows,path):

    """
    write a csv file from a list.
    rows <- list exportable as csv file.
    path <- file's location on computer.
    """

    writer = open(path, "w", encoding='UTF−8')
    
    for row in rows:
        writer.write(("\t".join(row)+"\n"))
    writer.close()

####################################################################################################################################################

def proceed(args):

    """
    execution function with argparse.
    """

    rows = csv_extract(args.input_file,'\t')
    res = [["","sent_more","sent_less","stereo_antistereo","bias_type"]]

    for row in rows:

        r = []
        bias = str(row['bias_type'])
            
        if bias == args.bias:

            for key,value in row.items():
                r.append(str(value))

            res.append(r)

    csv_write(res,args.output_file)

####################################################################################################################################################
    
if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input_file", type=str, help="path to input file")
    parser.add_argument("--bias", type=str, help="see bias list in script")
    parser.add_argument("--output_file", type=str, help="path for output file")
    
    args = parser.parse_args()
    proceed(args)

import os
import subprocess

biais = ['autre','race-color','socioeconomic','gender','disability','nationality','sexual-orientation','physical-appearance','age','religion']
modeles_FR = ['camembert_large','flaubert_large','mbert','fralbert']
modeles_EN = ['bert','roberta','albert','mbert']

###########################################################################################

def proceed(args):

    corpus = args.input_file
    
    if args.lang == "FR":
        modeles = modeles_FR

    elif args.lang == "EN":
        modeles = modeles_EN

    if args.divide_bias:
        
        for b in biais:
            output = "data/bias/bias_"+b+".csv"
            subprocess.run(["python","divide_biais.py","--input_file",corpus,"--bias",b,"--output_file",output])

    if args.run_lm:
        
        for m in modeles:
            output = "data/confidence_scores/confidence_scores_"+m+".csv"
            subprocess.run(["python","metric.py","--input_file",corpus,"--lm_model",m,'--output_file',output])

    if args.run_bias_lm:

        for b in biais:
            for m in modeles:

                input_file = "data/bias/bias_"+b+".csv"
                subprocess.run(["python","metric.py","--input_file",input_file,"--lm_model",m])

###########################################################################################

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--input_file", type=str, help="path to input file")
    parser.add_argument("--lang", type=str, help="language of input file -> EN or FR")
    
    parser.add_argument("--divide_bias", action="store_true")
    parser.add_argument("--run_lm", action="store_true")
    parser.add_argument("--run_bias_lm", action="store_true")

    args = parser.parse_args()
    proceed(args)

    print("\n","-"*60,"\n","-"*27,"DONE","-"*27,"\n","-"*60)

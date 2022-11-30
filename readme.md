# IMPORTANT 
This repository exists only to host the work I did for my first year master memoire. Please refer to the following files if you want to use the work presented here :

- https://github.com/nyu-mll/crows-pairs (original CrowsPairs work)
- https://gitlab.inria.fr/french-crows-pairs/acl-2022-paper-data-and-code (french CrowsPairs work)

# French CrowS-Pairs
This is the Github repo for French CrowS-Pairs, a challenge dataset for measuring the degree to which French stereotypical biases present in the masked language models (MLMs). This challenge dataset builds on the Crows-Pairs corpus (Nangia et al. 2020) as follows: 1/ it addresses issues reported by Blodgett et al. (2021) through a revision of the original content in English 2/ it provides a translation into French of revised Crows-Pairs content and 3/ it provides newly collected stereotypes in native French using the original collection methodology described by Nangia et al. (2020). 

# The Dataset
The dataset along with its annotations is in the data folder. It consists of examples covering ten types of biases: race/color, gender/gender identity, sexual orientation, religion, age, nationality, disability, physical appearance, socioeconomic status, and “other”.

- crows_pairs_EN_revised.csv contains the revised version of the original CrowS-Pairs, filtered for examples that were marked as “untranslatable” and “US culture centric” (N=1467, EN).
- crows_pairs_EN_revised_FR_with_comments.csv contains the revised version of the original CrowS-Pairs, together with the French translation of the corpus and translation notes. DO NOT RUN THE SCRIPT ON THIS FILE. (N=1508, EN-FR) 
- crows_pairs_FR.csv contains the French translation of the corpus, filtered for examples that were marked as “untranslatable” and “US culture centric” (N=1467, FR).
- crows_pairs_FR_languagearc_contribution.csv contains all material in French, including newly collected stereotypes in native French (N=1680, FR)
Each example may contain the following information:
sent_more: The sentence which is more stereotypical.
sent_more_fr: The sentence which is more stereotypical (in French).
sent_less: The sentence which is less stereotypical.
sent_less_fr: The sentence which is less stereotypical (in French).
stereo_antistereo: The stereotypical direction of the pair. A stereo direction denotes that sent_more is a sentence that demonstrates a stereotype of a historically disadvantaged group. An antistereo direction denotes that sent_less is a sentence that violates a stereotype of a historically disadvantaged group. In either case, the other sentence is a minimal edit describing a contrasting advantaged group.
bias_type: The type of biases present in the example.
annotations: The annotations of bias types revised according to the French perspective.

# Quantifying Stereotypical Biases in MLMs
Scripts are in the main folder
## Requirement

Use Python 3 (we use Python 3.7) and install the required packages. It is recommended to use a virtual environment:

```
python3 -m venv /path/to/<venv_name>
```

And activate it:

```
source /path/to/<venv_name>/bin/activate
```

To install all requirements, you can use:

```
pip install -r requirements.txt
```

In addition, you have to install pytorch (v1.9.0). Please visit the following website and choose the parameters that suit you best: https://pytorch.org/get-started/locally/
## Reproducing Experiments 

Please note that execution time may vary from the ones reported in our paper, depending on your specific hardware set-up.
# License
French CrowS-Pairs is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. It is created using material developed by the authors of the Crows-Pairs corpus (Nangia et al. 2020)
Reference
If you use French CrowS-Pairs or our revised version of CrowS-Pairs in your work, please cite it directly:
Bezancon J, Dupont Y, Fort K, Névéol A. French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English. 2021. 


# ParseClass

Python package ParseClass for parsing JAGS log output (generated from R capture.output())

Example of use :

```python
python parser.py --source "C:\Users\Xavier\Thèse\EXP 2017\Suivi EXP\AVRIL18\pheno_12P" --param "QST" 
--filename "bilan.txt" --skipfoot 23 --mode 4

```

## class ParseFile

methods:

- __init__
- desc_textfile
- extract_values
- print_extractedvalues


## class ParseTreeFolder

methods:

- __init__
- parse_folder
- print_listofiles
- instantiate_list
- append_values
- make_value_df
- save_finaldf

## to do

- viz methods
- assertion methods
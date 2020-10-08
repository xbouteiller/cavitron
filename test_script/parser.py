# "C:\\Users\\Xavier\\Thèse\\EXP 2017\\Suivi EXP\\AVRIL18\\PHEN\\inter\\Diameter GR"

# python parser.py --source "C:\\Users\\Xavier\\Thèse\\EXP 2017\\Suivi EXP\\AVRIL18\\PHEN\\inter\\

# python parser.py --source "bilan.txt" --setdir "C:\\Users\\Xavier\\ParseProject"

# python parser.py --source "C:\Users\Xavier\Thèse\EXP 2017\Suivi EXP\AVRIL18\pheno_12P" --param "QST" --filename "bilan.txt" --skipfoot 23 --mode 4
# python parser.py --source "C:\Users\Xavier\Thèse\EXP 2017\Suivi EXP\AVRIL18\PHEN\inter" --param "QST" --filename "bilan.txt" --skipfoot 23 --mode 4
# python parser.py --source "C:\Users\Xavier\Thèse\EXP 2017\Suivi EXP\AVRIL18\PHEN\intra_us" --param "QST" --filename "bilan.txt" --skipfoot 23 --mode 4


if __name__=="__main__":

    #%% Dependencies
    import os
    import argparse
    # from ParseClass import ParseFile

    # Permet de récupérer les arguments de la commande shell
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='the source folder', type = str )
    parser.add_argument('--param', default = 'QST', help='the parameter value', type = str )
    parser.add_argument('--filename', help='the target filename', default='bilan.txt', type = str )
    parser.add_argument('--skipfoot', help='the number of lines to skip from the end', default=43, type = int )
    parser.add_argument('--mode', help='number of folders to save', default=3, type = int )
    parser.add_argument('--savename', help='the saved filename', default='extractedvalue.csv', type = str )
    args = parser.parse_args()

    rootdir = args.source
    paramtoextract = args.param
    filenametoparse = args.filename
    skipfoottodel =  args.skipfoot
    modefolder = args.mode
    savename = args.savename

    from ParseProject.ParseClass import ParseFile, ParseTreeFolder
    ptf = ParseTreeFolder()
    ptf.instantiate_list()
    ptf.parse_folder(path_folder=rootdir, targetfilename=filenametoparse)
    ptf.print_listofiles()
    ptf.append_values(param=paramtoextract, skipfoot=skipfoottodel, mode=modefolder)
    ptf.make_value_df()
    ptf.save_finaldf(FileSaveName=savename)
    print(ptf.finaldf)
    ptf.make_crosstab(print_tab = True, choice = '2.5%')

    ptf.plot_heatmap()

    # print(ptf.Value)
    # print(ptf.Folder)
    # print(ptf.Parameter)



    # parse_file = ParseFile(rootdir)
    # parse_file.desc_textfile()
    # parse_file.extract_values('QST')
    # parse_file.print_extractedvalues()

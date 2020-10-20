if __name__=="__main__":

    #%% Dependencies
    import os

    from CaviClean.ParseClass import ParseFile, ParseTreeFolder

    # ENTER FOLDER PATH HERE
    root = "C:\\Users\\Xavier\\Thèse\\Nouveau dossier"

    parse_folder = ParseTreeFolder(path = root)
    parse_folder.parse_folder()
    # parse_folder.print_listofiles()
    parse_folder.append_values()
    parse_folder.save_finaldf(FileSaveName='Formanrisk.csv')

    print(parse_folder.final_frame)

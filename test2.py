if __name__=="__main__":

    #%% Dependencies
    import os

    from ParseProject.ParseClass import ParseFile, ParseTreeFolder

    root = "F:\\FORMANRISK"

    parse_folder = ParseTreeFolder(path = root)
    parse_folder.parse_folder()
    parse_folder.print_listofiles()
    parse_folder.append_values()
    parse_folder.save_finaldf(FileSaveName='Formanrisk.csv')

    print(parse_folder.final_frame)

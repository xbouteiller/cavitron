f __name__=="__main__":

    #%% Dependencies
    import os

    from CaviClean.ParseClass import ParseFile, ParseTreeFolder

    root = os.getcwd()

    parse_folder = ParseTreeFolder()
    parse_folder.parse_folder()
    # parse_folder.print_listofiles()
    parse_folder.append_values()
    parse_folder.save_finaldf()

    print(parse_folder.final_frame)

DEBUG = False

def parse_template(
        tpl: str, 
        data: dict, 
        delimiters: tuple=("{{", "}}"), 
        default: str="N/A",
        **opts
):
    """
    fonction d'interprétation d'un template str avec des data injectées

    options **opts possibles

    debug=True: mode debug
    """
    while delimiters[0] in tpl:
        start_index = tpl.index(delimiters[0]) + len(delimiters[0])
        end_index = tpl.index(delimiters[1])
        key = tpl[start_index:end_index]
        if "debug" in opts and opts["debug"] == True:
            print(f"DEBUG - key: {key}")

        # 2/
        tpl = tpl.replace(delimiters[0] + key + delimiters[1], str(data.get(key, default)))

    return tpl

if __name__ == "__main__":
    print("coucou")
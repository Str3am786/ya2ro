import argparse

if __name__ == "__main__":

    #----------------------------------------------------------------------------------
    # Handle arguments
    #----------------------------------------------------------------------------------

    parser = argparse.ArgumentParser(
        description='Human and machine readeable input as a yalm file and create RO-Object in jsonld and/or HTML view.')

    # Required positional argument
    parser.add_argument('-i','--input', type=str, required=True,
        help='Path of the required yalm input. Follow the documentation or the example given to see the structure of the file.')

    # Optional argument
    parser.add_argument('-o', '--output_directory', type=str, help='Output diretory.')
    
    # Optional argument
    parser.add_argument('-p', '--properties_file', type=str, help='Properties file name.')

    args = parser.parse_args()

    # Default values and yalm_input
    output_directory = "output" if args.output_directory is None else args.output_directory
    properties_file = "resources/properties.yaml" if args.properties_file is None else args.properties_file
    input_yalm = args.input

    ###################################################################################
    # LOGO

    print("""
                        ad888888b,                         
                       d8"     "88                         
                               a8P                         
8b       d8 ,adPPYYba,      ,d8P"  8b,dPPYba,  ,adPPYba,   
`8b     d8' ""     `Y8    a8P"     88P'   "Y8 a8"     "8a  
 `8b   d8'  ,adPPPPP88  a8P'       88         8b       d8  
  `8b,d8'   88,    ,88 d8"         88         "8a,   ,a8"  
    Y88'    `"8bbdP"Y8 88888888888 88          `"YbbdP"'   
    d8'                                                    
   d8' 
_________________________________________________________
    """)

    #----------------------------------------------------------------------------------
    # Create RO objects and dump results
    #----------------------------------------------------------------------------------
    
    import properties

    properties.init(properties_file, input_yalm, output_directory)

    from ro_html import ro_html

    ro_html = ro_html()
    ro_html.load_data()
    ro_html.create_HTML_file()

    from ro_jsonld import ro_jsonld

    ro_jsonld = ro_jsonld()
    ro_jsonld.load_data()
    ro_jsonld.create_JSONLD_file()

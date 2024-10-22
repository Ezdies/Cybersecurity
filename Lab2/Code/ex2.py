def modify_bytes(input_filename, output_filename, byte_modifications): 
    with open(input_filename, 'rb') as f: 
        file_data = bytearray(f.read())
    
    for pos, val in enumerate(file_data):
        pos, val = byte_modifications

    with open(output_filename, 'wb') as f:
        f.write(file_data)
    

modify_bytes('tux-96_cbc_enc.bmp', 'ex2mod.bmp', [])

        
        
import os




def articleReader(relpath):
    # create path variable
    output =[]
    abs_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(abs_path,relpath)
    files =  os.listdir(file_path)

    for f in files:

        file = open(os.path.join(file_path, f))
    
        info = file.read()
        
        num_of_characters= len(info)
        
        strval= f'Number of characters in {file} : {num_of_characters}'
        
        output.append(strval)
        file.close()
    
    return output
    
        
    
    
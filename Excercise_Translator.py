#text is in this folder with Trans.txt file
#we have to convert this into hindi

#have to install Translator using pip3 install command 
from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('Trans.txt',mode='r') as my_file:
        text= my_file.read()
        translation = translator.translate(text)
    with open('Trans-ja.txt',mode='w') as my_file2:
            my_file2.write(translation) 

except FileNotFoundError as err:
        print('file doesnt exist')
        raise err
    

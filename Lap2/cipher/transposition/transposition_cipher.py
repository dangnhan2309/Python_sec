class TranspositionCipher:
    def __init__(self):
        pass
    def encrypt(self,text,key):
        text_copy = str(text)
        encrypted_text = ''
        for col in range(key):
            poiter = col
            while poiter < len(text_copy):
                encrypted_text += text_copy[poiter]
                poiter+= key
        return encrypted_text


    def decrypt(self,text,key):
        text_copy = str(text)

        dencrypted_text = ['']* key
        row, col = 0,0
        for symbol in text_copy :
            dencrypted_text[col]+= symbol
            col+= 1
            if col == key or (col == key -1 and row >= len(text_copy)%key):
                col = 0
                row +=1
        return ''.join(dencrypted_text)
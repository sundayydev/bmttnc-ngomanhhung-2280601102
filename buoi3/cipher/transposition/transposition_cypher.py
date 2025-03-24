class TranspositionCipher:
   def __init__(self):
      pass

   def encrypt(self, plain_text, key):
      encrypted_text = ""
      for col in range(key):
         pointer = col
         while pointer < len(plain_text):
            encrypted_text += plain_text[pointer]
            pointer += key
      return encrypted_text
   
   def decrypt(self, cipher_text, key):
      num_cols = len(cipher_text) // key
      num_rows = key
      num_shaded_boxes = (num_cols * num_rows) - len(cipher_text)
      
      decrypted_text = [''] * num_cols
      col, row = 0, 0
      
      for symbol in cipher_text:
         decrypted_text[col] += symbol
         col += 1
         
         if col == num_cols or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
               col = 0
               row += 1
      
      return ''.join(decrypted_text)

   
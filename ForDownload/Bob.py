from ForDownload.PGP_All_Common import *
Generate_AES_Dec_For_DigSig_Plus_Key('Enc_Output2.txt', 'KeyFile/aliceprivatekey.txt', 'R_plaintext2.txt')
sign_plan = open('R_plaintext2.txt', 'rb').read()
Verify_DigSig_On_Hashed_File('R_plaintext2.txt', 'KeyFile/bobpublickey.txt')
print()
print(sign_plan[256:].decode())


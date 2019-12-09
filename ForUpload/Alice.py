from ForUpload.PGP_All_Common import *

# 서명 생성 및 평문과 합친 값을 txt 파일로 아웃풋을 만듭니다.
Generate_DigSig_On_Hashed_File('plaintext.txt', 'KeyFile/aliceprivatekey.txt','sig_MSG_Alice.txt')

# 서명 및 평문이 합쳐진 값을 AES로 암호화 단계
# 웹서버에서 다운받은 공개키를 이용하여 세션키를 RSA 로 암호화
# 두 파일을 합쳐서 하나의 임호화 파일 생성
Generate_AES_Enc_On_DigSig_Plus_Key('sig_MSG_Alice.txt', 'ReceivedFile/bobpublickey.txt', 'Enc_Output.txt')



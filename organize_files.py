import os
import shutil  #ファイル異動で使う（次ステップ用）
import sys #コマンドライン引数を受け取るため
from datetime import datetime  #ログに日時を入れる


#拡張仕事の移動先フォルダ名
EXTENSION_MAP = {
    ".csv": "CSV",
    ".png": "画像",
    ".jpg": "画像",
    ".jpeg": "画像",
    ".pdf": "PDF"

}
# 拡張子から移動先フォルダ名を決める/該当しない拡張子は「その他」にする
def get_folder_name(file_name):
    _, ext = os.path.splitext(file_name)  #ファイル名を「名前」と「拡張子」に分ける

    ext = ext.lower()  #拡張子を小文字にそろえる(.JPG などにも対応するため)

    #辞書に登録されている拡張子ならそのフォルダ名を返す
    if ext in EXTENSION_MAP:
        return EXTENSION_MAP[ext] 
    return "その他"  #登録されていない拡張子は「その他」にする

#同じ名前のファイルがある時に重複しない名前を作る　例”sample.csv → sample_1.csv
def get_unique_file_path(target_folder_path, file_name):
    #元のファイル名を「名前」と「拡張子」に分ける
    name, ext = os.path.splitext(file_name)

    #最初はそのままの名前を使う
    new_file_name = file_name 
    new_file_path = os.path.join(target_folder_path, new_file_name)

    #同じ名前のファイルがある限り、連番を付ける
    count = 1
    while os.path.exists(new_file_path):
        new_file_name = f"{name}_{count}{ext}"
        new_file_path = os.path.join(target_folder_path, new_file_name)
        count += 1
    
    return new_file_path

# フォルダ整理ツールのメイン処理　今はファイルごとの移動先フォルダ名を表示する
def organize_folder(target_folder):
    log_file = open("log.txt", "a", encoding="utf-8")  #ログファイルを追記モードで開く

    if not os.path.exists(target_folder):  #指定したフォルダが存在するか確認する
        error_massage = f"フォルダが見つかりません：{target_folder}"
        print(error_massage)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{now}] ERROR: {error_massage}\n")  #エラーもログに残す
        return
    
    #フォルダではなくファイルが指定された場合のチェック
    if not os.path.isdir(target_folder):
        error_massage = f"フォルダではありません：{target_folder}"
        print(error_massage)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{now}] ERROR: {error_massage}\n")
        return
    
    #フォルダ内の名前を１つずつ取り出す
    for item_name in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item_name)

        #フォルダは対象外にしてファイルだけ見る
        if os.path.isfile(item_path):

            #実行中このPythonファイル自身は移動しない
            if item_name == "organize_files.py" or item_name == "log.txt" :
                continue

            folder_name = get_folder_name(item_name)
            
            target_folder_path = os.path.join(target_folder, folder_name)  #移動先フォルダのパスを作る

            #フォルダがなければ作成する
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path)
                print(f"{folder_name} フォルダを作成しました")

            #上書きしない移動先のファイルパスを作る
            target_file_path = get_unique_file_path(target_folder_path, item_name)
            
            #ファイルを移動する
            shutil.move(item_path, target_file_path)

            #実際に保存されたファイル名を取得する
            moved_file_name = os.path.basename(target_file_path)            

            print(f"{item_name} → {folder_name}/{moved_file_name} に移動しました")
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #現在の日時を文字にする
            log_file.write(f"[{now}] {item_name} → {folder_name} に移動しました\n")  #log_file.write()ファイルに文字を書き込む命令
        
    log_file.close()  #ログファイルを閉じる
            


#プログラムの開始位置
if __name__ == "__main__":
    #引数があれば、、そのフォルダを整理対象にする
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    else:
        #引数がないときは今いるフォルダを対象にする
        target_folder = os.getcwd()
    organize_folder(target_folder)


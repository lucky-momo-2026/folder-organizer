import os
import shutil  #ファイル異動で使う（次ステップ用）


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

# フォルダ整理ツールのメイン処理　今はファイルごとの移動先フォルダ名を表示する
def organize_folder(target_folder):
    log_file = open("log.txt", "a", encoding="utf-8")  #ログファイルを追記モードで開く

    if not os.path.exists(target_folder):  #指定したフォルダが存在するか確認する
        print("フォルダが見つかりません")
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

            #移動元ファイルのパスと移動先のファイルのパスを作る
            target_file_path = os.path.join(target_folder_path, item_name)
            
            #ファイルを移動する
            shutil.move(item_path, target_file_path)
            print(f"{item_name} → {folder_name} に移動しました")
            log_file.write(f"{item_name} → {folder_name} に移動しました\n")  #log_file.write()ファイルに文字を書き込む命令
        
    log_file.close()  #ログファイルを閉じる
            


#プログラムの開始位置
if __name__ == "__main__":
    #今回は自分のるフォルダを対象にする
    current_folder = os.getcwd()
    organize_folder(current_folder)

import os

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
def origanize_folder(target_folder):
    if not os.path.exists(target_folder):  #指定したフォルダが存在するか確認する
        print("フォルダが見つかりません")
        return
    
    #フォルダ内の名前を１つずつ取り出す
    for item_name in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item_name)

        #フォルダは対象外にしてファイルだけ見る
        if os.path.isfile(item_path):
            folder_name = get_folder_name(item_name)
        print(f"{item_name} → {folder_name}")


#プログラムの開始位置
if __name__ == "__main__":
    #今回は自分のるフォルダを対象にする
    current_folder = os.getcwd()
    origanize_folder(current_folder)

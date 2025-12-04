# Kindle for PC to PDF Converter

Windows 版 Kindle for PC の書籍をキャプチャして PDF に変換するツールです。

## 前提条件
- **Windows OS** 上で実行する必要があります（WSL不可）。
- Python がインストールされていること。

## インストール

1. このフォルダを Windows 上の適当な場所に配置します。
2. 依存ライブラリをインストールします:
   ```powershell
   pip install pyautogui img2pdf
   ```
   ※ `Pillow` も必要ですが `img2pdf` の依存で入るはずです。もしエラーが出たら `pip install Pillow` してください。

## 実行方法

1. コマンドプロンプトまたは PowerShell でこのフォルダを開きます。

2. スクリプトを実行します:
   ```powershell
   python main.py --output my_book.pdf
   ```
   ページ数を指定したい場合は `--pages` オプションを使います:
   ```powershell
   python main.py --output my_book.pdf --pages 100
   ```

3. 画面の指示に従い、Enterキーを押します。

4. **5秒以内**に Kindle for PC のウィンドウをアクティブにし、**全画面表示 (F11)** にしてください。

5. 自動でページがめくられ、スクリーンショットが撮られます。
   - 停止したい場合は、このターミナルウィンドウに戻って **Ctrl+C** を押してください（またはマウスを画面左上に急激に動かすと緊急停止します）。

6. 終了後、`my_book.pdf` が生成されます。

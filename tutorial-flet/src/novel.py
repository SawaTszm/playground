# 簡単なノベルゲームの体裁を見繕ってみよう のコード
import flet as ft

SAMPLE_TEXT = [
    ",昔々あるところに、おじいさんとおばあさんが住んでいました。,/images/mukashibanashi_ojiisan_obaasan.png,",
    ",おじいさんは山へしばかりに、,/images/sport_jogging_oldman.png,",
    ",おばあさんは川へせんたくに行きました。,/images/sport_walking_oldwoman.png,",
    ",おばあさんが川でせんたくをしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。,/images/fruit_peach.png,",
    ",おばあさんはどうする？,,桃を拾う,ROUTE_A,そのまま帰る,ROUTE_B",
]
ROUTE_A = [
    "おばあさん,おや、これは良いおみやげになるわ。,/images/sport_walking_oldwoman.png,",
    ",おばあさんは大きな桃を拾い上げて、家に持ち帰りました。,",
]
ROUTE_B = ["おばあさん,そんなことよりお洗濯しなくちゃ。,/images/sport_walking_oldwoman.png,", ",おばあさんは桃を見送りました。,"]


class TextRead:
    def __init__(self, page) -> None:
        # TODO: fetch text from text file
        self.current_text_file = "SAMPLE_TEXT"
        self.text_list = SAMPLE_TEXT
        self.current_index = 0
        self.text = ft.Text(value="「桃太郎」", size=20)
        self.name = ft.Text(value="")
        self.image = ft.Image(
            src="/images/monogatari_momotarou_solo.png", width=200, height=200, fit=ft.ImageFit.CONTAIN
        )
        self.page = page

    def handle_clicked(self, e):
        """handle_clicked
        クリックされた時の状況に応じて、画面の更新を行う。

        現在表示されている内容が選択肢の時: 何もしない
        テキストリストの最後までたどり着いた時: "続く……。"を表示
        それ以外: テキストを更新。選択肢がある場合は選択肢を表示

        """
        if self.current_index > 0 and len(self.text_list[self.current_index - 1].split(",")) > 4:
            return

        if len(self.text_list) < self.current_index + 1:
            self.name.value = ""
            self.text.value = "続く……。"
        else:
            split_text = self.text_list[self.current_index].split(",")
            self.name.value = split_text[0]
            self.text.value = split_text[1]
            if len(split_text) >= 3 and split_text[2]:
                self.image.src = split_text[2]
            if len(split_text) > 4:
                self.a = ft.TextButton(content=ft.Text(value=split_text[3]), on_click=self.change_route)
                self.b = ft.TextButton(content=ft.Text(value=split_text[5]), on_click=self.change_route)
                self.page.add(self.a, self.b)
            self.current_index += 1
        self.page.update()

    def change_route(self, e):
        """change_route
        選択肢をクリックしたとき、ルート分岐を行う。

        TODO: Eventオブジェクトが持つマジックナンバーに頼って分岐してるので、普遍的な参照に直したい。
        """
        split_text = self.text_list[self.current_index - 1].split(",")
        # TODO: fetch text from text file
        print(e.target)
        self.current_text_file = split_text[4] if e.target == "_14" else split_text[6]
        self.text_list = eval(self.current_text_file)
        self.current_index = 0
        self.page.controls.pop()
        self.page.controls.pop()
        self.handle_clicked(e)

    def save(self, e):
        """save

        セーブファイルに現在の情報をセーブする。

        TODO: loadファイルを選択できるようになったら上書き設定("a")に戻す
        """
        with open("save.txt", "w") as f:
            f.write(f"{self.current_text_file},{self.current_index},\n")

    def load(self, e):
        """load

        最新のセーブデータをロードする。

        TODO: 選択画面を出すshow_load()を実装して、その値を受け取ってloadできるようにする
        """
        with open("save.txt", "r") as f:
            last_save = f.readlines()[-1].split(",")
            self.current_text_file = last_save[0]
            self.text_list = eval(self.current_text_file)
            self.current_index = int(last_save[1]) - 1
            self.handle_clicked(e)

    def get_text(self):
        return self.text

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image


def main(page):
    text_read = TextRead(page)

    page.add(
        text_read.get_image(),
        ft.TextButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        text_read.get_name(),
                        text_read.get_text(),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            on_click=text_read.handle_clicked,
        ),
        ft.TextButton(
            content=ft.Text(value="save", size=10),
            on_click=text_read.save
        ),
        ft.TextButton(
            content=ft.Text(value="load", size=10),
            on_click=text_read.load,
        )
    )


ft.app(target=main, assets_dir="assets")

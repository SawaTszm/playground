# 簡単なノベルゲームの体裁を見繕ってみよう のコード
import flet as ft

SAMPLE_TEXT = [
    ",昔々あるところに、おじいさんとおばあさんが住んでいました。,/images/mukashibanashi_ojiisan_obaasan.png,",
    ",おじいさんは山へしばかりに、,/images/sport_jogging_oldman.png,",
    ",おばあさんは川へせんたくに行きました。,/images/sport_walking_oldwoman.png,",
    ",おばあさんが川でせんたくをしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。,/images/fruit_peach.png,",
    ",おばあさんはどうする？,/images/fruit_peach.png,桃を拾う,ROUTE_A,そのまま帰る,ROUTE_B",
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
        self.a = ft.TextButton(visible=False)
        self.b = ft.TextButton(visible=False)
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
                self_class = self
                self.a = ft.TextButton(
                    content=ft.Text(value=split_text[3]),
                    on_click=lambda self=self_class, e=self, route=split_text[4]: self_class.change_route(e, route),
                )
                self.b = ft.TextButton(
                    content=ft.Text(value=split_text[5]),
                    on_click=lambda self=self_class, e=self, route=split_text[6]: self_class.change_route(e, route),
                )
                self.page.add(self.a, self.b)
            self.current_index += 1
        self.page.update()

    def change_route(self, e, route):
        """change_route
        選択肢をクリックしたとき、ルート分岐を行う。
        """
        # TODO: fetch text from text file
        self.current_text_file = route
        self.text_list = eval(self.current_text_file)
        self.current_index = 0
        self.a.visible = False
        self.b.visible = False
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
            # TODO: fetch text from text file
            self.text_list = eval(self.current_text_file)
            self.current_index = int(last_save[1]) - 1
            self.a.visible = False
            self.b.visible = False
            self.handle_clicked(e)

    def get_text_container(self):
        """テキストエリアのTextButtonオブジェクトを返す"""
        return ft.OutlinedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        self.get_name(),
                        self.get_text(),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
                width=600,
                height=100,
            ),
            on_click=self.handle_clicked,
            style=ft.ButtonStyle(
                bgcolor={ft.MaterialState.HOVERED: ft.colors.WHITE},
                shape=ft.RoundedRectangleBorder(radius=0),
            ),
        )

    def get_text(self):
        """テキストエリアに表示するためのTextオブジェクトを返す"""
        return self.text

    def get_name(self):
        """テキストエリア上部に名前を表示するためのTextオブジェクトを返す"""
        return self.name

    def get_image(self):
        """人物のImageオブジェクトを返す(今のところ一つの画像だけ)"""
        return self.image


def main(page):
    page.theme_mode = "LIGHT"
    text_read = TextRead(page)

    page.add(
        text_read.get_image(),
        ft.Row(
            spacing=5,
            controls=[
                text_read.get_text_container(),
                ft.TextButton(content=ft.Text(value="save", size=10), on_click=text_read.save),
                ft.TextButton(
                    content=ft.Text(value="load", size=10),
                    on_click=text_read.load,
                ),
            ],
        ),
    )


ft.app(target=main, assets_dir="assets")

# 簡単なノベルゲームの体裁を見繕ってみよう のコード
import flet as ft

SAMPLE_TEXT = [
    ",昔々あるところに、おじいさんとおばあさんが住んでいました。,/images/mukashibanashi_ojiisan_obaasan.png",
    ",おじいさんは山へしばかりに、,/images/sport_jogging_oldman.png",
    ",おばあさんは川へせんたくに行きました。,/images/sport_walking_oldwoman.png",
    ",おばあさんが川でせんたくをしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。,/images/fruit_peach.png",
    "おばあさん,おや、これは良いおみやげになるわ。,/images/sport_walking_oldwoman.png",
    ",おばあさんは大きな桃を拾い上げて、家に持ち帰りました。",
]


class TextRead:
    def __init__(self, page) -> None:
        # TODO: fetch text from text file
        self.text_list = SAMPLE_TEXT
        self.current_index = 0
        self.text = ft.Text(value="「桃太郎」", size=20)
        self.name = ft.Text(value="")
        self.image = ft.Image(
            src="/images/monogatari_momotarou_solo.png",
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN
        )
        self.page = page

    def handle_clicked(self, e,):
        if len(self.text_list) < self.current_index + 1:
            self.name.value = ""
            self.text.value = "続く……。"
        else:
            split_text = self.text_list[self.current_index].split(",")
            self.name.value = split_text[0]
            self.text.value = split_text[1]
            if len(split_text) == 3:
                self.image.src = split_text[2]
            self.current_index += 1
        self.page.update()

    def get_text(self):
        return self.text

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image


def main(page):

    text_read = TextRead(page)

    page.add(text_read.get_image(), ft.TextButton(
        content=ft.Container(
            content=ft.Column([
                text_read.get_name(),
                text_read.get_text(),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5,
            ),
            padding=ft.padding.all(10),
        ), on_click=text_read.handle_clicked
    ))


ft.app(target=main, assets_dir="assets")

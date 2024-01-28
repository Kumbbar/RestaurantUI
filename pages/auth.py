import flet as ft
from flet_core import Page

from consts.colors import PastelColors
from consts.sizes import BUTTON_HEIGHT, BUTTON_WIGHT, BASE_HEIGHT, BR
from consts.style import CONTENT_PADDING
from consts.text import ERROR_MESSAGE
from pages.base import BasePage
from settings import MAIN_PAGE_VIEW_URL


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.background_image = ft.Image(
            src='assets/images/deckstop_background.svg',
            fit=ft.ImageFit.COVER
        )
        self.page.bgcolor = ft.colors.BLACK
        self.view_hide_text = ft.Text(
            value='View',
            color=PastelColors.LIGHT_BROWN,
            font_family='poppins medium',
        )
        self.error_message_text = ft.Text(
                color='red',
                font_family='poppins regular',
                value=ERROR_MESSAGE
        )
        self.login_input = ft.Container(
            height=BUTTON_HEIGHT,
            bgcolor='white',
            border_radius=10,
            content=ft.TextField(
                on_focus=self.password_field_in_focus,
                on_change=self.user_field_change,
                hint_text='Email',
                hint_style=ft.TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=PastelColors.INPUT_TEXT_COLOR,
                ),
                text_style=ft.TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=PastelColors.INPUT_TEXT_COLOR,
                ),
                border=ft.InputBorder.NONE,
                content_padding=CONTENT_PADDING,
                selection_color=PastelColors.DARK_BROWN,
                cursor_color=PastelColors.WHITE_BASE
            )
        )

        self.password_input = ft.Container(
            height=BUTTON_HEIGHT,
            bgcolor='white',
            border_radius=10,
            content=ft.TextField(
                on_focus=self.password_field_in_focus,
                on_change=self.user_field_change,
                password=True,
                suffix=ft.Container(
                    on_click=self.view_password,
                    content=self.view_hide_text,
                ),
                hint_text='Password',
                hint_style=ft.TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=PastelColors.INPUT_TEXT_COLOR,
                ),
                text_style=ft.TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=PastelColors.INPUT_TEXT_COLOR,
                ),
                border=ft.InputBorder.NONE,
                content_padding=CONTENT_PADDING,
                selection_color=PastelColors.DARK_BROWN,
                cursor_color=PastelColors.WHITE_BASE
            )
        )

        self.error = ft.Row(
            controls=[
                self.error_message_text
            ],
            visible=False
        )

        self.login_box = ft.Column(
            width=360,
            controls=[
                ft.Container(
                    content=ft.Text(
                        value='Login',
                        color=PastelColors.WHITE_BASE,
                        font_family='SF Pro Bold',
                        size=30,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
                ft.Container(height=2),

                self.login_input,
                self.password_input,

                ft.Container(height=1),

                self.error,

                ft.Container(height=1),

                ft.Container(
                    height=BUTTON_HEIGHT,
                    width=BUTTON_WIGHT,
                    on_click=self.switch_page,
                    bgcolor=PastelColors.DARK_BROWN,
                    border_radius=10,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value='Continue',
                        font_family='Poppins Medium',
                        size=16,

                    )
                ),
                ft.Container(height=5),
                ft.Container(
                    content=ft.Text(
                        value="Forgot your password?",
                        size=14,
                        font_family='poppins medium',
                        color=PastelColors.DARK_BROWN
                    ),
                ),
                ft.Container(height=5),

            ]
        )
        self.content = ft.Container(
            bgcolor=PastelColors.WHITE_BASE,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            expand=True,
            content=ft.Stack(
                controls=[
                    self.background_image,
                    ft.Container(
                        border_radius=BR,
                        height=BASE_HEIGHT,
                        padding=ft.padding.only(top=30, left=10, right=10, ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container(),
                                ft.Container(
                                    padding=20,
                                    bgcolor='#E6E0C8',
                                    border_radius=10,
                                    content=self.login_box,
                                ),
                            ]
                        )
                    )
                ]
            )
        )

    def password_field_in_focus(self, e):
        self.password_input.bgcolor = 'white'
        self.password_input.border = None
        self.password_input.update()
        self.login_box.update()

    def view_password(self, e):
        is_shown = self.password_input.content.password
        if is_shown:
            self.password_input.content.password = False
            self.view_hide_text.value = 'Hide'
        else:
            self.view_hide_text.value = 'View'
            self.password_input.content.password = True
        self.password_input.content.update()
        self.view_hide_text.update()

    def switch_page(self, e):
        if self.login_input.content.value and self.password_input.content.value:
            self.auth_service.login_user(
                self.login_input.content.value,
                self.password_input.content.value
            )
            if self.auth_service.is_authenticated:
                self.error.visible = False
                self.page.go(MAIN_PAGE_VIEW_URL)
            else:
                self.error.visible = True
            self.login_box.update()
        else:
            self.error.visible = True
            self.login_box.update()

    def user_field_change(self, e):
        if self.password_input.content.value and self.login_input.content.value:
            self.error.visible = False








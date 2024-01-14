from flet import *
from flet import padding

base_height = 900
base_width = 1080
btn_width = 350
btn_height = 50
br = 30
bnt_size = 9
base_color = 'white'
input_fill_color = "#ffffff"
base_green = "#986a46"
light_green = "#d4ad86"
input_hint_color = '#75797c'
content_padding = padding.only(left=20,top=10,right=10,bottom=10)
input_error_bg = "#f8c1bc"
input_error_outline = "#cb1a2a"
img_src ='https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80'


class LoginPage(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.padding = 0
        self.page = page
        self.expand = True
        self.page.bgcolor = 'red'
        self.view_hide_text = Text(
            value='View',
            color=base_color,
            font_family='poppins medium',

        )

        self.password_input = Container(
            height=btn_height,
            bgcolor='white',
            border_radius=10,
            # padding=20,
            content=TextField(
                on_focus=self.password_field_in_focus,
                password=True,
                suffix=Container(
                    on_click=self.view_hide_password,
                    content=self.view_hide_text,
                ),
                hint_text='Password',
                hint_style=TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=input_hint_color,
                ),
                text_style=TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=input_hint_color,
                ),
                border=InputBorder.NONE,
                content_padding=content_padding,
                selection_color=base_green,
                cursor_color=base_color
            )
        )
        self.login_input = Container(
            height=btn_height,
            bgcolor='white',
            border_radius=10,
            # padding=20,
            content=TextField(
                on_focus=self.password_field_in_focus,
                hint_text='Email',
                hint_style=TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=input_hint_color,
                ),
                text_style=TextStyle(
                    size=16,
                    font_family='Poppins Regular',
                    color=input_hint_color,
                ),
                border=InputBorder.NONE,
                content_padding=content_padding,
                selection_color=base_green,
                cursor_color=base_color
            )
        )

        self.error = Row(
            controls=[
                Image(
                    src='assets/icons/danger.png',
                    # scale=0.8,

                ),
                Text(
                    value='Please enter the correct password to login',
                    color='red',
                    font_family='poppins regular'

                )
            ]
        )

        self.login_box = Column(
            width=360,
            controls=[

                Container(height=2),

                self.login_input,
                self.password_input,

                Container(height=1),

                # self.error,

                Container(height=1),

                Container(
                    height=btn_height,
                    width=btn_width,
                    on_click=self.switch_page,
                    bgcolor=base_green,
                    border_radius=10,
                    alignment=alignment.center,
                    content=Text(
                        value='Continue',
                        font_family='Poppins Medium',
                        size=16,

                    )
                ),
                Container(height=5),

                Container(
                    content=Text(
                        value="Forgot your password?",
                        size=14,
                        font_family='poppins medium',
                        color=base_green
                    ),
                ),

                Container(height=5),

            ]
        )
        self.content = Container(
            bgcolor=base_color,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            expand=True,
            content=Stack(
                controls=[
                    Container(
                        border_radius=br,
                        height=base_height,
                        padding=padding.only(top=30, left=10, right=10, ),
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Container(
                                    margin=margin.only(left=20),
                                    content=Text(
                                        value='Login',
                                        color='black',
                                        font_family='SF Pro Bold',
                                        size=30,
                                    ),
                                ),
                                Container(height=2),
                                Container(

                                    padding=20,
                                    # height=550,
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

        y = self.error in self.login_box.controls
        if y == True:
            self.login_box.controls.remove(self.error)
            self.password_input.bgcolor = 'white'
            self.password_input.border = None
            self.password_input.update()
            self.login_box.update()

            # pass

    def view_hide_password(self, e):
        det = self.password_input.content.password
        if det == True:
            self.password_input.content.password = False
            self.view_hide_text.value = 'Hide'
        else:
            self.view_hide_text.value = 'View'
            self.password_input.content.password = True
        self.password_input.content.update()
        self.view_hide_text.update()

    def switch_page(self, e):
        self.page.go('/test')


class Next(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.offset = transform.Offset(0, 0, )
        self.expand = True
        self.view_hide_text = Text(
            value='View',
            color=base_color,
            font_family='poppins medium',

        )
        self.content = Container(
            alignment=alignment.center,
            on_click=lambda _: page.go('/login'),
            height=50, width=150,
            bgcolor='white',
            content=Text(
                value='Get Started',
                size=20,
                color='black'
            )
        )
        self.button = Container(
            height=btn_height,
            width=btn_width,
            on_click=self.back_click,
            bgcolor=base_green,
            border_radius=10,
            alignment=alignment.center,
            content=Text(
                value='Continue',
                font_family='Poppins Medium',
                size=16,

            )
        )


    def back_click(self, e):
        print('sadsad')
        self.page.go('/login')





import flet as ft

# This is the main function that will be executed when the app starts
def main(page: ft.Page):
    # Variables used in the app
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    confirm_password = ft.TextField(label="Confirm password", password=True, can_reveal_password=True)

    # Function to validate the sign in form
    def validate_form_SI(e):
        has_error = False
        # Check username
        if not username.value:
            username.error_text="The username is required"
            has_error=True
        else:
            username.error_text=None
        # Check password
        if not password.value:
            password.error_text="The password is required"
            has_error=True
        else:
            password.error_text=None
        username.update()
        password.update()
        # If there isn't any problem, it goes to forms
        if not has_error:
            page.go("/homepage")

    # Function to validate the sign up form
    def validate_form_SU(e):
        has_error = False
        # Check username
        if not username.value:
            username.error_text="The username is required"
            has_error=True
        else:
            username.error_text=None
        # Check password
        if not password.value:
            password.error_text="The password is required"
            has_error=True
        else:
            password.error_text=None
        # Check confirm password
        if not confirm_password.value:
            confirm_password.error_text="The password is required"
            has_error=True
        elif password.value != confirm_password.value:
            confirm_password.error_text="The passwords don't match"
            has_error=True
        else:
            confirm_password.error_text=None
        username.update()
        password.update()
        confirm_password.update()
        # If there isn't any problem, it goes to forms
        if not has_error:
            page.go("/homepage")

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Sign in"), bgcolor=ft.colors.SURFACE_VARIANT),
                    username,
                    password,
                    ft.ElevatedButton("Sign in", on_click=validate_form_SI),
                    ft.ElevatedButton("I don't have an account", on_click=lambda _: page.go("/signup")),                    
                ],
            )
        )
        if page.route == "/signup":
            page.views.append(
                ft.View(
                    "/signup",
                    [
                        ft.AppBar(title=ft.Text("Sign up"), bgcolor=ft.colors.SURFACE_VARIANT),
                        username,
                        password,
                        confirm_password,
                        ft.ElevatedButton("Sign up", on_click=validate_form_SU),
                        ft.ElevatedButton("I already have an account", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/homepage":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        ft.AppBar(title=ft.Text("Home page"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("This is the home page")
                    ],
                )
            )
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)

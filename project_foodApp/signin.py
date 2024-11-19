# Functional sign in and sign up 
import flet as ft

# This is the main function that will be executed when the app starts
def main(page: ft.Page):
    # Variables used in the app
    icon = ft.Image(
        src=f"/assets/icon.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    # Variables used in the authentication pages
    signup_username = ft.TextField(label="Username")
    signup_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    signup_confirm_password = ft.TextField(label="Confirm password", password=True, can_reveal_password=True)
    signin_username = ft.TextField(label="Username")
    signin_password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    # Variables used in the profile pages
    profile_name = ft.TextField(label="Name")
    profile_email = ft.TextField(label="Email")
    profile_phone = ft.TextField(label="Phone")
    profile_address = ft.TextField(label="Address")
    profile_username = ft.TextField(label="Username")
    profile_password = ft.TextField(label="Password", password=True, can_reveal_password=True)


    # Variables used in the main page




    # Variables used in the restaurant page


    # Variables used in the basket page


    # Function to validate the sign up form
    def signup_validate(e):
        has_error = False
        # Check username
        if not signup_username.value:
            signup_username.error_text="The username is required"
            has_error=True
        else:
            signup_username.error_text=None
        # Check password
        if not signup_password.value:
            signup_password.error_text="The password is required"
            has_error=True
        else:
            signup_password.error_text=None
        # Check confirm password
        if not signup_confirm_password.value:
            signup_confirm_password.error_text="The password is required"
            has_error=True
        elif signup_password.value != signup_confirm_password.value:
            signup_confirm_password.error_text="Passwords don't match"
            has_error=True
        else:
            signup_confirm_password.error_text=None
        signup_username.update()
        signup_password.update()
        signup_confirm_password.update()
        profile_username=signup_username.value
        # If there isn't any problem, it goes to forms
        if not has_error:
            signup_username.value=""
            signup_password.value=""
            signup_confirm_password.value=""
            signup_username.update()
            signup_password.update()
            signup_confirm_password.update()
            page.go("/homepage")

    # Function to validate the sign in form
    def signin_validate(e):
        has_error = False
        # Check username
        if not signin_username.value:
            signin_username.error_text="The username is required"
            has_error=True
        else:
            signin_username.error_text=None
        # Check password
        if not signin_password.value:
            signin_password.error_text="The password is required"
            has_error=True
        else:
            signin_password.error_text=None
        signin_username.update()
        signin_password.update()
        # If there isn't any problem, it goes to forms
        if not has_error:
            signin_username.value=""
            signin_password.value=""
            signin_username.update()
            signin_password.update()
            page.go("/homepage")


    # Function to change the navigation route
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Sign in"), bgcolor=ft.colors.SURFACE_VARIANT),
                    signin_username,
                    signin_password,
                    ft.ElevatedButton("Sign in", on_click=signin_validate),
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
                        ft.Column(controls=[icon], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column([
                            signup_username,
                            signup_password,
                            signup_confirm_password,],
                            alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column(controls=[
                            ft.ElevatedButton("Sign up", on_click=signup_validate),
                            ft.ElevatedButton("I already have an account", on_click=lambda _: page.go("/"))],
                            alignment=ft.MainAxisAlignment.CENTER),
                    ],
                )
            )
        if page.route == "/homepage":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        ft.AppBar(title=ft.Text("Home page"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("This is the home page"),
                    ],
                )
            )
        page.update()
    
    # Function to go back to the previous view
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)

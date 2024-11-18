import flet as ft

# This is the main function that will be executed when the app starts
def main(page: ft.Page):
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

    # Variables for the homepage
    basket = ft.IconButton(ft.icons.SHOPPING_BASKET)
    profile = ft.IconButton(ft.icons.ACCOUNT_CIRCLE)
    leading_avatar = ft.CircleAvatar(
        foreground_image_url="",
        radius=20,
    )

    # Data for the three restaurants
    restaurants = [
        {"name": "Hesburger", "category": "Burger", "image": "https://via.placeholder.com/300x150"}, #I'm displaying a placeholder just to wait untill figuring out the path for the photos in assets
        {"name": "Subway", "category": "Sandwich", "image": "https://via.placeholder.com/300x150"},
        {"name": "Taco Bell", "category": "Tacos", "image": "https://via.placeholder.com/300x150"},
    ]

    # Liste affichant les restaurants
    restaurant_list = ft.Column(spacing=10)

    # Function to filter restaurants
    def filter_restaurants(category):
        if category == "All":
            filtered_restaurants = restaurants
        else:
            filtered_restaurants = [r for r in restaurants if r["category"] == category]
        
        # Clear the current restaurant list and add filtered ones
        restaurant_list.controls.clear()
        for r in filtered_restaurants:
            restaurant_list.controls.append(create_restaurant_container(r["name"], r["image"]))
        page.update()

    # Function to create restaurant container
    def create_restaurant_container(name, image_url):
        return ft.Container(
            content=ft.Text(name, color=ft.colors.WHITE, size=20, weight=ft.FontWeight.BOLD),
            expand=True,
            bgcolor=ft.colors.BLUE_GREY_900,  # Check if they are here
            padding=20,
            border_radius=10,
            alignment=ft.alignment.center,
            image_src=image_url,
            image_fit=ft.ImageFit.COVER,
            height=150,
        )


    #variables used in the profile page


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
                        signup_username,
                        signup_password,
                        signup_confirm_password,
                        ft.Column(controls=[
                            ft.ElevatedButton("Sign up", on_click=signup_validate),
                            ft.ElevatedButton("I already have an account", on_click=lambda _: page.go("/"))],
                            alignment=ft.MainAxisAlignment.CENTER),
                    ],
                )
            )
            
        elif page.route == "/homepage":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        ft.AppBar(
                            leading=leading_avatar,
                            leading_width=40,
                            title=ft.Text("Homepage"),
                            bgcolor=ft.colors.GREEN,
                            center_title=True,
                            actions=[basket, profile],
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("All", on_click=lambda _: filter_restaurants("All")),
                                ft.ElevatedButton("Burger", on_click=lambda _: filter_restaurants("Burger")),
                                ft.ElevatedButton("Sandwich", on_click=lambda _: filter_restaurants("Sandwich")),
                                ft.ElevatedButton("Tacos", on_click=lambda _: filter_restaurants("Tacos")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(
                            content=restaurant_list, expand=True
                        ),
                    ],
                )
            )
            # Show all restaurants by default
            filter_restaurants("All")
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

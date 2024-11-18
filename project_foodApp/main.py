import flet as ft

def main(page: ft.Page):
    # Variables for authentification
    signup_username = ft.TextField(label="Username")
    signup_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    signup_confirm_password = ft.TextField(label="Confirm password", password=True, can_reveal_password=True)
    signin_username = ft.TextField(label="Username")
    signin_password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    # Variables for the homepage
    basket = ft.IconButton(ft.icons.SHOPPING_BASKET)
    profile = ft.IconButton(ft.icons.ACCOUNT_CIRCLE)
    leading_avatar = ft.CircleAvatar(
        foreground_image_url="",
        radius=20,
    )

    # Données pour les trois restaurants
    restaurants = [
        {"name": "Hesburger", "category": "Burger", "image": "assets/Hesburger.jpg"},
        {"name": "Subway", "category": "Sandwich", "image": "assets/Subway.jpg"},
        {"name": "Taco Bell", "category": "Tacos", "image": "assets/Tacos.jpg"},
    ]

    # Liste affichant les restaurants
    restaurant_list = ft.Column(spacing=10)

    # Variables used in the profile pages

    # Variables used in the restaurant page

    # Variables used in the basket page

    # Function to filter the restaurants
    def filter_restaurants(category):
        if category == "All":
            restaurant_list.controls = [
                create_restaurant_container(r["name"], r["image"])
                for r in restaurants
            ]
        else:
            restaurant_list.controls = [
                create_restaurant_container(r["name"], r["image"])
                for r in restaurants
                if r["category"] == category
            ]
        page.update()

    # Fonction pour créer un conteneur pour chaque restaurant
    def create_restaurant_container(name, image_url):
        return ft.Container(
            content=ft.Text(name, color=ft.colors.WHITE, size=20, weight=ft.FontWeight.BOLD),
            expand=True,
            bgcolor=ft.colors.TRANSPARENT,
            padding=20,
            border_radius=10,
            alignment=ft.alignment.center,
            image_src=image_url,
            image_fit=ft.ImageFit.COVER,
            height=150,
            width=300,
        )

    # Function to validate the sign up form
    def signup_validate(e):
        has_error = False
        if not signup_username.value:
            signup_username.error_text = "The username is required"
            has_error = True
        else:
            signup_username.error_text = None
        if not signup_password.value:
            signup_password.error_text = "The password is required"
            has_error = True
        else:
            signup_password.error_text = None
        if signup_password.value != signup_confirm_password.value:
            signup_confirm_password.error_text = "Passwords don't match"
            has_error = True
        else:
            signup_confirm_password.error_text = None

        signup_username.update()
        signup_password.update()
        signup_confirm_password.update()

        if not has_error:
            page.go("/homepage")

    # Function to validate the sign in form
    def signin_validate(e):
        # Check username and password
        if signin_username.value and signin_password.value:
            page.go("/homepage")
        else:
            if not signin_username.value:
                signin_username.error_text = "The username is required"
            if not signin_password.value:
                signin_password.error_text = "The password is required"
            signin_username.update()
            signin_password.update()

    # Gestion des routes
    def route_change(route):
        page.views.clear()

        if page.route == "/":
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

        elif page.route == "/signup":
            page.views.append(
                ft.View(
                    "/signup",
                    [
                        ft.AppBar(title=ft.Text("Sign up"), bgcolor=ft.colors.SURFACE_VARIANT),
                        signup_username,
                        signup_password,
                        signup_confirm_password,
                        ft.ElevatedButton("Sign up", on_click=signup_validate),
                        ft.ElevatedButton("I already have an account", on_click=lambda _: page.go("/")),
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
                                ft.ElevatedButton(
                                    "All", on_click=lambda _: filter_restaurants("All")
                                ),
                                ft.ElevatedButton(
                                    "Burger", on_click=lambda _: filter_restaurants("Burger")
                                ),
                                ft.ElevatedButton(
                                    "Sandwich", on_click=lambda _: filter_restaurants("Sandwich")
                                ),
                                ft.ElevatedButton(
                                    "Tacos", on_click=lambda _: filter_restaurants("Tacos")
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        restaurant_list,
                    ],
                )
            )
            # Affiche tous les restaurants par défaut
            filter_restaurants("All")

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)

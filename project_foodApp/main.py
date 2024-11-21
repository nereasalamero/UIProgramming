import flet as ft

# Create a restaurant class that has types of food, menu, and location
# if easy implement search system for the menu
class Restaurant:
    def __init__(self, type_of_food: str, menu: dict, location: str, rating: float):
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        self.type_of_food = type_of_food
        self.menu = menu  # menu should be a dictionary with the food as the key and the price as the value
        self.location = location # location is a string that indicates where certain restaurant is located
        # possibility for certain restaurants to only have certain locations
        # ex: taco bell only in Helsinki
        # user could select through autoselect
        self.rating = rating
    # def get_menu(self):
    #     return self.menu
    # def get_rating(self):
    #     return self.rating
    # def get_location(self):
    #     return self.location
    # def get_type_of_food(self):
    #     return self.type_of_food
class RestaurantApp:
    def __init__(self, restaurant, page):
        self.restaurant = restaurant
        self.quantities = {item: 0 for item in self.restaurant.menu}
        self.menu_controls = []
        self.quantity_texts = {item: ft.Text(f"0") for item in self.restaurant.menu}
        self.total_quantity_text = ft.Text("Total Quantity: 0")
        self.total_price_text = ft.Text("Total Cost: $0.00")
        self.page = page  # Store the page object for UI updates

    def update_total(self):
        total_quantity = sum(self.quantities.values())
        total_price = sum(self.quantities[item] * price for item, price in self.restaurant.menu.items())
        self.total_quantity_text.value = f"Total Quantity: {total_quantity}"
        self.total_price_text.value = f"Total Price: ${total_price:.2f}"
        self.page.update()  # Update the UI

    def increment_quantity(self, item):
        self.quantities[item] += 1
        self.quantity_texts[item].value = str(self.quantities[item])
        self.update_total()
        self.page.update()

    def decrement_quantity(self, item):
        if self.quantities[item] > 0:
            self.quantities[item] -= 1
            self.quantity_texts[item].value = str(self.quantities[item])
            self.update_total()
            self.page.update()

    def update_menu_controls(self):
        self.menu_controls.clear()
        for item, price in self.restaurant.menu.items():
            self.menu_controls.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{item} - ${price:.2f}"),
                        ft.IconButton(ft.icons.REMOVE, on_click=lambda e, item=item: self.decrement_quantity(item)),
                        self.quantity_texts[item],
                        ft.IconButton(ft.icons.ADD, on_click=lambda e, item=item: self.increment_quantity(item)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    width=300,
                )
            )
        self.page.update()  # Update the UI


# This is the main function that will be executed when the app starts
def main(page: ft.Page):
    # Variables used in the authentication pages
    signup_username = ft.TextField(label="Username")
    signup_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    signup_confirm_password = ft.TextField(label="Confirm password", password=True, can_reveal_password=True)
    signin_username = ft.TextField(label="Username")
    signin_password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    # Variables used in the main page


    # Variables used in the profile pages


    # Variables used in the restaurant page
    hesburger = Restaurant(
        type_of_food="Burgers, Fast Food",
        menu={
            "Hesburger": 5, 
            "Cheeseburger": 6,
            "Fries": 3},
        location="Kuopio",
        rating=4.5
    )
    hes = RestaurantApp(hesburger, page)
    hes.update_menu_controls()

    subway = Restaurant(
        type_of_food="Subs, Fast Food",
        menu={
            "BLT": 5,
            "Meatball Sub": 6,
            "Veggie Delight": 3},
        location="Kuopio",
        rating=4.5
    )
    sub = RestaurantApp(subway, page)
    sub.update_menu_controls()

    tacobell = Restaurant(
        type_of_food="Tacos, Burritos, Fast Food",
        menu={
            "Taco": 5,
            "Burrito": 6,
            "Nachos": 3},
        location="Kuopio",
        rating=4.5
    )
    tb = RestaurantApp(tacobell, page)
    tb.update_menu_controls()

    # update_menu_controls()


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
        if page.route == "/homepage":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        ft.AppBar(title=ft.Text("Home page"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("This is the home page"),
                        ft.ElevatedButton("Hesburger", on_click=lambda _: page.go("/hesburger")),
                        ft.ElevatedButton("Subway", on_click=lambda _: page.go("/subway")),
                        ft.ElevatedButton("Taco Bell", on_click=lambda _: page.go("/tacobell")),
                        # create this button to go to restaurant chooser function that will then append different values depending on restaurant
                    ],
                )
            )
        if page.route == "/hesburger":
            page.views.append(
                ft.View(
                    "/hesburger",
                    [
                        ft.AppBar(title=ft.Text("Hesburger", size=25), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Image(src=" "),
                                    width=150,
                                    height=150,
                                    border_radius=ft.border_radius.all(10),
                                    bgcolor=ft.colors.WHITE,
                                    padding=ft.padding.all(10),
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Hesburger", size=25, weight=ft.FontWeight.BOLD),
                                        ft.Row(
                                            controls=[
                                                ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                ft.Icon(name=ft.icons.STAR_BORDER, color=ft.colors.AMBER_500, size=15),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Text(hesburger.type_of_food, size=15),
                                        ft.Text(hesburger.location, size=15),
                                        hes.total_quantity_text,
                                        hes.total_price_text
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Divider(height=20),
                        ft.Column(
                            controls=[
                                ft.Container(
                                    content=
                                    ft.Text("Menu"),
                                    width=150,
                                    height=50,
                                    bgcolor=ft.colors.SURFACE_VARIANT,
                                    padding=ft.padding.all(10),
                                    alignment=ft.alignment.center,  # Ensure this is a valid alignment value
                                    border_radius=ft.border_radius.all(10),
                                ),
                                ft.Container(
                                    content=
                                    ft.Column(
                                        controls=hes.menu_controls,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ),    
                                # ft.Column(
                                #     controls=[
                                #         ft.Column(
                                #             controls=[
                                #                 ft.Row(
                                #                     controls=[
                                #                         ft.Text(item, size=20),
                                #                         ft.Text(f"{hes_quantities[item]} x {price:.2f} ", size=20),
                                #                     ],
                                #                     alignment=ft.MainAxisAlignment.END,
                                #                 ) for item, price in hesburger.menu.items()
                                #             ],
                                #             alignment=ft.MainAxisAlignment.END,
                                #         ),
                                #         total_quantity_text,
                                #         total_price_text,
                                #     ],
                                #     alignment=ft.MainAxisAlignment.CENTER,
                                # ),
                                ft.ElevatedButton("Go to basket", on_click=lambda _: page.go("/basket")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                )
            )
        if page.route == "/subway":
                page.views.append(
                    ft.View(
                        "/subway",
                        [
                            ft.AppBar(title=ft.Text("Subway", size=25), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src=" "),
                                        width=150,
                                        height=150,
                                        border_radius=ft.border_radius.all(10),
                                        bgcolor=ft.colors.WHITE,
                                        padding=ft.padding.all(10),
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Subway", size=25, weight=ft.FontWeight.BOLD),
                                            ft.Row(
                                                controls=[
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR_BORDER, color=ft.colors.AMBER_500, size=15),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            ft.Text(subway.type_of_food, size=15),
                                            sub.total_quantity_text,
                                            sub.total_price_text
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Divider(height=20),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        content=
                                        ft.Text("Menu"),
                                        width=150,
                                        height=50,
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        padding=ft.padding.all(10),
                                        alignment=ft.alignment.center,  # Ensure this is a valid alignment value
                                        border_radius=ft.border_radius.all(10),
                                    ),
                                    ft.Container(
                                        content=
                                        ft.Column(
                                            controls=sub.menu_controls,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ), 
                                    ft.ElevatedButton("Go to basket", on_click=lambda _: page.go("/basket")),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                    )
                )
        if page.route == "/tacobell":
                page.views.append(
                    ft.View(
                        "/tacobell",
                        [
                            ft.AppBar(title=ft.Text("Tacobell", size=25), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src=" "),
                                        width=150,
                                        height=150,
                                        border_radius=ft.border_radius.all(10),
                                        bgcolor=ft.colors.WHITE,
                                        padding=ft.padding.all(10),
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Tacobell", size=25, weight=ft.FontWeight.BOLD),
                                            ft.Row(
                                                controls=[
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15),
                                                    ft.Icon(name=ft.icons.STAR_BORDER, color=ft.colors.AMBER_500, size=15),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            ft.Text("Tacos, Burritos, Fast Food", size=15),
                                            tb.total_quantity_text,
                                            tb.total_price_text
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Divider(height=20),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        content=
                                        ft.Text("Menu"),
                                        width=150,
                                        height=50,
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        padding=ft.padding.all(10),
                                        alignment=ft.alignment.center,  # Ensure this is a valid alignment value
                                        border_radius=ft.border_radius.all(10),
                                    ),
                                    ft.Container(
                                        content=
                                        ft.Column(
                                            controls=tb.menu_controls,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ), 
                                    ft.ElevatedButton("Go to basket", on_click=lambda _: page.go("/basket")),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
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

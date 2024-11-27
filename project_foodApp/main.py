import flet as ft

# Create a restaurant class that has types of food, menu, and location
# if easy implement search system for the menu
class Restaurant:
    def __init__(self, type_of_food: str, menu: dict, location: str, rating: float):
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        self.type_of_food = type_of_food
        self.menu = menu            # menu should be a dictionary with the food as the key and the price as the value
        self.location = location    # location is a string that indicates where certain restaurant is located
        self.rating = rating

# Create a class that will be used to manage the restaurant app
class RestaurantApp:
    def __init__(self, restaurant, page):
        self.restaurant = restaurant
        self.quantities = {item: 0 for item in self.restaurant.menu}
        self.menu_controls = []
        self.quantity_texts = {item: ft.Text(f"0") for item in self.restaurant.menu}
        self.total_quantity = 0
        self.total_price = 0
        self.total_quantity_text = ft.Text(f"Total Quantity: {self.total_quantity}")
        self.total_price_text = ft.Text(f"Total Cost: {self.total_price:.2f} €")
        self.basket_items = []
        self.page = page  # Store the page object for UI updates

    # Function to update the total quantity and price
    def update_total(self):
        self.total_quantity = sum(self.quantities.values())
        self.total_price = sum(self.quantities[item] * price for item, price in self.restaurant.menu.items())
        self.total_quantity_text.value = f"Total Quantity: {self.total_quantity}"
        self.total_price_text.value = f"Total Price: {self.total_price:.2f} €"
        self.page.update()  # Update the UI

    # Function to increment the quantity of an item
    def increment_quantity(self, item):
        self.quantities[item] += 1
        self.quantity_texts[item].value = str(self.quantities[item])
        self.update_total()
        self.page.update()

    # Function to decrement the quantity of an item
    def decrement_quantity(self, item):
        if self.quantities[item] > 0:
            self.quantities[item] -= 1
            self.quantity_texts[item].value = str(self.quantities[item])
            self.update_total()
            self.page.update()

    # Function to update the menu controls
    def update_menu_controls(self):
        self.menu_controls.clear()
        for item, price in self.restaurant.menu.items():
            self.menu_controls.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{item} - {price:.2f} €"),
                        ft.IconButton(ft.icons.REMOVE, on_click=lambda e, item=item: self.decrement_quantity(item)),
                        self.quantity_texts[item],
                        ft.IconButton(ft.icons.ADD, on_click=lambda e, item=item: self.increment_quantity(item)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    width=300,
                )
            )
        self.page.update()  # Update the UI

    # Function to delete the order
    def delete_order(self):
        self.quantities = {item: 0 for item in self.restaurant.menu}
        for item in self.restaurant.menu:
            self.quantity_texts[item].value = "0"
        self.update_total()
        self.page.update()


# This is the main function that will be executed when the app starts
def main(page: ft.Page):
    background_color = '#E5FFC0'
    page.bgcolor = background_color

    # Variables used in the authentication pages
    signup_username = ft.TextField(label="Username")
    signup_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    signup_confirm_password = ft.TextField(label="Confirm password", password=True, can_reveal_password=True)

    signin_username = ft.TextField(label="Username")
    signin_password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    # Variables used in the profile pages
    profile_name = ft.TextField(label="Name")
    profile_email = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL)
    profile_phone = ft.TextField(label="Phone", keyboard_type=ft.KeyboardType.PHONE)
    profile_address = ft.TextField(label="Address", keyboard_type=ft.KeyboardType.STREET_ADDRESS)
    profile_username = ft.TextField(label="Username")
    profile_password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    # Function to change the theme
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        profile_theme.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()
    page.theme_mode = ft.ThemeMode.LIGHT
    profile_theme = ft.Switch(label="Light theme", on_change=theme_changed)

    # Variables for the homepage
    basket = ft.IconButton(ft.icons.SHOPPING_BASKET, on_click=lambda _: page.go("/basket"))
    profile = ft.IconButton(ft.icons.ACCOUNT_CIRCLE, on_click=lambda _: page.go("/profile"))
    home = ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go("/homepage"))
    leading_avatar = ft.Image(
        src="https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/icon.png",
        width=30,
        height=30,
    )

    # Data for the three restaurants
    restaurants = [
        {"name": "Hesburger", "category": "Burger", "image": "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/hesburger.png", "page": "hesburger"},
        {"name": "Subway", "category": "Sandwich", "image": "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/subway.png", "page": "subway"},
        {"name": "Taco Bell", "category": "Tacos", "image": "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/tacobell.png", "page": "tacobell"},
        {"name": "McDonalds", "category": "Burger", "image": "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/mcdonalds.png", "page": "mcdonalds"},
        {"name": "Pizza Hut", "category": "Pizza", "image": "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/pizzahut.png", "page": "pizzahut"},
    ]

    # List showing the restaurants
    restaurant_list = ft.Column(spacing=10, scroll=True)

    # Variables used in the restaurant page
    # Create a Hesburger restaurant
    hesburger = Restaurant(
        type_of_food="Burgers, Fast Food",
        menu={
            "Hesburger": 5, 
            "Cheeseburger": 6,
            "Fries": 3},
        location="Kuopio",
        rating=4
    )
    hes = RestaurantApp(hesburger, page)
    hes.update_menu_controls()

    # Create a Subway restaurant
    subway = Restaurant(
        type_of_food="Subs, Fast Food",
        menu={
            "BLT": 5,
            "Meatball Sub": 6,
            "Veggie Delight": 3},
        location="Kuopio",
        rating=4
    )
    sub = RestaurantApp(subway, page)
    sub.update_menu_controls()

    # Create a Taco Bell restaurant
    tacobell = Restaurant(
        type_of_food="Tacos, Burritos, Fast Food",
        menu={
            "Taco": 5,
            "Burrito": 6,
            "Nachos": 3,
            "Crunchwrap": 5
            },
        location="Kuopio",
        rating=5
    )
    tb = RestaurantApp(tacobell, page)
    tb.update_menu_controls()

    # Create a McDonalds restaurant
    mcdonalds = Restaurant(
        type_of_food="Fast Food",
        menu={
            "Big Mac": 5,
            "10 Piece": 4,
            "Mcflurry": 3
        },
        location="Kuopio",
        rating = 4.5
    )
    mc = RestaurantApp(mcdonalds, page)
    mc.update_menu_controls()

    # Create a Pizza Hut restaurant
    pizzahut = Restaurant(
        type_of_food="Pizza, Fast Food",
        menu={
            "Pepperoni": 5,
            "Hawaiian": 6,
            "Margherita": 3
        },
        location="Kuopio",
        rating=4
    )
    ph = RestaurantApp(pizzahut, page)
    ph.update_menu_controls()

    # Variables used in the basket page (functions used for placing an order)
    def close_dlg(e):
        alert_place_order.open = False
        e.control.page.update()

    def open_dlg(e):
        e.control.page.overlay.append(dlg_confirm)
        dlg_confirm.open = True
        e.control.page.update()
        
    alert_place_order = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to place your order?"),
        actions=[
            ft.TextButton("Yes", on_click=open_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    dlg_confirm = ft.AlertDialog(
        title=ft.Text("Your order is on its way!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    # Function to place an order
    def place_order(e):
        e.control.page.overlay.append(alert_place_order)
        alert_place_order.open = True
        e.control.page.update()
    
    # Function to filter restaurants
    def filter_restaurants(category):
        if category == "All":
            filtered_restaurants = restaurants
        else:
            filtered_restaurants = [r for r in restaurants if r["category"] == category]

        # Clear the current restaurant list and add filtered ones
        restaurant_list.controls.clear()
        for r in filtered_restaurants:
            restaurant_list.controls.append(create_restaurant_container(r["name"], r["image"], r["page"]))
        page.update()

    # Function to create restaurant container
    def create_restaurant_container(name, image_url, link):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=image_url, width=page.width, height=100, fit=ft.ImageFit.COVER, expand=True),                     # Image here
                    ft.Text(name, color=ft.colors.BLACK, size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),      # Text below
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
            padding=20,
            bgcolor=ft.colors.GREY_200,
            border_radius=10,
            on_click=lambda _: page.go(f"/{link}"),  # Change to restaurant type or ID
        )

    # Function to validate the sign-up form
    def signup_validate(e):
        has_error = False
        # Check username
        if not signup_username.value:
            signup_username.error_text = "The username is required"
            has_error = True
        else:
            signup_username.error_text = None
        # Check password
        if not signup_password.value:
            signup_password.error_text = "The password is required"
            has_error = True
        else:
            signup_password.error_text = None
        # Check confirm password
        if not signup_confirm_password.value:
            signup_confirm_password.error_text = "The password is required"
            has_error = True
        elif signup_password.value != signup_confirm_password.value:
            signup_confirm_password.error_text = "Passwords don't match"
            has_error = True
        else:
            signup_confirm_password.error_text = None
        
        # Check password length
        if len(signup_password.value) < 8:
            signup_password.error_text = "The password must be at least 8 characters long"
            has_error = True
        else:
            signup_password.error_text = None
        
        # Update controls only after they are part of the UI
        signup_username.update()
        signup_password.update()
        signup_confirm_password.update()
        # If there isn't any problem, clear inputs and navigate to the homepage
        if not has_error:
            profile_username.value = signup_username.value
            signup_username.value = ""
            signup_password.value = ""
            signup_confirm_password.value = ""
            signup_username.update()
            signup_password.update()
            signup_confirm_password.update()
            page.go("/homepage")

    # Function to validate the sign-in form
    def signin_validate(e):
        has_error = False
        # Check username
        if not signin_username.value:
            signin_username.error_text = "The username is required"
            has_error = True
        else:
            signin_username.error_text = None

        # Check password
        if not signin_password.value:
            signin_password.error_text = "The password is required"
            has_error = True
        else:
            signin_password.error_text = None

        # Check password length
        if len(signin_password.value) < 8:
            signin_password.error_text = "The password must be at least 8 characters long"
            has_error = True
        else:
            signin_password.error_text = None

        # Update controls while they are still part of the view
        signin_username.update()
        signin_password.update()

        if not has_error:
            profile_username.value = signin_username.value
            # Clear input fields before navigating
            signin_username.value = ""
            signin_password.value = ""
            signin_username.error_text = None
            signin_password.error_text = None
            signin_username.update()
            signin_password.update()

            # Navigate to the homepage
            page.go("/homepage")

    # Function to create the restaurant page    
    def restaurant_page(page, route, name, image_src, type_of_food, location, total_quantity_text, total_price_text, menu_controls, rating):
        return ft.View(
            route,
            [
                ft.AppBar(
                    leading=leading_avatar,
                    leading_width=40,
                    bgcolor=background_color,
                    center_title=True,
                    actions=[home, basket, profile],
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Image(src=image_src),  # Imagen del restaurante
                            width=150,
                            height=150,
                            border_radius=ft.border_radius.all(10),
                            bgcolor=ft.colors.WHITE,
                            padding=ft.padding.all(10),
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(name, size=25, weight=ft.FontWeight.BOLD),  # Restaurant name
                                print_stars(rating),            # Stars
                                ft.Text(type_of_food, size=15), # Type of food
                                ft.Text(location, size=15),     # Location
                                total_quantity_text,            # Total quantity
                                total_price_text                # Total price
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
                            content=ft.Text("Menu"),
                            width=150,
                            height=50,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            padding=ft.padding.all(10),
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=menu_controls,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Keep shopping", on_click=lambda _: page.go("/homepage")),
                                ft.ElevatedButton("Go to basket", on_click=lambda _: page.go("/basket")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,

                ),
            ],
        )

    #Function to automatize the stars
    def print_stars(rating):
        stars = []
        full_stars = int(rating)
        half_star = rating - full_stars >= 0.5
        for _ in range(full_stars):
            stars.append(ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_500, size=15))
        if half_star:
            stars.append(ft.Icon(name=ft.icons.STAR_HALF, color=ft.colors.AMBER_500, size=15))
        for _ in range(5 - len(stars)):
            stars.append(ft.Icon(name=ft.icons.STAR_BORDER, color=ft.colors.AMBER_500, size=15))
        return ft.Row(controls=stars, alignment=ft.MainAxisAlignment.CENTER)

    # Function to show the basket page, including the items the user has added
    def show_basket():
        basket_total_quantity = (hes.total_quantity + sub.total_quantity + tb.total_quantity)
        basket_total_price = (hes.total_price + sub.total_price + tb.total_price)
        return ft.View(
            "/basket",
            [
                ft.AppBar(
                    title=ft.Text("Basket"),
                    leading=leading_avatar,
                    leading_width=40,
                    bgcolor=background_color,
                    center_title=True,
                    actions=[home, profile],
                ),
                ft.Column([
                    ft.Column([
                        ft.Container(
                            content=ft.Row([
                                    ft.Text("Hesburger", size=25, width=200),
                                    ft.Column(
                                        controls=[
                                            ft.Text(f"Quantity: {hes.total_quantity} items", size=15),
                                            ft.Text(f"Price: {hes.total_price:.2f} €", size=15),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        width=400,
                                    ),
                                    ft.ElevatedButton("Delete order", on_click=lambda _: delete_order_res(hes)),
                                ],),
                            padding=10,  # Add padding inside the container
                            margin=ft.margin.only(bottom=15),  # Add space below the section
                            border_radius=ft.border_radius.all(8),  # Optional: Rounded corners
                        ),

                        ft.Container(
                            content=ft.Row([
                                ft.Text("Subway", size=25, width=200),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"Quantity: {sub.total_quantity} items", size=15),
                                        ft.Text(f"Price: {sub.total_price:.2f} €", size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    width=400,
                                ),
                                ft.ElevatedButton("Delete order", on_click=lambda _: delete_order_res(sub)),
                            ],),
                            padding=10,
                            margin=ft.margin.only(bottom=15),
                            border_radius=ft.border_radius.all(8),
                        ),

                        ft.Container(
                            content=ft.Row([
                                ft.Text("Taco Bell", size=25, width=200),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"Quantity: {tb.total_quantity} items", size=15),
                                        ft.Text(f"Price: {tb.total_price:.2f} €", size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    width=400,
                                ),
                                ft.ElevatedButton("Delete order", on_click=lambda _: delete_order_res(tb)),
                            ],),
                            padding=10,
                            margin=ft.margin.only(bottom=15),
                            border_radius=ft.border_radius.all(8),
                        ),

                        ft.Container(
                            content=ft.Row([
                                ft.Text("McDonalds", size=25, width=200),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"Quantity: {mc.total_quantity} items", size=15),
                                        ft.Text(f"Price: {mc.total_price:.2f} €", size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    width=400,
                                ),
                                ft.ElevatedButton("Delete order", on_click=lambda _: delete_order_res(mc)),
                            ],),
                            padding=10,
                            margin=ft.margin.only(bottom=15),
                            border_radius=ft.border_radius.all(8),
                        ),

                        ft.Container(
                            content=ft.Row([
                                ft.Text("Pizza Hut", size=25, width=200),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"Quantity: {ph.total_quantity} items", size=15),
                                        ft.Text(f"Price: {ph.total_price:.2f} €", size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    width=400,
                                ),
                                ft.ElevatedButton("Delete order", on_click=lambda _: delete_order_res(ph)),
                            ],),
                            padding=10,
                            margin=ft.margin.only(bottom=15),
                            border_radius=ft.border_radius.all(8),
                        ),],
                        alignment=ft.MainAxisAlignment.START,
                        scroll=True,
                    ),
                    ft.Divider(height=10),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("Place order", on_click=lambda e: place_order(e)),
                            ft.Text("Total:", size=15),
                            ft.Text(f"{basket_total_quantity} items", size=15),
                            ft.Text(f"{basket_total_price:.2f} €", size=15),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                    ft.Divider(height=10),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    scroll=True,
                ),
            ],
        )
       

    # Function to delete the order
    def delete_order_res(restaurant: RestaurantApp):
        restaurant.delete_order()
        # Re-render the basket page
        page.views[-1] = show_basket()  # Replace the current view with the updated basket
        page.update()
    
    # Function to change the navigation route
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Sign in"), bgcolor=background_color, center_title=True),
                    ft.Container(
                        content=
                            ft.Column(
                                controls=[
                                    ft.Image(
                                        src="https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/icon.png",
                                        width=250,
                                        height=250,
                                    ),
                                    ft.Text("Welcome to GustoGo!", size=20),
                                    signin_username,
                                    signin_password,
                                    ft.ElevatedButton("Sign in", on_click=signin_validate),
                                    ft.ElevatedButton("I don't have an account", on_click=lambda _: page.go("/signup")),
                                ], 
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            expand=True,
                    ),
                ],
            )
        )

        if page.route == "/signup":
            page.views.append(
                ft.View(
                    "/signup",
                    [
                        ft.AppBar(title=ft.Text("Sign up"), bgcolor=background_color, center_title=True),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        src="https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/icon.png",
                                        width=250,
                                        height=250,
                                    ),
                                    ft.Text("Welcome to GustoGo!", size=20),
                                    signup_username,
                                    signup_password,
                                    signup_confirm_password,
                                    ft.ElevatedButton("Sign up", on_click=signup_validate),
                                    ft.ElevatedButton("I already have an account", on_click=lambda _: page.go("/")),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            expand=True,
                        ),
                    ],
                )
            ),

        if page.route == "/homepage":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        ft.AppBar(
                            leading=leading_avatar,
                            leading_width=40,
                            title=ft.Text("Homepage"),
                            bgcolor=background_color,
                            center_title=True,
                            actions=[home, basket, profile],
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("All", on_click=lambda _: filter_restaurants("All")),
                                ft.ElevatedButton("Burger", on_click=lambda _: filter_restaurants("Burger")),
                                ft.ElevatedButton("Sandwich", on_click=lambda _: filter_restaurants("Sandwich")),
                                ft.ElevatedButton("Tacos", on_click=lambda _: filter_restaurants("Tacos")),
                                ft.ElevatedButton("Pizza", on_click=lambda _: filter_restaurants("Pizza")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(
                            content=restaurant_list, expand=True,
                        ),
                    ],
                )
            )
            # Show all restaurants by default
            filter_restaurants("All")

        if page.route == "/basket":
            page.views.append(
                show_basket(),
            )

        if page.route == "/profile":
            page.views.append(
                ft.View(
                    "/profile",
                    [
                        ft.AppBar(
                            leading=leading_avatar,
                            leading_width=40,
                            title=ft.Text("Profile"),
                            bgcolor=background_color,
                            center_title=True,
                            actions=[home, basket],
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Image(
                                    src="https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/profilepic.jpg",
                                    width=250,
                                    height=250,
                                ),
                                ft.Column(  
                                    controls=[
                                        ft.Text(f"Welcome, {profile_username.value}", size=20),
                                        ft.Text(f"Name: {profile_name.value}", size=15),
                                        ft.Text(f"Email: {profile_email.value}", size=15),
                                        ft.Text(f"Phone: {profile_phone.value}", size=15),
                                        ft.Text(f"Address: {profile_address.value}", size=15),
                                        ft.Text(f"Dark mode: {profile_theme.value}", size=15),
                                        ft.ElevatedButton("Edit profile", on_click=lambda _: page.go("/editprofile")),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER, 
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                ),
                            ],),
                            expand=True,
                        ),
                    ],
                )
            )
        if page.route == "/editprofile":
            page.views.append(
                ft.View(
                    "/editprofile",
                    [
                        ft.AppBar(
                            leading=leading_avatar,
                            leading_width=40,
                            title=ft.Text("Edit profile"),
                            bgcolor=background_color,
                            center_title=True,
                            actions=[home, basket, profile],
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("This is my profile page", size=20),
                                    profile_name,
                                    profile_email,
                                    ft.Row(
                                        controls=[
                                            ft.Dropdown(
                                                label="Country",
                                                options=[
                                                    ft.dropdown.Option("(FI) +358"),
                                                    ft.dropdown.Option("(FR) +33"),
                                                    ft.dropdown.Option("(SP) +34"),
                                                    ft.dropdown.Option("(UK) +44"),                                                
                                                ],
                                                on_change=lambda e: print(e),
                                                width=200,
                                            ),
                                            profile_phone,
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                    ),
                                    profile_address,
                                    profile_password,
                                    profile_theme,
                                    ft.ElevatedButton("Save changes", on_click=lambda _: page.go("/profile")),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER, 
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                            expand=True,
                        ),
                    ],
                )
            )
        if page.route == "/hesburger":
            page.views.append(
                restaurant_page(
                    page,
                    "/hesburger",
                    "Hesburger",
                    "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/hesburger.png",
                    hesburger.type_of_food,
                    hesburger.location,
                    hes.total_quantity_text,
                    hes.total_price_text,
                    hes.menu_controls,
                    hesburger.rating,
                )
            )
        if page.route == "/subway":
            page.views.append(
                restaurant_page(
                    page,
                    "/subway",
                    "Subway",
                    "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/subway.png",
                    subway.type_of_food,
                    subway.location,
                    sub.total_quantity_text,
                    sub.total_price_text,
                    sub.menu_controls,
                    subway.rating,
                )
            )
        if page.route == "/tacobell":
            page.views.append(
                restaurant_page(
                    page,
                    "/tacobell",
                    "Tacobell",
                    "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/tacobell.png",
                    tacobell.type_of_food,
                    tacobell.location,
                    tb.total_quantity_text,
                    tb.total_price_text,
                    tb.menu_controls,
                    tacobell.rating,
                )
            )
        if page.route == "/mcdonalds":
            page.views.append(
                restaurant_page(
                    page,
                    "/mcdonalds",
                    "McDonalds",
                    "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/mcdonalds.png",
                    mcdonalds.type_of_food,
                    mcdonalds.location,
                    mc.total_quantity_text,
                    mc.total_price_text,
                    mc.menu_controls,
                    mcdonalds.rating,
                )
            )
        if page.route == "/pizzahut":
            page.views.append(
                restaurant_page(
                    page,
                    "/pizzahut",
                    "Pizza Hut",
                    "https://raw.githubusercontent.com/nereasalamero/UIProgramming/main/project_foodApp/assets/pizzahut.png",
                    pizzahut.type_of_food,
                    pizzahut.location,
                    ph.total_quantity_text,
                    ph.total_price_text,
                    ph.menu_controls,
                    pizzahut.rating,
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

from django_components import Component, register


@register("navbar")
class NavBar(Component):
    template_name = "navbar.html"

    def get_context_data(
        self,
        title,
        menu_items,
        login_url=None,
        login_text="Connexion",
        logout_url=None,
        logout_text="Déconnexion",
    ):
        return {
            "title": title,
            "menu_items": menu_items,
            "login_url": login_url,
            "login_text": login_text,
            "logout_url": logout_url,
            "logout_text": logout_text,
        }

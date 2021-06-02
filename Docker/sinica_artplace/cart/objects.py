from django.conf import settings
from django.db.models import Model

from api.models import *

import json
from collections import OrderedDict


SESSION_CART_KEY = settings.SESSION_CART_KEY


class Cart:
    def __init__(self, request, model: Model):
        self.model = model
        
        self.session = request.session
        cart = self.session.get(SESSION_CART_KEY)
        if not cart:
            cart = {}
            self.session[SESSION_CART_KEY] = cart
        self.cart = cart

    def __iter__(self) -> dict:
        articul_list = self.session[SESSION_CART_KEY].keys()
        articul_list = [int(a) for a in articul_list]
        query = self.model.objects.filter(articul__in=articul_list)

        for item in query:
            item.quantity = self.session[SESSION_CART_KEY][str(item.articul)]
            yield item

    def __len__(self):
        return sum([int(quantity) for quantity in self.session[SESSION_CART_KEY].values()])

    def add(self, articul, quantity=1):                         #TODO добавить проверку на articul
        articul = str(articul)
        item = self.cart.get(articul)

        if item:
            item_quantity = int(item)
            self.cart[articul] += item_quantity
        else:
            self.cart[articul] = quantity

        self.session[SESSION_CART_KEY] = self.cart
        print(self.session[SESSION_CART_KEY])
        self.save()

    def delete(self, articul, del_quantity:int=None):
        if del_quantity is not None:
            quantity = int(self.cart[articul]) - del_quantity
            if quantity == 0:
                self.cart.pop(str(articul))
            else:
                self.cart[articul] = quantity             #TODO добавить проверки на присланные значения
        else:
            self.cart.pop(str(articul))
        
        self.session[SESSION_CART_KEY] = self.cart
        self.save()
    
    def save(self):
        self.session.modified = True
    
    def clear(self):
        self.cart = {}
        self.session[SESSION_CART_KEY] = self.cart
        self.save()            

    def get_json_cart(self) -> str:
        """Return str json formatted
        {"length": int, "articul_list": [{"articul: int": "quantity: int"}, {...}, ]}
        """
        return {'length': len(self), 'articul_list': [item for item in self.cart.items()]}

    # def get_total_price(self):          TODO допилить функцию
    #     return sum([price * quantity for price, quantity in self.session[SESSION_CART_KEY].items()])
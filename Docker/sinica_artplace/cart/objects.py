from django.conf import settings
from django.db.models import Model

from api.models import *

import json
from collections import OrderedDict


SESSION_CART_KEY = settings.SESSION_CART_KEY


class CartException(Exception):
    pass


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
        return sum([int(quantity['quantity']) for quantity in self.session[SESSION_CART_KEY].values()])

    def get_total_price(self):
        cost = 0
        for v in self.cart.values():
            price, quantity = int(v['price']), int(v['quantity'])
            cost += price * quantity
        return cost

    def add(self, articul:str, price:int, quantity:int=1):
        try:
            articul = str(articul)
            quantity = int(quantity)
            price = int(price)
        except (ValueError, TypeError) as exc:
            raise CartException(exc)

        if quantity < 0:
            raise CartException('Quantity must be non-negative.')
        if price < 0:
            raise CartException('Price must be non-negative.')

        item = self.cart.get(articul)

        if item:
            self.cart[articul]['quantity'] += quantity
        else:
            self.cart[articul] = {'quantity': quantity, 'price': price}

        self.session[SESSION_CART_KEY] = self.cart
        self.save()

    def delete(self, articul:str, del_quantity=None):
        if del_quantity is None:
            self.cart.pop(str(articul))
        else:
            try:
                articul = str(articul)
                del_quantity = int(del_quantity)
            except (ValueError, TypeError) as exc:
                raise CartException(exc)

            if del_quantity < 0:
                raise CartException('Quantity must be non-negative.')

            quantity = int(self.cart[articul]['quantity']) - del_quantity
            if quantity == 0:
                self.cart.pop(str(articul))
            else:
                self.cart[articul]['quantity'] = quantity
        
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
        return {'length': len(self), 'total_price': self.get_total_price(), 'articul_list': [item for item in self.cart.items()]}

    # def get_total_price(self):          TODO допилить функцию
    #     return sum([price * quantity for price, quantity in self.session[SESSION_CART_KEY].items()])
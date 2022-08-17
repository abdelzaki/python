"""
Decouple creation from representation
it creats the object in multiple steps not in a single step like factory
builder : create different parts of complex item 
director : control building process using builder instance 
it consists of director which uses the builder to build the object 
"""


def builderEasy():
    class Product:
        def __init__(self, name) -> None:
            self.name = name
            self.price: int = None
            self.weight: int = None
            self.owner: str = None

    class BuilderOfProduct:
        """the builder which has the ability to build the product according to the data which is provided by the director"""

        def __init__(self) -> None:
            self.product: Product = Product("computer")

        def configurePrice(self, price: int):
            self.product.price = price
            return self

        def configureWeight(self, weight: int):
            self.product.weight = weight
            return self

        def configureOwner(self, owner: str):
            self.product.owner = owner
            return self

    class Director:
        def __init__(self) -> None:
            self.builder: BuilderOfProduct = BuilderOfProduct()

        def construct(self, price: int, weight: int, owner: str):
            self.builder.configureOwner(owner).configurePrice(price).configureWeight(weight)

        @property
        def product(self):
            return self.builder.product

    director = Director()
    director.construct(1, 22, "apple")
    print(director.product.weight)


builderEasy()

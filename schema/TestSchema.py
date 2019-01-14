from mongoengine import *

class Testdata(Document):
    tags = StringField()
    num = IntField()
    longnum = LongField()
    url = URLField()
    email = EmailField()
    float = FloatField()
    decimals = DecimalField()
    boolean = BooleanField()
    date = DateTimeField()
    dynamic = DynamicField()
    listfield = ListField()
    dictfield = DictField()
    image = ImageField()
    objId = ObjectIdField()

from mongoengine import *
"""
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()
"""

#connect('tumblelog')

"""
ross = User(email='ross@example.com')
ross.first_name = 'Ross'
ross.last_name = 'Lawley'
ross.save()
"""

#s = User.objects(id='579031d52c28c02ae81bb171').count() #ObjectId("579031d52c28c02ae81bb171")
#print s
'''
class User(DynamicDocument):
    id = StringField(primary_key=True)
'''

class User2(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

connect("test")
#u = User.objects(id="a2bd4800-02ef-408b-a570-e04fa0454550").count() #"a2bd4800-02ef-408b-a570-e04fa0454550"
#print u

u = User2()
u.first_name = str(5)
u.last_name = 55
u.email = "555@555.com"
u.save()
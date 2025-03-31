from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
from config import graph

class User(GraphObject):
    __primarykey__ = "email"

    email = Property()
    name = Property()
    created_at = Property()

    created_posts = RelatedTo("Post", "CREATED")
    friends = RelatedTo("User", "FRIENDS_WITH")

class Post(GraphObject):
    __primarykey__ = "title"

    title = Property()
    content = Property()
    created_at = Property()

    creator = RelatedFrom("User", "CREATED")
    comments = RelatedTo("Comment", "HAS_COMMENT")
    liked_by = RelatedFrom("User", "LIKES")

class Comment(GraphObject):
    __primarykey__ = "content"

    content = Property()
    created_at = Property()

    creator = RelatedFrom("User", "CREATED")
    post = RelatedFrom("Post", "HAS_COMMENT")
    liked_by = RelatedFrom("User", "LIKES")

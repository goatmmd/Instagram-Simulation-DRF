# Instagram Clone (Django Rest API)

# Endpoints
### User(JWT):
    - api/auth/token/                                   - Retrieve
    - api/auth/token/refresh/                           - Retrieve
### Content:
    - content/tag/list/                                           - List
    - content/tag/<int:pk>/                                       - Retrieve
    - content/post/<int:pk>/                                      - Retrieve
    - content/user/<str:username>/posts/                          - List
    - content/user/<str:username>/posts/<int:pk>/                 - Retrieve
    - content/user/<str:username>/posts/<int:pk>/get_like_list    - List
### Activity:
    - activity/comment/<int:pk>/add/                 - Create
    - activity/comment/retrieve/<int:pk>/            - Retrieve
    - activity/comment/delete/<int:pk>/              - Delete


class UserChoice:

    user_admin = 'user_admin'
    maintainence = 'maintainence'
    moderator = 'moderator'
    normal_user = 'normal_user'


    TYPE_CHOICES = (
        (user_admin, "User Administrator"),
        (maintainence, "Maintainence Administrator"),
        (moderator, "Moderator"),
        (normal_user, "Normal User")
    )

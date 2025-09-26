from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileView, ProfileUpdateView


urlpatterns = [
    # registrácia
    path("signup/", SignUpView.as_view(), name="signup"),

    # login/logout (vstavané views)
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # zmena hesla (po prihlásení)
    path("password-change/", auth_views.PasswordChangeView.as_view(template_name="mailing/password_change_form.html"), name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="mailing/password_change_done.html"), name="password_change_done"),

    # reset hesla (cez email)
    path("password-reset/", auth_views.PasswordResetView.as_view(
            template_name="mailing/password_reset_form.html",
            email_template_name="mailing/password_reset_email.txt"
        ), 
        name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="mailing/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="mailing/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="mailing/password_reset_complete.html"), name="password_reset_complete"),

    # profil
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]
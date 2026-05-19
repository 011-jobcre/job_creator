from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import (
    HomeView,
    AboutView,
    ServicesView,
    RegisterView,
    HiringContactView,
    InquiryView,
    InquiryThanksView,
    GroupView,
    PrivacyView,
    TermsofuseView,
    # chubunrui_options,
    # shobunrui_options,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("rosetta/", include("rosetta.urls")),
]

urlpatterns += i18n_patterns(
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("services/", ServicesView.as_view(), name="services"),
    path("register/", RegisterView.as_view(), name="register"),
    path("hiring-contact/", HiringContactView.as_view(), name="hiring-contact"),
    path("inquiry/", InquiryView.as_view(), name="inquiry"),
    path("inquiry/thanks/", InquiryThanksView.as_view(), name="inquiry-thanks"),
    path("group/", GroupView.as_view(), name="group"),
    path("privacy-policy/", PrivacyView.as_view(), name="privacy-policy"),
    path("terms-of-use/", TermsofuseView.as_view(), name="terms-of-use"),
    # path("api/chubunrui-options/", chubunrui_options, name="chubunrui-options"),
    # path("api/shobunrui-options/", shobunrui_options, name="shobunrui-options"),
)

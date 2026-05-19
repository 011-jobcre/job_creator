from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

# from .models import Chubunrui, Shobunrui
# from .forms import InquiryForm


class HomeView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ServicesView(TemplateView):
    template_name = "services.html"


class RegisterView(TemplateView):
    template_name = "register.html"


class HiringContactView(TemplateView):
    template_name = "hiring_contact.html"


class InquiryView(FormView):
    template_name = "inquiry.html"
    # form_class = InquiryForm
    # success_url = reverse_lazy("inquiry-thanks")

    # def form_valid(self, form):
    #     self.send_inquiry_email(form.cleaned_data)
    #     return super().form_valid(form)

    # def send_inquiry_email(self, data):
    #     subject = "【e-tac】お問い合わせが送信されました"
    #     message = "\n".join(
    #         [
    #             "お問い合わせフォームから以下の内容が送信されました。",
    #             "",
    #             f"会社名: {data['company_name']}",
    #             f"業務分類 大分類: {data['daibunrui']}",
    #             f"業務分類 中分類: {data['chubunrui']}",
    #             f"業務分類 小分類: {data['shobunrui']}",
    #             f"所属: {data['position']}",
    #             f"担当者名: {data['contact_name']}",
    #             "",
    #             "お問い合わせ内容:",
    #             data["inquiry_content"],
    #         ]
    #     )

    #     send_mail(
    #         subject,
    #         message,
    #         settings.INQUIRY_FROM_EMAIL,
    #         [settings.INQUIRY_TO_EMAIL],
    #         fail_silently=False,
    #     )


class InquiryThanksView(TemplateView):
    template_name = "inquiry_thanks.html"


class GroupView(TemplateView):
    template_name = "group.html"


class PrivacyView(TemplateView):
    template_name = "privacy.html"


class TermsofuseView(TemplateView):
    template_name = "terms_of_use.html"


# def chubunrui_options(request):
#     """HTMX endpoint: trả về options cho 中分類"""
#     dai_code = request.GET.get("daibunrui")

#     chubunrui_list = Chubunrui.objects.none()
#     if dai_code:
#         chubunrui_list = Chubunrui.objects.filter(daibunrui_id=dai_code).values(
#             "code", "name"
#         )

#     return render(
#         request,
#         "inquiry/partials/_chubunrui_select.html",
#         {
#             "chubunrui_list": chubunrui_list,
#             "selected_dai": dai_code,
#             "disabled": not dai_code,
#         },
#     )


# def shobunrui_options(request):
#     """HTMX endpoint: trả về options cho 小分類"""
#     chu_code = request.GET.get("chubunrui")

#     shobunrui_list = Shobunrui.objects.none()
#     if chu_code:
#         shobunrui_list = Shobunrui.objects.filter(chubunrui_id=chu_code).values(
#             "code", "name"
#         )

#     return render(
#         request,
#         "inquiry/partials/_shobunrui_select.html",
#         {
#             "shobunrui_list": shobunrui_list,
#             "selected_chu": chu_code,
#             "disabled": not chu_code,
#         },
#     )

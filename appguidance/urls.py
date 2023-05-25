from django.urls import path
from appguidance import views

urlpatterns = [
        path("user",views.UserRegisterSerializersAPIView.as_view(),name="user"),
        path("shop",views.ShopRegisterSerializersAPIView.as_view(),name="shop"),
        path("work",views.WorkshopSerializerAPIView.as_view(),name="work"),
        path("product",views.productSerializersAPIView.as_view(),name="product"),
        path("order",views.orderSerializersAPIView.as_view(),name="order"),
        path("payment",views.paymentSerializersAPIView.as_view(),name="payment"),
        path("feedback",views.feedbackSerializersAPIView.as_view(),name="feedback"),
        path("notification",views.notificationSerializersAPIView.as_view(),name="notification"),
        path("complaints",views.complaintsSerializersAPIView.as_view(),name="complaints"),
        path("counciling",views.councilingSerializersAPIView.as_view(),name="counciling"),
        path("shops",views.shopSerializersAPIView.as_view(),name="shops"),  
        path("login",views.LoginUserAPIView.as_view(),name="login"), 
        path("get_all_product",views.Get_ProductAPIView.as_view(),name="get_all_product"), 
        path("get_single_product/<int:id>",views.SingleProductAPIView.as_view(),name="get_single_product"), 
        path("get_all_user",views.Get_UserRegisterAPIView.as_view(),name="get_all_user"),
        path("get_Single_user/<int:id>",views.SingleUserRegisterAPIView.as_view(),name="get_single_user"), 
        path("get_all_shop",views.Get_ShopRegisterAPIView.as_view(),name="get_all_shop"),
        path("get_Single_shop/<int:id>",views.SingleShopRegisterAPIView.as_view(),name="get_single_shop"), 
        path("get_all_notification",views.Get_notificationAPIView.as_view(),name="get_all_notification"),
        path("get_Single_notification/<int:id>",views.SinglenotificationAPIView.as_view(),name="get_single_notification"),
        path("get_all_complaints",views.Get_complaintsAPIView.as_view(),name="get_all_complaints"),
        path("get_Single_complaints/<int:id>",views.SinglecomplaintsAPIView.as_view(),name="get_single_complaints"), 
]


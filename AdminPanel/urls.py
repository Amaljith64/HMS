from django import views
from django.urls import path
from AdminPanel import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('viewroom',views.rooms,name='viewroom'),
    path('guest',views.guest,name='guest'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('addroom',views.addrooms,name='addroom'),
    path('editroom/<int:id>',views.editroom,name='editroom'),
    path('delete/<int:id>',views.deleteroom,name='deleteroom'),
    path('category',views.category,name='category'),
    path('editcategory/<int:id>',views.edit_category,name='editcategory'),
    path('subcategory',views.subcategory,name='subcategory'),
    path('bookings',views.bookings,name='bookings'),
    path('makecheckin/<int:id>',views.makecheckin,name='makecheckin'),
    path('makecheckout/<int:id>',views.makecheckout,name='makecheckout'),
    path('cancel/<int:id>',views.cancel,name='cancel'),
    path('deletebooking/<int:id>',views.delete,name='deletethebooking'),
    path('coupons',views.add_coupons,name='coupons'),
    path('editcoupons/<int:id>',views.edit_coupon,name='editcoupons'),


    #------------------------- category offer management ------------------------ #
    path("categoryoffers",views.CategoryOffer,name="categoryoffers"),
    path("editcategoryoffers/<int:id>/",views.Edit_CategoryOffer,name="EditCategoryOffer"),
    path("blockcategoryoffers/<int:id>/",views.Block_CategoryOffer,name="BlockCategoryOffer"),
    path("unblockcategoryoffers/<int:id>/",views.UnBlock_CategoryOffer,name="UnBlockCategoryOffer"),
    path("deletecategoryoffers/<int:id>/",views.Delete_CategoryOffer,name="DeleteCategoryOffer"),

#------------------------- subcategory offer management ------------------------ #
    path("subcategoryoffers",views.SubCategoryOffer,name="subcategoryoffers"),
    path("editsubcategoryoffers/<int:id>/",views.Edit_SubCategoryOffer,name="EditSubCategoryOffer"),
    # path("blocksubcategoryoffers/<int:id>/",views.Block_SubCategoryOffer,name="BlockSubCategoryOffer"),
    # path("unblocksubcategoryoffers/<int:id>/",views.UnBlock_SubCategoryOffer,name="UnBlockSubCategoryOffer"),
    # path("deletesubcategoryoffers/<int:id>/",views.Delete_SubCategoryOffer,name="DeleteSubCategoryOffer"),

#------------------------- Product offer management ------------------------ #
    path("roomoffer",views.RoomOffer,name="roomoffer"),
    path("editroomoffer/<int:id>/",views.Edit_RoomOffer,name="EditRoomOffer"),
    # path("blockproductoffers/<int:id>/",views.Block_ProductOffer,name="BlockProductOffer"),
    # path("unblockproductoffers/<int:id>/",views.UnBlock_ProductOffer,name="UnBlockProductOffer"),
    # path("deleteproductoffers/<int:id>/",views.Delete_ProductOffer,name="DeleteProductOffer"),

    path('salesreport',views.salesReport,name='SalesReport'),
    path("monthly_report/<int:date>/",views.monthly_report,name="monthly_report"),
    path("yearly_report/<int:date>/",views.yearly_report,name="yearly_report"),
    path("date_range",views.date_range,name="date_range"),
]

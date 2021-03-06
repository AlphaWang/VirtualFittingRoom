from django.conf.urls import patterns, url, include
from views.mainViews import index,redirect_to_index, members, logout, mainpage, top_menu, fittingroom,qunit, wishlist, profile, wishlistcontent, fitlistcontent, customlistcontent
from views.categoryViews import listProduct, category_list
from views.productViews import detail, detailpage, previewProduct, addProduct, addcustomimage, editcustomimage
from views.commentViews import addComment, getComments
from views.internalViews import setUpDb
from views.wishlistViews import getWishlist, removeFromWishlist, addToWishlist
from views.fitlistViews import getFitlist, removeFromFitlist, addToFitlist, getPreviewItem
from views.searchProductViews import searchProducts, search_list
from views.userViews import addProfilePic, getUserInfo, getProfilePic, getCustomItem, removeCustomItem, editCustomItem
from views.fittingroomViews import setConfig
urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^fittingroom/setconfig/(?P<token>[\w]+)', setConfig, name="setConfig"),
                       url(r'^addprofilepic', addProfilePic, name='addProfilePic'),
                       url(r'^getprofilepic', getProfilePic, name='getProfilePic'),
                       url(r'^getuserinfo', getUserInfo, name='getUserInfo'),
                       url(r'^getcustompage', getCustomItem, name='getCustomItem'),
                       url(r'^internal', setUpDb, name='internal'),
					   url(r'^profile', profile, name='profile'),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^login-error', redirect_to_index , name='redirect_to_index'),
                       url(r'^mainpage', mainpage, name='mainpage'),
					   url(r'^addcustomimage', addcustomimage, name='addcustomimage'),
					   url(r'^editcustomimage', editcustomimage, name='editcustomimage'),
                       url(r'^top_menu', top_menu, name='top_menu'),
					   url(r'^wishlistcontent', wishlistcontent, name='wishlistcontent'),
					   url(r'^fitlistcontent', fitlistcontent, name='fitlistcontent'),
					   url(r'^customlistcontent', customlistcontent, name='customlistcontent'),
					   url(r'^qunit', qunit, name='qunit'),
                       url(r'^fittingroom', fittingroom, name='fittingroom'),
					   url(r'^wishlist/$', wishlist, name='wishlist'),
                       url(r'^previewcustomitem/get/(?P<token>[\wd]+)', getPreviewItem, name='getPreviewItem'),
                       url(r'^previewcustomitem', previewProduct, name='previewProduct'),
                       url(r'^addcustomitem/(?P<token>[\w]+)', addProduct, name='addProduct'),         
                       url(r'^$', index, name='index'),
                       url(r'^searchResult/$', search_list, name='search_list'),
                       url(r'^searchResult/search/$' ,searchProducts, name='searchProducts' ),
                       url(r'^deletecustompage/(?P<id>[\d]+)', removeCustomItem,name='deleteCustomItem' ),
                       url(r'^editcustompage/(?P<id>[\d]+)/(?P<token>[\w]+)', editCustomItem,name='editCustomItem' ),
                       url(r'^(?P<category>[\w ]+)/$', category_list, name='category_list'),
                       url(r'^(?P<category>[\w ]+)/list/$' , listProduct, name='listProduct' ),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/$', detailpage, name='detailpage'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/info/$', detail, name='detail'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/comments/add$', addComment, name='addComment'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/comments/get/$', getComments, name='getComments'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/wishlist/add$', addToWishlist, name='addToWishlist'),
                       url(r'^wishlist/get/$', getWishlist, name='getWishlist'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/wishlist/remove$', removeFromWishlist, name='removeFromWishlist'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/fitlist/add$', addToFitlist, name='addToFitlist'),
                       url(r'^fitlist/get/$', getFitlist, name='getFitlist'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>(.+))_(?P<id>[\d]+)/fitlist/remove$', removeFromFitlist, name='removeFromFitlist'),
    
)   

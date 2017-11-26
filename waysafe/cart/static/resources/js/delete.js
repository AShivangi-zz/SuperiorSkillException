jQuery(document).ready(function($){

   var cartWrapper = $('.cd-cart-container');
   var test = $('.testcontainer');
   ///////////////////////

   // var quantityamount = document.getElementById('amount').value;




   function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
   }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

   ///////////////////////
   //product id - you don't need a counter in your real project but you can use your real product id
   var productId = 0;
   //
   // if( cartWrapper.length > 0 ) {
   //    //store jQuery objects
   //    var cartTestItemName = test.find('.itemname');
   //    //alert(cartTestItemName);
   //    var cartBody = cartWrapper.find('.body');
   //    var cartList = cartBody.find('ul').eq(0);
   //    var cartTotal = cartWrapper.find('.checkout').find('span');
   //    var cartTrigger = cartWrapper.children('.cd-cart-trigger');
   //    var cartCount = cartTrigger.children('.count');
   //    var addToCartBtn = $('.cd-add-to-cart');
   //    var undo = cartWrapper.find('.undo');
   //    var undoTimeoutId;
   //    var here = $('.qtyinput');

      //var quantityamount = $('.qtyinput');
     //var quantityamount = $("#amount").val();


       /*quantityamount.on('keyup mouseup' ,function (event){
            event.preventDefault();
            alert("IN HERE");
       }).trigger('mouseup');*/

    // if( cartWrapper.length > 0 ) {
    //   //store jQuery objects
    //   var cartTestItemName = test.find('.itemname')
    //   //alert(cartTestItemName);
    //   var cartBody = cartWrapper.find('.body');
    //   var cartList = cartBody.find('ul').eq(0);
    //   var cartTotal = cartWrapper.find('.checkout').find('span');
    //   var cartTrigger = cartWrapper.children('.cd-cart-trigger');
    //   var cartCount = cartTrigger.children('.count');
    //   var addToCartBtn = $('.cd-add-to-cart');
    //   var deleteitembutton = $('.delete-button');
    //   var undo = cartWrapper.find('.undo');
    //   var undoTimeoutId;
    //   var here = $('.qtyinput');


    var deleteitembutton = $('.delete-button');
//     deleteitembutton.on('click', function(event){
//         event.preventDefault();

//             id = $(this).attr('id');
//             quantity = $(this).attr('quantity');
//             name = $(this).attr('name');
//             // var quantityamount = document.getElementById(thisdata).value;
//             // var quantityamount = id = $(this).attr('id');

//             removeFromCart($(this), id,quantity);

//     });

    function removeFromCart(trigger, id,quantity){
        var cartIsEmpty = cartWrapper.hasClass('empty');

        removeProduct(id,quantity);
        //update number of items
        updateCartCount(cartIsEmpty);
        //update total price
        updateCartTotal(trigger.data('price'), true);
        //show cart
        cartWrapper.removeClass('empty');

    }
    function removeProduct(product,quantity) {
      // clearInterval(undoTimeoutId);
      // cartList.find('.deleted').remove();

      var topPosition = product.offset().top - cartBody.children('ul').offset().top ,
         productQuantity = Number(product.find('.quantity').find('select').val()),
         productTotPrice = Number(product.find('.price').text().replace('$', '')) * productQuantity;

      product.css('top', topPosition+'px').addClass('deleted');

      //update items count + total price
      updateCartTotal(productTotPrice, false);
      updateCartCount(true, -productQuantity);
      undo.addClass('visible');

      //wait 8sec before completely remove the item
      undoTimeoutId = setTimeout(function(){
         undo.removeClass('visible');
         cartList.find('.deleted').remove();
      }, 8000);
   }




});

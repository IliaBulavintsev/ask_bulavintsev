(function ($) {
  $('.spinner .btn:first-of-type').on('click', function() {
    $('.spinner input').val( parseInt($('.spinner input').val(), 10) + 1);
  });
  $('.spinner .btn:last-of-type').on('click', function() {
    $('.spinner input').val( parseInt($('.spinner input').val(), 10) - 1);
  });
})(jQuery);

var csrfModule = (function() {
    var _csrfToken = $.cookie('csrftoken');

    var _setUp = function() {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if(!_csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", _csrfToken);
                }
            }
        });
    };

    var _csrfSafeMethod = function(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    };

    return {
        init: function() {
            _setUp();
        }
    }
})();

var LogIn = (function(){

    var _refreshListeners = function() {
        $('.login_form').off();
        _addListeners();
    };

    var _addListeners = function() {
        $('.login_form').on('submit', _LogIn);
        $('.answer__form').on('submit', _answer);
    };

    var _LogIn = function(event){
        event.preventDefault();
        var data =$(this).serialize();
        $.ajax({
            url : "../login/",
            type : "POST",
            data :  data,
            dataType : 'json',
            success: function(json){
                if(json.status == 'ok'){
                    history.go(-1);
                } else {
                   $('.form-group').addClass('has-error')
                }
            },
            error: function(){
                $('.form-group').addClass('has-error')
            }
        });
        console.log(data)
    };

    var _answer = function(event){
        event.preventDefault();
        var data =$(this).serialize();
        $.ajax({
            url : "../../answer/",
            type : "POST",
            data :  data,
            dataType : 'json',
            success: function(json){
                if(json.status == 'ok'){
                    location.reload()
                } else {
                   $('.form-group').addClass('has-error')
                }
            },
            error: function(){
                $('.form-group').addClass('has-error')
            }
        });
        console.log(data)

    };

    var init = function () {
        _addListeners();
        console.log("init");
    };

    return {
       init : init
    };
})();


LogIn.init();
csrfModule.init();
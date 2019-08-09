function(){

        $('#time').click(function(){
                                    var time = moment().format('YYYY-MM-DDTHH:mm:ss');
                  $('#time-holder').val(time);
        });

    }

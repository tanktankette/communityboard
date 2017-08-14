/**
 * Created by tanktankette on 8/13/17.
 */

$(".check").click(function () {


    var check_url = $(location).attr('host') + $(this).attr('name');
    console.log(check_url);

    if ($(this).is(':checked')) {

        const pkg = {pk: $(this).val(), check: true};

        $.ajax({
            type: 'POST',
            url: '/tasklist/check',
            data: pkg,
            success: function (data) {
                console.log("yay")
            }
        })
    }
});
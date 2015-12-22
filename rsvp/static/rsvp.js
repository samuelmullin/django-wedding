function addRow(selector) {
    var newElement = $(selector).clone(true);
    var total = $('#id_form-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_form-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

function removeRow(selector) {
    var total = $('#id_form-TOTAL_FORMS').val();
    if (total != '1') {
        total--;
        $('#id_form-TOTAL_FORMS').val(total);
        $(".guest").last().remove();
    }
}

$(function () {

    $("input[type=radio]").click(function () {
        if (document.getElementById('id_rsvp_0').checked) {
            $('.rsvp').fadeIn();
        } else {
            $('.rsvp').fadeOut();
        }
    });

    $(".add-guest").click(function () {
        addRow($(".guest")[0])
    });

    $(".remove-guest").click(function () {
        removeRow($(".guest")[0])
    });

});

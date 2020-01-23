var graf;
jQuery(document).ready(function ($){
$('.plot').click(function (e) {
    clearInterval(graf);
    console.log(graf);
    const x1 = parseFloat($('.from').val());
    const x2 = parseFloat($('.to').val());
    const fun = ($('.fun').val());

    var x = x1;
    var i = x;
    var step = 1;
    var poinst = [x, eval(fun)];

    console.log(poinst);
    console.log(fun);
    if (i < x2)
    {
    graf=setInterval(function () {
        $.plot($('.graph'), [{label: fun, data: poinst}], {});
        x = x + (x2 - x1) / 100;
//        console.log(poinst);
        if (poinst.length > 100) {
            poinst.splice(1, 1)
        }
        poinst.push([x, eval(fun)])
    }, 100);
        i += parseFloat(step)
    }
    else
    {
        clearInterval(graf);
    }
});

$('.stop').click(function (e) {
    clearInterval(graf);
    console.log('Stop!');

});
});
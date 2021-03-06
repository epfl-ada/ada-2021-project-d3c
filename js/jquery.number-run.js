/**
 * jquery.number-run.js
 * jquery 数字滚动插件s
 *
 * By postbird - http://www.ptbird.cn
 * license:MIT
 */
 (function ($) {
    $.fn.numberRun = function (options) {
        var defaultOptions = {
            speed: 24, // 速度
            number: 100, // 需要滚动到的数字
            attr: false, // 是否从attr中获取相关参数
            callback: function () {} // 回调函数
        };
        var options = $.extend({}, defaultOptions, options);
        var domObj = this;
        if (options.attr) {
            options.speed = parseInt(domObj.attr("speed"));
            options.number = domObj.attr("number");
        }
        var baseNum = 100,
            number = options.number,
            speed = Math.floor(number / baseNum),
            sum = 0,
            step = 1,
            int_speed = parseInt(options.speed);
        var timer = setInterval(function () {
            if (step <= baseNum && speed != 0) {
                domObj.text(sum = speed * step);
                step++;
            } else if (sum < number) {
                domObj.text(++sum);
            } else {
                clearInterval(timer);
                // 最终的结果确保小数的情况
                domObj.text(options.number);
                // 执行一次 callback
                options.callback();
            }
        }, int_speed);

    }

})(jQuery);
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
      n =  x > 0 ? Number(String(x).split("").reverse().join("")) :
                     -Number(String(x).split("").slice(1).reverse().join(""))
    return (-2147483648 < n && n < 2147483647) ? n : 0
};

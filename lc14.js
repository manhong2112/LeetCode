/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
   if(strs == []) return ""
   if(strs.length == 1) return strs[0]
   let a = strs.shift() || ""
   let b = strs.shift() || ""
   let s = ""
   for(let i = 0;a[i] != undefined && a[i] === b[i];i++) {
       s += a[i]
   }
   return strs.length ? longestCommonPrefix(strs.concat([s])) : s;
};

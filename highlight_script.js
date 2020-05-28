Document.prototype.queryXPath = function (path) {

        var list = new Array();

        var xpath = document.evaluate(
          path,
          document,
          null,
          XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
          null
        );

        for (var i=0; i<xpath.snapshotLength; i++) {

          list.push(xpath.snapshotItem(i));

        };

        return list

}
var tableRows = document.queryXPath("//*[@id='RequestsView_TABLE']/tbody/tr");
console.log(tableRows);